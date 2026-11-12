# Asset production and placement

## Asset classes

`Axx` = new page-owned photographic master; `Mxx` = new generated visual-reference mockup; `B01` = authentic logo; `PRxx` = original product media group. The manifest records file dimensions, SHA-256, owner, crop, alt intent, provenance, production role and derivative paths. Use IDs, not guesswork from filenames.

All text-free photography was generated with the built-in image_gen tool using the exact saved prompt set. Original PNGs are retained. WebP derivatives are supplied for efficient implementation; never upscale an undersized file to satisfy an export target. Master dimensions are observed, not promised dimensions from a generation prompt.

## Freshness and ownership

An original editorial image belongs to its listed page slot. Do not put the homepage goal photo on the quiz, journal and contact pages as filler. The same slot can use a responsive crop on desktop/mobile unless it has a separately authored mobile plate, such as A01/A02. Shared packshots, logo and new component primitives are the explicit exceptions. Utility pages intentionally use typography rather than recycled decorative photography.

## Product-included variants — preferred in revision 3.1

Twelve finished variants A15–A26 now include products. Use them for most B-roll and staging slots rather than displaying empty pedestals. `preferred_asset_ids` on each page and `preferred_variant_id` on original assets provide the exact lookup. The 14 originals remain available as alternate source material; these additions do not erase provenance or change the approved theme.

| Finished variant | Original slot | Page | Product identity |
|---|---|---|---|
| A15 / A16 | A01 / A02 desktop/phone hero | P01 | Essential Aminos, Bone Broth Protein, Premium Omega |
| A17 | A07 standards still life | P01 | Essential Aminos, Premium Omega |
| A18 | A08 collection masthead | P02 | Essential Aminos, Bone Broth Protein, Premium Omega |
| A19 | A09 Aminos gallery staging | P04 | Essential Aminos |
| A20 | A10 Aminos routine | P04 | Essential Aminos |
| A21 | A11 quiz entry | P08 | Essential Aminos, Premium Omega |
| A22 | A12 journal feature | P10 | Bone Broth Protein |
| A23 | A13 article hero | P11 | Bone Broth Protein |
| A24 | A03 nutrition goal | P01 | Bone Broth Protein |
| A25 | A04 strength goal | P01 | Micronized Creatine |
| A26 | A05 recovery goal | P01 | Calm |

Products are already present in these finished images: do not overlay a second packshot. Product handles are metadata in the asset manifest, not an eligibility, dosage or health claim. A06 wellness walk and A14 about remain intentionally people-led. Editorial photos remain owned by their page; the Aminos editorial must not become another SKU's product gallery.

These variants were generated as edits using the authentic product files and original slot image as references. Packaging still requires comparison with the current approved source before launch. Never extract Supplement Facts, label text or claims from a generated photo. Grid images, cart photos and factual gallery/label views continue to use authentic current product media. If a generated label differs, use a verified retouch or a faithful original-media composition before launch.

## Optional separate-layer composition

If a product assortment or variant changes, the empty originals A01/A02/A08/A09 remain useful for composing current authentic product media. Use one approach per media region: a finished product-filled image OR an original empty plate with separate product layers. Keep native proportions, transparent edges and a natural contact shadow. On the desktop hero retain clear left-side space for copy; on phone keep the cluster centered and avoid cropping the packaging. A missing product photo receives a neutral missing-image treatment, never an unrelated product.

## Product source library

Original files are grouped by product in `manifests/products.json`. Each preserves the original filename and unmodified bytes. They are reference assets for the current brand, not a newly verified photography shoot. Many files are labels, alternate angles or directions, not grid front views. Primary candidates are identified for convenience and must be checked against the actual Shopify variant before publication. A historical label must never override current approved Supplement Facts or warnings.

The supplied Secretropin source is only 265 × 503px. Its original is included, but no larger derivative is generated and it must not be stretched into a high-resolution hero or label zoom. Obtain a better authentic source before that product's large-gallery launch. The other primary source candidates were inspected together in the product contact sheet; inspection confirms visual identity only, not current label approval.

## Cropping and exports

People/goal images: use `object-fit: cover`, with the manifest's focal point, never cut off the face or primary hand action. Product sources: `contain`; maintain alpha. Decorative stone: cover at its page's aspect ratio; alt text empty if products/content already describe the purpose. Journal feature: 3:2 desktop and 4:3 phone crop. Article hero: 16:9 desktop, 4:3 phone if the whole-food composition remains intelligible.

Create responsive `srcset` candidates at widths 480, 768, 1200 and 1600 where the original supports them. Product media candidates 360, 720 and 1080 where supported. Use width/height attributes and suitable `sizes`. Hero may load eagerly with high priority; below-fold media is lazy. Do not preload every photo.

## Implementation budgets

V3 internal targets: mobile hero image under 180KB when practical, desktop hero under 300KB, goal tile under 100KB, grid packshot under 90KB. These are optimization targets, not claims that every supplied master already meets them. Original lossless masters are not intended to be uploaded wholesale to theme assets. Select only mapped derivatives, with Shopify image transforms where media is in Files/product media.

Local preview/rebuild tooling needs Python and Pillow. Example: create a virtual environment, install Pillow there, then run `python design/v3/tools/build_catalog.py`. The validator uses only the standard library. No image-generation API calls occur in either tool.

## Icons and background motifs

V3's small line-icon sheet and curve motif are newly authored vectors, not stand-ins for the requested photography. Icons use 24px viewboxes, 1.75px stroke, rounded caps, no filled pictograms. Use native controls and accessible labels. Decorative SVG instances are hidden from assistive technology. The authentic brand logo is kept as the original raster; do not trace or redraw it.
