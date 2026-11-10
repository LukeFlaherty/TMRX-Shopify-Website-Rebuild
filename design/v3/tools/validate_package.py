#!/usr/bin/env python3
"""Check V3 handoff integrity. Standard library only; does not test a website."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
errors = []
checks = []


def require(condition, message):
    if not condition:
        errors.append(message)


def load(path):
    return json.loads((ROOT / path).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_record(record, prefix=''):
    file = record['file']
    path = ROOT / file
    require(path.is_file(), f'Missing {prefix}{file}')
    require(path.resolve().is_relative_to(ROOT), f'Path escapes package: {file}')
    if path.is_file():
        require(path.stat().st_size == record['bytes'], f'Wrong byte count: {file}')
        require(sha(path) == record['sha256'], f'Hash mismatch: {file}')
        if path.suffix == '.png':
            raw = path.read_bytes()[:24]
            require(raw[:8] == b'\x89PNG\r\n\x1a\n', f'Invalid PNG: {file}')
            if len(raw) >= 24:
                width = int.from_bytes(raw[16:20], 'big')
                height = int.from_bytes(raw[20:24], 'big')
                require((width, height) == (record['width'], record['height']), f'PNG dimensions mismatch: {file}')
    for derivative in record.get('derivatives', []):
        file_record(derivative, 'derivative ')


def local_link(origin, href):
    if not href or href.startswith(('#', 'http:', 'https:', 'mailto:', 'tel:', 'data:')):
        return
    value = unquote(urlsplit(href).path)
    if not value:
        return
    target = origin.parent / value
    require(target.exists(), f'Broken local link in {origin.relative_to(ROOT)}: {href}')


def main():
    parsed = {}
    for path in ROOT.rglob('*.json'):
        try:
            parsed[path.relative_to(ROOT).as_posix()] = json.loads(path.read_text())
        except Exception as exc:
            errors.append(f'Invalid JSON {path}: {exc}')
    checks.append('All JSON files parse')
    if errors:
        return finish({})

    assets = load('manifests/assets.json')['assets']
    products = load('manifests/products.json')['products']
    pages = load('manifests/pages.json')['pages']
    ids = [a['id'] for a in assets]
    require(len(ids) == len(set(ids)), 'Duplicate asset IDs')
    require(len(pages) == 22, 'Expected 22 page/surface briefs')
    require(len({p['id'] for p in pages}) == len(pages), 'Duplicate page IDs')
    require(len(products) == 16, 'Expected 16 product source groups')
    sources = set(re.findall(r'\| (S\d+) \|', (ROOT/'research/sources.md').read_text()))
    for page in pages:
        require((ROOT/page['spec']).is_file(), f'Missing page spec: {page["id"]}')
        require(bool(page['required_states']), f'No states for {page["id"]}')
        for identity in page['asset_ids'] + page['mockup_ids']:
            require(identity in ids, f'Unknown asset {identity} in {page["id"]}')
        for source in page['source_ids']:
            require(source in sources, f'Unknown source {source}')
    checks.append('Route/spec/state/source/asset lookup is complete')

    for asset in assets:
        file_record(asset)
        if asset.get('prompt_ref'):
            require((ROOT/asset['prompt_ref']).is_file(), f'Missing prompt set {asset["id"]}')
        if asset['kind'] == 'photography':
            require(not asset['cross_page_reuse'], f'Photo reused across pages: {asset["id"]}')
            owners = [p['id'] for p in pages if asset['id'] in p['asset_ids']]
            require(owners == [asset['owner_page']], f'Owner mismatch {asset["id"]}: {owners}')
    require(sum(a['kind'] == 'photography' for a in assets) == 14, 'Expected 14 fresh photos')
    require(sum(a['kind'] == 'mockup' for a in assets) == 12, 'Expected 12 selected mockups')
    fresh = [a['sha256'] for a in assets if a['source_kind'] == 'generated-new']
    require(len(fresh) == len(set(fresh)), 'Duplicate fresh creative content hash')
    checks.append('Selected originals, derivatives, ownership and hashes verified')

    originals = 0
    for product in products:
        require((ROOT/product['primary_candidate']).is_file(), f'Missing product primary {product["id"]}')
        for media in product['media']:
            file_record(media)
            original = REPO/'assets'/Path(media['file']).name
            if original.exists():
                require(sha(original) == media['sha256'], f'Original source changed: {media["file"]}')
            originals += 1
        for derivative in product['primary_derivatives']:
            file_record(derivative)
    require(originals == 61, f'Expected 61 original product source images, found {originals}')
    checks.append('Product source groups and original-byte identity verified')

    quiz = load('manifests/quiz-rules.example.json')
    require(quiz['enabled'] is False, 'Unreviewed quiz fixture must remain disabled')
    require(quiz['rules'] == [], 'Fixture must not contain unreviewed product recommendations')
    require(quiz['email_required'] is False, 'Quiz must not require email')
    checks.append('Unreviewed quiz fixture cannot be mistaken for enabled rules')

    for path in ROOT.rglob('*.md'):
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            local_link(path, href.strip('<>'))
    for path in ROOT.rglob('*.html'):
        for href in re.findall(r'(?:href|src)="([^"]+)"', path.read_text()):
            local_link(path, href)
    for path in ROOT.rglob('*.svg'):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f'Invalid SVG: {path}: {exc}')
    checks.append('Markdown/HTML local links and SVG XML checked')

    def lum(value):
        rgb = [int(value[i:i+2], 16)/255 for i in (1, 3, 5)]
        linear = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in rgb]
        return sum(a*b for a, b in zip(linear, (.2126, .7152, .0722)))

    colors = load('specs/tokens.json')['color']
    contrasts = {}
    for fg, bg, minimum in [('ink', 'canvas', 4.5), ('muted', 'canvas', 4.5),
                            ('canvas', 'action', 4.5), ('action', 'canvas', 4.5),
                            ('controlBorder', 'canvas', 3), ('focus', 'canvas', 3)]:
        values = sorted([lum(colors[fg]), lum(colors[bg])])
        ratio = (values[1]+.05)/(values[0]+.05)
        contrasts[f'{fg}/{bg}'] = round(ratio, 2)
        require(ratio >= minimum, f'Contrast {fg}/{bg} {ratio:.2f} below {minimum}')
    checks.append('Key token text/control contrast pairs measured')
    finish({'pages': len(pages), 'photos': 14, 'mockups': 12,
            'products': len(products), 'original_product_images': originals,
            'contrast_ratios': contrasts})


def finish(summary):
    result = {'version': '3.0.0', 'scope': 'Design package integrity only; no website functional tests.',
              'passed': not errors, 'checks': checks, 'errors': errors, **summary}
    (ROOT/'qa/package-validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
