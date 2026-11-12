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
METADATA = json.loads((ROOT/'package-metadata.json').read_text())
EXPECTED = METADATA['expected']
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
    require(len(pages) == EXPECTED['pages'], 'Unexpected page/surface count')
    require(len({p['id'] for p in pages}) == len(pages), 'Duplicate page IDs')
    require(len(products) == EXPECTED['product_groups'], 'Unexpected product group count')
    by_id = {a['id']: a for a in assets}
    product_handles = {p['handle'] for p in products}
    sources = set(re.findall(r'\| (S\d+) \|', (ROOT/'research/sources.md').read_text()))
    for page in pages:
        require((ROOT/page['spec']).is_file(), f'Missing page spec: {page["id"]}')
        require(bool(page['required_states']), f'No states for {page["id"]}')
        for identity in page['asset_ids'] + page['mockup_ids']:
            require(identity in ids, f'Unknown asset {identity} in {page["id"]}')
        for source in page['source_ids']:
            require(source in sources, f'Unknown source {source}')
        for identity in page.get('preferred_asset_ids', []):
            require(identity in page['asset_ids'], f'Preferred asset outside page: {identity}')
            require(by_id.get(identity, {}).get('contains_products'), f'Preferred photo has no products: {identity}')
    checks.append('Route/spec/state/source/asset lookup is complete')

    for asset in assets:
        file_record(asset)
        if asset.get('prompt_ref'):
            require((ROOT/asset['prompt_ref']).is_file(), f'Missing prompt set {asset["id"]}')
        if asset['kind'] == 'photography':
            require(not asset['cross_page_reuse'], f'Photo reused across pages: {asset["id"]}')
            owners = [p['id'] for p in pages if asset['id'] in p['asset_ids']]
            require(owners == [asset['owner_page']], f'Owner mismatch {asset["id"]}: {owners}')
    photos = sum(a['kind'] == 'photography' for a in assets)
    mockups = sum(a['kind'] == 'mockup' for a in assets)
    require(photos == EXPECTED['photography'], 'Unexpected photographic asset count')
    require(mockups == EXPECTED['mockups'], 'Unexpected mockup count')
    variants = [a for a in assets if a.get('variant_of')]
    require(len(variants) == 12, 'Expected 12 product-included variants')
    for asset in variants:
        parent = by_id.get(asset['variant_of'], {})
        require(parent.get('owner_page') == asset['owner_page'], f'Variant owner mismatch: {asset["id"]}')
        require(parent.get('preferred_variant_id') == asset['id'], f'Variant not preferred by parent: {asset["id"]}')
        require(asset.get('contains_products') and asset.get('product_handles'), f'Missing product identity: {asset["id"]}')
        require(set(asset.get('product_handles', [])) <= product_handles, f'Unknown product in {asset["id"]}')
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
    require(originals == EXPECTED['original_product_images'], f'Unexpected original product source count: {originals}')
    checks.append('Product source groups and original-byte identity verified')

    roadmap = load('manifests/development-roadmap.json')
    tasks = roadmap['tasks']
    task_ids = {t['id'] for t in tasks}
    require(len(tasks) == EXPECTED['roadmap_tasks'], 'Unexpected roadmap task count')
    require(len(task_ids) == len(tasks), 'Duplicate roadmap task IDs')
    phase_ids = {p['id'] for p in roadmap['phases']}
    require(len(phase_ids) == 13, 'Expected 13 roadmap phases')
    page_ids = {p['id'] for p in pages}
    mapped_pages = set()
    for task in tasks:
        require(task['phase'] in phase_ids, f'Unknown phase: {task["id"]}')
        require(set(task['depends_on']) <= task_ids, f'Unknown task dependency: {task["id"]}')
        require(set(task['page_ids']) <= page_ids, f'Unknown task page: {task["id"]}')
        mapped_pages.update(task['page_ids'])
        for field in ('inputs', 'deliverables', 'acceptance', 'file_targets'):
            require(bool(task.get(field)), f'Missing {field}: {task["id"]}')
        require(task['status'] in roadmap['status_vocabulary'], f'Unknown status: {task["id"]}')
        if task['status'] == 'verified':
            require(bool(task.get('verification_evidence')) and bool(task.get('commit')), f'Verified task lacks evidence: {task["id"]}')
    require(mapped_pages == page_ids, 'Roadmap does not cover every page/surface')
    sku_tasks = [t for t in tasks if t['id'].startswith('SKU')]
    require({t['product_handle'] for t in sku_tasks} == product_handles, 'SKU checks do not cover all product groups')
    remaining = {t['id']: set(t['depends_on']) for t in tasks}
    while remaining:
        ready = {identity for identity, deps in remaining.items() if not deps}
        if not ready:
            errors.append('Roadmap dependencies contain a cycle')
            break
        remaining = {identity: deps-ready for identity, deps in remaining.items() if identity not in ready}
    for identity, required in [('P05', {'M13', 'M14', 'M17', 'M18'}), ('P06', {'M15', 'M16', 'M17', 'M18'})]:
        page = next(p for p in pages if p['id'] == identity)
        require(required <= set(page['mockup_ids']), f'Missing cart visual coverage: {identity}')
    checks.append('Product-filled variants, cart references and complete acyclic roadmap checked')

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
    finish({'pages': len(pages), 'photos': photos, 'mockups': mockups,
            'product_variants': len(variants), 'roadmap_tasks': len(tasks), 'roadmap_phases': len(phase_ids),
            'products': len(products), 'original_product_images': originals,
            'contrast_ratios': contrasts})


def finish(summary):
    result = {'version': METADATA['version'], 'scope': 'Design package integrity only; no website functional tests.',
              'passed': not errors, 'checks': checks, 'errors': errors, **summary}
    (ROOT/'qa/package-validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
