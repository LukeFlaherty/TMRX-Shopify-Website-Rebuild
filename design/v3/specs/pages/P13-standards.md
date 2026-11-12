# P13 — Product information and standards

Routes: `/pages/our-standards`
Shopify surface: page.v3-standards.json (proposed)
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S01, S03 (see [source ledger](../../research/sources.md)).

## Purpose

Explain how shoppers can inspect product information without unsubstantiated quality promises.

## Content and section order

### 1. Headline

Clear information for your routine.; text-first editorial header, no borrowed laboratory photo.

### 2. Label guidance

Where to find product label, ingredients, directions and warnings; link real product media.

### 3. Practitioner context

Only merchant-approved wording. Do not imply every product is clinically tested, certified or recommended.

### 4. Help

Contact support and browse products. Any actual test/report is linked to a verified document.

## Responsive composition

**Desktop:** Narrow text introduction plus three plain process columns and document links.

**Phone:** Single column, linked document rows at least44px targets; no miniature charts.

## Data contract

Verified labels/reports, approved brand standards text and support destination.

## Required states

- documents available
- document absent
- external report link

## Page-specific acceptance

- Every certification/report claim has a real supporting document.
- Missing evidence is omitted, not replaced with an invented badge.
- No empty decorative panel is added to compensate for text-only design.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P13`. This brief specifies design; task status and implementation evidence live in the tracker.
