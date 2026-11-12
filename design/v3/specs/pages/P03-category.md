# P03 — Product categories and goals

Routes: `/collections/:handle`
Shopify surface: collection.v3.json (proposed)
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S02, S05, S07 (see [source ledger](../../research/sources.md)).

## Purpose

Create focused category pages without inventing a separate site design for every goal.

## Content and section order

### 1. Category introduction

Actual collection title plus a short approved description. Typographic masthead by default; no recycling homepage goal photography as a full category hero.

### 2. Related categories

A small relevant set of collection links, not a second global navigation.

### 3. Catalog

Same new V3 open item/filter pattern as P02 with the current collection scope. Show useful format/size information and real prices.

### 4. Education

Optional original category FAQ and a relevant published article link; omit when source content is missing.

## Responsive composition

**Desktop:** Short introduction, filter sidebar, 3 columns. No giant invented hero.

**Phone:** Short title, category rail if useful, Filter/Sort sheet and 2 columns. Collapsed long description after first paragraph.

## Data contract

Actual collection handle/title/description; configured goal/format fields; collection image optional and requires a new page-specific asset.

## Required states

- protein category
- strength/recovery category
- wellness category
- empty collection
- unconfigured filter
- zero matches

## Page-specific acceptance

- Every navigation destination resolves to a real collection.
- Category does not add products by name-substring heuristics.
- No image is required merely to fill space; text-only masthead is designed.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P03`. This brief specifies design; task status and implementation evidence live in the tracker.
