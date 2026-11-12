#!/usr/bin/env python3
"""Build the offline V3 catalog, derivatives and inventories; requires Pillow.

Run from any directory. Does not call image generation or modify theme source.
Original generated/source masters are never overwritten. Rebuild after adding
generation records or changing page/asset metadata, then run validate_package.py.
"""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
import hashlib
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def write(path, value):
    (ROOT / path).write_text(json.dumps(value, indent=2) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def info(path):
    with Image.open(path) as image:
        return {'width': image.width, 'height': image.height,
                'mode': image.mode, 'bytes': path.stat().st_size,
                'sha256': sha(path)}


def derivatives(path, widths):
    outputs = []
    with Image.open(path) as source:
        source = ImageOps.exif_transpose(source)
        for width in widths:
            if width > source.width:
                continue
            height = round(source.height * width / source.width)
            output = path.with_name(f'{path.stem}-{width}.webp')
            if output.exists() and output.stat().st_mtime >= path.stat().st_mtime:
                current = info(output)
                if (current['width'], current['height']) == (width, height):
                    outputs.append({'file': output.relative_to(ROOT).as_posix(), **current})
                    continue
            scaled = source.resize((width, height), Image.Resampling.LANCZOS)
            scaled.save(output, 'WEBP', quality=86, method=6)
            outputs.append({'file': output.relative_to(ROOT).as_posix(), **info(output)})
    return outputs


OWNERS = {
    'A01': ('P01', 'hero-desktop', [0.78, 0.68], '', 'decorative-compositing-plate'),
    'A02': ('P01', 'hero-mobile', [0.5, 0.7], '', 'decorative-compositing-plate'),
    'A03': ('P01', 'goal-daily-nutrition', [0.53, 0.5], 'Preparing a morning shake in a bright kitchen.', 'editorial-photo'),
    'A04': ('P01', 'goal-strength', [0.5, 0.45], 'Everyday strength training with dumbbells.', 'editorial-photo'),
    'A05': ('P01', 'goal-recovery', [0.5, 0.5], 'A relaxed stretch beside a sunlit window.', 'editorial-photo'),
    'A06': ('P01', 'goal-wellness', [0.55, 0.45], 'A morning walk on a green trail.', 'editorial-photo'),
    'A07': ('P01', 'standards-editorial', [0.5, 0.55], 'Water, a measuring scoop and folded linen.', 'editorial-photo'),
    'A08': ('P02', 'collection-masthead', [0.78, 0.65], '', 'decorative-compositing-plate'),
    'A09': ('P04', 'essential-aminos-gallery', [0.5, 0.7], '', 'decorative-compositing-plate'),
    'A10': ('P04', 'essential-aminos-routine', [0.53, 0.45], 'A shaker as part of a simple morning routine.', 'editorial-photo'),
    'A11': ('P08', 'quiz-entry', [0.5, 0.5], '', 'decorative-editorial'),
    'A12': ('P10', 'featured-story', [0.56, 0.5], 'A chocolate shake with a small bowl of powder.', 'editorial-photo'),
    'A13': ('P11', 'example-article-hero', [0.5, 0.5], 'Everyday foods and a shake arranged on a table.', 'editorial-photo'),
    'A14': ('P12', 'about-hero', [0.55, 0.45], 'Two adults walking together beside the coast.', 'editorial-photo'),
}


def font(size):
    for candidate in ['/System/Library/Fonts/Supplemental/Arial.ttf',
                      '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default(size=size)


def sheet(rows, output, title, columns=4, image_height=220):
    cell_w, cell_h = 340, image_height + 70
    count_rows = (len(rows) + columns - 1) // columns
    canvas = Image.new('RGB', (columns * cell_w + 40, count_rows * cell_h + 100), '#EDF7FE')
    draw = ImageDraw.Draw(canvas)
    draw.text((24, 22), title, fill='#101820', font=font(28))
    for i, row in enumerate(rows):
        x, y = 20 + i % columns * cell_w, 80 + i // columns * cell_h
        with Image.open(ROOT / row['file']) as im:
            im = im.convert('RGBA')
            backdrop = Image.new('RGBA', im.size, 'white')
            backdrop.alpha_composite(im)
            thumb = ImageOps.contain(backdrop.convert('RGB'), (cell_w-16, image_height), Image.Resampling.LANCZOS)
            canvas.paste(thumb, (x + (cell_w-16-thumb.width)//2, y))
        label = row.get('title', row.get('slug', row['id']))
        draw.text((x+4, y+image_height+8), row['id'], fill='#0067B8', font=font(17))
        for n, part in enumerate([label[:34], label[34:68]]):
            if part:
                draw.text((x+58, y+image_height+8+n*20), part, fill='#101820', font=font(15))
    canvas.save(ROOT / output)


def main():
    metadata = read('package-metadata.json')
    version = metadata['version']
    records = read('manifests/generation-records.json')
    pages = read('manifests/pages.json')['pages']
    assets = []
    for record in records:
        path = ROOT / record['target']
        identity = record['id']
        owners = [p['id'] for p in pages if identity in p['mockup_ids']]
        row = {'id': identity, 'file': record['target'], 'slug': record['slug'],
               'kind': record['kind'], 'source_kind': 'generated-new',
               'created': record.get('created', '2026-11-10'), 'generation_tool': 'built-in image_gen',
               'status': record['status'], **info(path)}
        if record['kind'] == 'photography':
            if record.get('variant_of'):
                owner, slot, focal, alt, role = (record['owner_page'], record['slot'],
                    record['focal_point'], record['suggested_alt'], record['production_role'])
            else:
                owner, slot, focal, alt, role = OWNERS[identity]
            row.update(owner_page=owner, slot=slot, focal_point=focal, suggested_alt=alt,
                       production_role=role, cross_page_reuse=False,
                       prompt_ref=record.get('prompt_ref', 'prompts/photography.json'),
                       derivatives=derivatives(path, [480, 768, 1200, 1600]))
            if record.get('variant_of'):
                row.update(variant_of=record['variant_of'], contains_products=True,
                    product_handles=record['product_handles'], preferred_for_slot=True,
                    label_status='Compare with current authentic source before launch; never a label-data source')
        else:
            row.update(owner_pages=owners, viewport=record['viewport'],
                       production_role='reference-only-not-a-runtime-asset',
                       prompt_ref=record['prompt_ref'],
                       derivatives=derivatives(path, [320]))
        assets.append(row)

    by_id = {a['id']: a for a in assets}
    for asset in assets:
        if asset.get('variant_of'):
            by_id[asset['variant_of']]['preferred_variant_id'] = asset['id']
            by_id[asset['variant_of']]['preferred_for_slot'] = False

    logo = ROOT / 'assets/brand/true-matrx-logo-original.png'
    assets.append({'id': 'B01', 'file': logo.relative_to(ROOT).as_posix(),
                   'slug': 'authentic-logo', 'kind': 'brand',
                   'source_kind': 'authentic-source-exception',
                   'original_repository_path': 'assets/tmrx-logo.png',
                   'status': 'original-brand-source', 'suggested_alt': 'True Matrx',
                   'production_role': 'brand-identity', **info(logo)})

    for identity, file, label in [('V01', 'assets/brand/v3-icons.svg', 'new-line-icons'),
                                  ('V02', 'assets/brand/v3-curve.svg', 'new-decorative-curve')]:
        path = ROOT / file
        assets.append({'id': identity, 'file': file, 'slug': label, 'kind': 'vector',
                       'source_kind': 'new-code-native-vector', 'status': 'design-ready',
                       'bytes': path.stat().st_size, 'sha256': sha(path),
                       'production_role': 'new-vector-component-resource'})

    write('manifests/assets.json', {'version': version, 'path_base': 'design/v3',
                                  'assets': assets})

    product_rows = []
    for observed in read('research/catalog-observations.json')['products']:
        low, high = observed['local_media_range']
        files = [p for p in sorted((ROOT/'assets/products').glob('*.png'))
                 if low <= int(p.name[:2]) <= high]
        primary = files[0]
        media = [{'file': p.relative_to(ROOT).as_posix(), **info(p)} for p in files]
        product_rows.append({**observed, 'source_kind': 'authentic-source-exception',
                             'media': media,
                             'primary_candidate': primary.relative_to(ROOT).as_posix(),
                             'primary_status': 'visual-candidate-verify-current-variant-and-label',
                             'primary_derivatives': derivatives(primary, [360, 720, 1080])})
        if media[0]['width'] < 720:
            product_rows[-1]['source_quality'] = 'Low-resolution original; obtain better authentic media for a large gallery.'
    write('manifests/products.json', {'version': version, 'observed_date': '2026-11-10',
                                    'runtime_use': 'Never use as a live price/inventory database.',
                                    'products': product_rows})

    photos = [a for a in assets if a['kind'] == 'photography']
    mockups = [a for a in assets if a['kind'] == 'mockup']
    variants = [a for a in photos if a.get('contains_products')]
    carts = [a for a in mockups if int(a['id'][1:]) >= 13]
    sheet(photos, 'qa/photography-contact-sheet.jpg', f'True Matrx V3 — {len(photos)} photographic assets')
    sheet(mockups, 'qa/page-contact-sheet.jpg', f'True Matrx V3 — {len(mockups)} page references', columns=4, image_height=360)
    sheet(variants, 'qa/product-variant-contact-sheet.jpg', 'True Matrx V3 — product-included variants')
    sheet(carts, 'qa/cart-contact-sheet.jpg', 'True Matrx V3 — drawer, page and recommendation states', columns=3, image_height=350)
    sheet([{'id': p['id'], 'file': p['primary_candidate'], 'title': p['title']} for p in product_rows],
          'qa/product-source-contact-sheet.jpg', 'True Matrx — original source candidates, verify before binding', columns=4)

    def esc(value):
        return html.escape(str(value), quote=True)

    def card(a):
        preview = a.get('derivatives', [{}])[0].get('file', a['file'])
        title = a.get('slug', a['id']).replace('-', ' ')
        variant_note = ('Product-filled variant of '+a['variant_of']+' · preferred for its slot') if a.get('variant_of') else ('Preferred variant: '+a['preferred_variant_id']) if a.get('preferred_variant_id') else ''
        return f'''<article class="asset" data-search="{esc(a['id']+' '+title+' '+a['kind']+' '+variant_note)}">
        <a href="{esc(a['file'])}"><img loading="lazy" src="{esc(preview)}" alt="{esc(title)}"></a>
        <h3>{esc(a['id'])} · {esc(title)}</h3><p>{esc(a['production_role'])}</p>
        <p>{esc(variant_note)}</p>
        <p>{a['width']} × {a['height']} · {esc(a['status'])}</p>
        <a href="{esc(a['file'])}">Open original</a></article>'''

    page_links = ''.join(f'<tr><td>{esc(p["id"])}</td><td><a href="{esc(p["spec"])}">{esc(p["title"])}</a></td><td>{esc(", ".join(p["routes"]))}</td><td>{esc(", ".join(p["mockup_ids"]) or "Written specification")}</td></tr>' for p in pages)
    product_cards = ''.join(f'<article class="asset" data-search="{esc(p["title"])}"><a href="{esc(p["primary_candidate"])}"><img loading="lazy" src="{esc(p["primary_derivatives"][0]["file"] if p["primary_derivatives"] else p["primary_candidate"])}" alt="{esc(p["title"])}"></a><h3>{esc(p["id"])} · {esc(p["title"])}</h3><p>Authentic source exception; verify current variant/label.</p><a href="{esc(p["source_url"])}">Public product source</a></article>' for p in product_rows)
    doc = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>True Matrx · V3 redesign package</title>
    <style>:root{font-family:system-ui,sans-serif;color:#101820;background:#fff}*{box-sizing:border-box}body{margin:0}header{background:#edf7fe;padding:40px max(24px,5vw)}h1{font-size:38px;line-height:1.1;margin:12px 0}h2{font-size:28px}p{line-height:1.5;max-width:85ch}a{color:#0067b8}a:focus-visible,input:focus-visible{outline:3px solid #003f73;outline-offset:3px}nav{display:flex;gap:20px;flex-wrap:wrap;padding:20px 0}main{max-width:1450px;margin:auto;padding:24px}section{margin:36px 0 56px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:28px}.asset{border-top:1px solid #c9e2f3;padding-top:16px}.asset img{width:100%;height:230px;object-fit:contain;background:#fafcfe}.mockups img{height:500px}.asset h3{font-size:17px;line-height:1.4}.asset p{font-size:14px;color:#536270}input{font:inherit;min-height:48px;padding:12px;width:min(100%,480px);border:1px solid #708494}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:14px 10px;border-bottom:1px solid #c9e2f3;vertical-align:top}.table-wrap{overflow:auto}footer{padding:24px;border-top:1px solid #c9e2f3}label{display:block;margin:8px 0}.logo{max-width:230px;height:auto}[hidden]{display:none!important}@media(max-width:600px){h1{font-size:30px}.grid{grid-template-columns:1fr}.mockups img{height:460px}}</style>
    <header><img class="logo" src="assets/brand/true-matrx-logo-original.png" alt="True Matrx"><p>V3 REDESIGN · VERSION 3.0.0 · NOVEMBER 10, 2026</p><h1>A higher standard. A clear design handoff.</h1><p>Fresh creative, researched flows, page-by-page specifications and original brand/product sources. This is a local design catalog, not a functioning storefront or deployed Shopify theme.</p><nav><a href="README.md">Package guide</a><a href="BUILDER-HANDOFF.md">Builder start</a><a href="#pages">Page lookup</a><a href="#mockups">Page references</a><a href="#photos">Photography</a><a href="#products">Product sources</a><a href="qa/visual-review.md">Visual caveats</a></nav><label for="find">Filter assets by name or ID</label><input id="find" type="search" placeholder="Try A09, product, mobile…"></header><main>
    <section id="pages"><h2>22 page briefs and surfaces</h2><p>Written specs and current Shopify data override generated screenshot text. Supporting pages have intentional written layouts. Fresh imagery has one page owner; authentic packshots/logo are the disclosed identity exceptions.</p><div class="table-wrap"><table><thead><tr><th>ID</th><th>Brief</th><th>Route/surface</th><th>Reference</th></tr></thead><tbody>'''+page_links+'''</tbody></table></div></section>
    <section id="cart"><h2>Cart page, drawer and interaction states</h2><p>Visual recommendations with Add to bag controls. Read the <a href="specs/cart-experience.md">no-reload cart specification</a> and <a href="qa/cart-scenarios.md">functional acceptance matrix</a>. Images are concepts, not working cart code.</p><div class="grid mockups">'''+''.join(card(a) for a in carts)+'''</div></section>
    <section id="mockups"><h2>'''+str(len(mockups))+''' page and state references</h2><p>Composition references only. No generated product labels, prices, medical prose or interface states are a runtime source. Open the full-resolution file to inspect.</p><div class="grid mockups">'''+''.join(card(a) for a in mockups)+'''</div></section>
    <section id="product-variants"><h2>Product-included B-roll variants</h2><p>Preferred variants for most product-staging and B-roll slots. Products are already in these images: do not overlay them a second time. Compare packaging with current original sources before launch.</p><div class="grid">'''+''.join(card(a) for a in variants)+'''</div></section>
    <section id="photos"><h2>'''+str(len(photos))+''' photographic masters and variants</h2><p>Product-filled variants are preferred where mapped. Empty staging plates remain optional source material, not the default finished image.</p><div class="grid">'''+''.join(card(a) for a in photos)+'''</div></section>
    <section id="products"><h2>16 authentic product source groups</h2><p>Unmodified original media, not newly generated products. Primary candidates below require current-variant and label verification. All original views/labels are indexed in the product manifest.</p><div class="grid">'''+product_cards+'''</div></section>
    <section><h2>Supporting design resources</h2><p><a href="specs/tokens.json">Design tokens</a> · <a href="assets/brand/v3-icons-preview.svg">New icon preview</a> · <a href="assets/brand/v3-curve.svg">New background curve</a> · <a href="research/sources.md">Research sources</a> · <a href="DECISIONS.md">Open decisions</a> · <a href="qa/implementation-checklist.md">Build acceptance</a></p></section></main><footer>True Matrx V3 — design-ready package, pending merchant review and real implementation.</footer>
    <script>document.querySelector('#find').addEventListener('input',e=>{const q=e.target.value.toLowerCase();document.querySelectorAll('[data-search]').forEach(a=>a.hidden=!a.dataset.search.toLowerCase().includes(q));});</script></html>'''
    doc = doc.replace('VERSION 3.0.0 · NOVEMBER 10, 2026', 'VERSION '+version+' · NOVEMBER 12, 2026')
    doc = doc.replace('<a href="#pages">Page lookup</a>', '<a href="DEVELOPMENT-ROADMAP.md">92-task roadmap</a><a href="#product-variants">Product-filled B-roll</a><a href="#cart">Cart designs</a><a href="#pages">Page lookup</a>')
    (ROOT/'index.html').write_text(doc)
    print(f'Built {len(photos)} photos, {len(mockups)} mockups, {len(product_rows)} product groups, catalog and contact sheets.')


if __name__ == '__main__':
    main()
