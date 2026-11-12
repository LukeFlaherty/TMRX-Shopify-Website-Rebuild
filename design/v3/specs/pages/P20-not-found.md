# P20 — 404 and missing content

Routes: `system:404`
Shopify surface: 404.json (new)
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S04, S09 (see [source ledger](../../research/sources.md)).

## Purpose

Help a visitor recover from a missing URL.

## Content and section order

### 1. Message

We couldn't find that page.; concise explanation without blaming user.

### 2. Recovery

Search field, Shop all and Home links; relevant real categories optional.

### 3. Footer

Normal shell and footer; no oversized reused hero.

## Responsive composition

**Desktop:** Compact centered text/form in a deliberately short page.

**Phone:** Single-column message, search and full-width primary link.

## Data contract

Actual destination URLs and search action.

## Required states

- invalid route
- removed product
- unpublished article

## Page-specific acceptance

- 404 response/status remains correct.
- Search is usable, not a decorative input.
- No auto-redirect that masks broken links.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P20`. This brief specifies design; task status and implementation evidence live in the tracker.
