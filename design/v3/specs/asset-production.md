# Asset production and placement

## Asset classes

`Axx` = new page-owned photographic master; `Mxx` = new generated visual-reference mockup; `B01` = authentic logo; `PRxx` = original product media group. The manifest records file dimensions, SHA-256, owner, crop, alt intent, provenance, production role and derivative paths. Use IDs, not guesswork from filenames.

All text-free photography was generated with the built-in image_gen tool using the exact saved prompt set. Original PNGs are retained. WebP derivatives are supplied for efficient implementation; never upscale an undersized file to satisfy an export target. Master dimensions are observed, not promised dimensions from a generation prompt.

## Freshness and ownership

An original editorial image belongs to its listed page slot. Do not put the homepage goal photo on the quiz, journal and contact pages as filler. The same slot can use a responsive crop on desktop/mobile unless it has a separately authored mobile plate, such as A01/A02. Shared packshots, logo and new component primitives are the explicit exceptions. Utility pages intentionally use typography rather than recycled decorative photography.

## Product staging recipes

The plates are intentionally empty. Compose original product media as separate HTML image layers in a responsive media region, so labels remain faithful. Do not use AI-generated label text from a mockup. These are suggested initial placement bounds; refine the contact point visually with the real PNG transparency, preserve aspect ratio and do not stretch.

| Slot | Plate | Authentic layers | Position guidance in media region |
|---|---|---|---|
| Home desktop | A01 | Aminos front, Bone Broth front, Omega front | Products sit on right-hand platforms; approximate centers 63%, 81%, 91%; bottom contacts ~72%, 57%, 81% depending crop |
| Home mobile | A02 | Same actual identities | Centered cluster; use back high stone for tall Bone Broth, low front stone for Aminos; crop plate before scaling product layers |
| Collection masthead | A08 | Optional category-specific originals | Keep imagery low-profile, right half on desktop; hide grouping if small-screen title needs room |
| Essential Aminos gallery | A09 | Aminos front only | Center product, base near top of slab; size around 55–65% media height; real label legible |

Layer coordinates are art-direction starting points, not pixel-perfect guarantees. The generated mockup may depict different stone geometry. The shipped plate plus original product PNGs are the source. A generic missing product photo gets a simple neutral missing-image treatment, never a red block or unrelated product image.

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
