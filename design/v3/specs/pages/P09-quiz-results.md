# P09 — Routine quiz results

Routes: `/pages/find-your-routine?step=results`
Shopify surface: quiz state, not independent Shopify template
Visual references: Written layout specification; no dedicated raster mockup in 3.0.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S02, S06 (see [source ledger](../../research/sources.md)).

## Purpose

Present understandable individual product matches without medical personalization claims.

## Content and section order

### 1. Summary

Your routine, your next step.; plain answer summary, Edit answers and Start again.

### 2. Matches

One to three eligible available individual products with original media, real price, short transparent match reason and View product.

### 3. No match

Explain that no current products fit the chosen preferences; edit format or browse goal collection. Never relax safety/eligibility silently.

### 4. Optional follow-up

Optional generic signup after results, clearly separate from quiz answers.

## Responsive composition

**Desktop:** Answer summary above open product columns; keep reasons aligned and readable.

**Phone:** Stacked match rows with full-width product links; answer editing easy to reach.

## Data contract

Merchant-reviewed rules and actual product availability; avoid recommending excluded or unreviewed SKUs.

## Required states

- eligible results
- only sold-out matches
- no matches
- rules missing
- product fetch failure
- reset

## Page-specific acceptance

- No bundle auto-add or medical score.
- Every match has a real URL and reason based on user choices.
- Quiz answers are not silently sent to newsletter systems.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
