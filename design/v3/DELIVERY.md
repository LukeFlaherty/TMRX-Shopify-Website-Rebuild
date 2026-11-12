# V3 delivery inventory

Version 3.1.0, November 12, 2026.

- **22 dedicated page/surface briefs**, each with content order, phone/desktop layout, required data and state-specific acceptance criteria.
- **18 generated visual references**: the original 12 plus six new desktop/phone cart drawer, full cart page and recommendation/empty-state concepts.
- **26 page-owned photographic masters and variants**: 14 originals plus 12 new product-included B-roll/staging variants, now preferred in mapped page slots. Empty originals remain alternate source material.
- **16 product identity groups with 61 original source images**, preserving actual branding and labels as disclosed identity exceptions. One authentic logo source.
- **145 WebP derivatives**, new line-icon sprite/preview and subtle background-curve SVG, plus page/photo/product, product-variant and cart contact sheets.
- Machine-readable route, asset and product manifests; tokens and copy dictionary; exact image-generation prompts and correction log.
- Research/source ledger, dated product observations, component and data contracts, responsive guidance, content direction, decisions and future implementation checks.
- A local searchable HTML catalog, standard-library integrity validator and ZIP packaging tool.
- **92 development tasks across 13 phases**, with dependencies, all 22 page/surface mappings, 16 individual product checks, acceptance conditions and an iteration evidence template.
- Expanded cart interaction specification and **22 future functional scenarios** requiring visual recommendations, explicit variant choice and enhanced updates without page reload on both cart surfaces.

All new raster creative, including the product-included variants and cart references, was produced with the **built-in image_gen tool**. No generation CLI or API key was used. Earlier approved concepts were style references only; their original PNGs are not shipped as V3 deliverables. The actual company logo/product source photographs are the documented identity exceptions.

## What is complete

The design package is assembled, the selected visuals/contact sheets reviewed, and package links, mappings, dimensions, hashes and key color contrasts validated. The distributable ZIP is generated from this folder with CRC and content-hash checks. See `qa/package-validation.json` and `qa/file-inventory.json` for exact machine-readable results.

## What remains outside this package

No Shopify theme implementation, deployment, live inventory/selling-plan audit, medical-claims review, legal-policy drafting or merchant approval is represented as complete. Supporting utility pages have written specifications rather than a raster image each. The Secretropin original needs a higher-resolution authentic replacement for a large gallery. The final business input list is in DECISIONS.md.

Browser policy prevented opening the local `file:` HTML viewer; no interactive browser test is claimed. File references and original image contact sheets were reviewed independently, as recorded in `qa/catalog-review.md`.

## Portable use

Open `index.html` in a local browser and begin at README.md or BUILDER-HANDOFF.md. From an extracted package folder, run `python3 tools/validate_package.py`; inside the repository, run `python3 design/v3/tools/validate_package.py`. Rebuilding WebP exports/catalog needs Pillow; validation and ZIP creation use only Python's standard library. `tools/package_release.py` creates the versioned ZIP/checksum beside this folder and excludes Python cache files.
