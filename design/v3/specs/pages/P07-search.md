# P07 — Search and predictive suggestions

Routes: `/search`, `ui:predictive-search`
Shopify surface: search.json
Visual references: M11
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S09, S12 (see [source ledger](../../research/sources.md)).

## Purpose

Let visitors find real products and useful content quickly.

## Content and section order

### 1. Search form

Search True Matrx; persistent query field, submit and clear. No decorative hero.

### 2. Suggestions

Optional supported predictive product/article/collection suggestions. Clear grouping and keyboard navigation; View all results.

### 3. Result page

Product/article resource controls, actual count, relevant filtering/sorting and open result items.

### 4. No results

Echo escaped query, edit field, clear and actual category links. Do not invent a product match.

## Responsive composition

**Desktop:** Prominent field, concise result grouping and 3-column product grid. Article results are text-first if images absent.

**Phone:** Full-width field, readable suggestion list and 2-column products. Keyboard does not obscure close/submit.

## Data contract

Shopify search/predictive APIs and actual resource URLs; HTML escape query text.

## Required states

- empty query
- typing
- loading
- suggestions
- results
- no results
- request failure
- stale request

## Page-specific acceptance

- Typing stale responses cannot replace newer results.
- Submit works without predictive enhancement.
- No-result screen retains query and provides useful recovery.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
