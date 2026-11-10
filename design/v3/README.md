# True Matrx — V3 redesign package

Version **3.0.0**, prepared **November 10, 2026**. This is a design and research handoff, not a deployed theme. The accepted direction is homepage A: white, subtle ice blue, authentic True Matrx packaging, natural stone staging, clear blue actions, and a relaxed but efficient page rhythm.

## Start here

1. Open [the visual asset catalog](index.html) to browse the delivered images locally.
2. Read [the builder handoff](BUILDER-HANDOFF.md) and [design system](specs/design-system.md).
3. Find the requested route in [the page index](PAGE-INDEX.md) or [machine-readable page registry](manifests/pages.json).
4. Follow its individual page brief. Resolve image IDs in [the asset manifest](manifests/assets.json); resolve product media in [the product source manifest](manifests/products.json).
5. Read the relevant interaction rules in [components and states](specs/components-and-states.md), then the [data contract](specs/data-contract.md).
6. Use [the implementation acceptance checklist](qa/implementation-checklist.md). The package validator checks the handoff itself; it does not test a Shopify implementation.

## What is authoritative

User direction → written page brief and design tokens → current Shopify product/variant data → verified original product media → fresh page-specific photography → generated page mockup. Mockups communicate art direction and hierarchy. Generated labels, body copy, prices, product counts, thumbnails, dates, and interaction depictions are never a data source. See the explicit [visual review notes](qa/visual-review.md).

## Fresh-work policy

V3 photography, mockups, design specifications, copy direction, token files, and page registry are new work. No earlier generated campaign graphic, desktop/mobile concept PNG, old theme section, or existing theme CSS is shipped as a V3 creative deliverable. Earlier approved concepts were used as style references only.

Two identity exceptions are intentional: the authentic company logo and original product/label photographs are preserved and copied into this self-contained package. Recreating those would change the actual brand or product. They are marked `authentic-source-exception` in the manifest, not represented as newly photographed. Repeated catalog packshots and a consistent global header/footer are appropriate; page-specific editorial photography must not be recycled across unrelated pages. New V3 components may share a new implementation; do not copy the legacy theme's sections or fabricated data fallbacks.

## Scope and status

The page registry covers shopping, discovery, editorial, brand/support pages, commerce states, and platform handoffs. Core pages have fresh generated visual references; supporting pages have written desktop/mobile specifications. A missing screenshot is explicitly marked, not disguised as completed visual design. The core desktop/mobile views are composition references; exact dimensions and spacing are in tokens and briefs.

The package includes researched product identity and a dated public price snapshot. It does not have authenticated Shopify inventory, selling plans, customer account configuration, legal policy approval, or a merchant-approved quiz eligibility model. Those are recorded in [the decision register](DECISIONS.md). They do not prevent building the visual structure and safe fallbacks.

## Folder guide

| Folder | Contents | Builder use |
|---|---|---|
| `assets/generated/` | New text-free photographic masters and WebP derivatives | Dedicated page slots; see ownership in manifest |
| `assets/brand/` | Authentic logo source | Header/footer at native proportions |
| `assets/products/` | Original catalog/label source images | Verify variant and label before binding |
| `mockups/desktop/`, `mockups/mobile/` | Newly generated page compositions | Visual reference only; never ship as a webpage image |
| `specs/pages/` | Individual page plans and state requirements | Main implementation brief for a route |
| `specs/` | Tokens, components, responsive rules, data contract | Shared V3 standards |
| `research/` | Source ledger, findings, catalog snapshot | Evidence and observed limitations |
| `manifests/` | IDs, route mapping, file provenance, dimensions/hashes | Programmatic lookup and integrity checks |
| `prompts/` | Exact image-generation prompts | Reproducibility and future targeted revisions |
| `qa/` | Package validation, visual caveats, future build checks | Separate design readiness from launch readiness |
| `tools/` | Package inventory, catalog and integrity tooling | Maintenance of this package only |

Read [CHANGELOG](CHANGELOG.md) when continuing work. Validate with `python3 design/v3/tools/validate_package.py` from the repository root. For rebuilding previews/derivatives, use Python with Pillow as described in [the asset production guide](specs/asset-production.md). No API key is required to inspect this package.
