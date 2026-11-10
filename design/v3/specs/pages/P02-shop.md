# P02 — Shop all

Routes: `/collections/all`
Shopify surface: collection.json
Visual references: M03, M04
Page-owned photography: A08
Evidence: S02, S05, S07, S14 (see [source ledger](../../research/sources.md)).

## Purpose

Help visitors compare the full catalog and narrow it without losing context.

## Content and section order

### 1. Masthead

Short H1 Find your daily essentials.; compact A08 background, optional authentic product layers. Do not use a homepage-size promotional banner.

### 2. Category navigation

All supplements/Protein/Recovery/Wellness links to configured collections. Current category identified. Categories and active filters are distinct.

### 3. Filter and results

Real filters Goal/Format/Availability only when configured; applied-filter summary; clear-all; result count; sort. Main 3-column desktop/2-column phone product grid includes price and availability.

### 4. Below results

One optional routine-discovery CTA then newsletter/footer. Avoid a second identical quiz tile in the grid if the banner exists.

## Responsive composition

**Desktop:** 220–240px sidebar plus 3-column grid. Product images share intrinsic regions but retain real proportions. Sort above grid.

**Phone:** Category rail, Filter/Sort controls, closed filter sheet, 2-column grid. Product row gap 28px. No permanent checkbox sidebar.

## Data contract

Actual collection.products, filters, sort options and pagination; native platform URLs; real variant availability and prices.

## Required states

- default
- filtered
- sorted
- paginated
- zero results
- loading
- failed refresh
- sold-out item
- missing product image

## Page-specific acceptance

- Applied selections are visible/removable and survive return from a PDP.
- Zero results preserves filters and offers Clear filters.
- No fabricated collagen/magnesium SKU is added because it appeared in a generated image.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
