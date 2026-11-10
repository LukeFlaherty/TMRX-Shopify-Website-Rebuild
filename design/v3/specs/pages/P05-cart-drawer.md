# P05 — Cart drawer

Routes: `ui:cart-drawer`
Shopify surface: new V3 global section
Visual references: M10
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S08, S12 (see [source ledger](../../research/sources.md)).

## Purpose

Confirm cart contents and make editing or checkout straightforward.

## Content and section order

### 1. Drawer header

Your bag, accurate item count and clear Close action.

### 2. Line list

Original thumbnail, linked product name, actual variant/options, unit/line price, quantity and Remove. Shipping/taxes note sourced appropriately; no fabricated upgrade offer.

### 3. Summary

Real discounts/subtotal; Checkout primary; View bag and Continue shopping secondary. Optional single relevant recommendation only with actual data.

### 4. Empty state

Your bag is empty.; Shop supplements plus real category text links, no reused decorative photo.

## Responsive composition

**Desktop:** 440–480px right panel; dimmed inert backdrop. List scrolls independently and summary remains reachable.

**Phone:** Full-width sheet with safe-area padding. Close target at top; checkout not hidden by keyboard or browser controls.

## Data contract

Current Shopify cart, line keys, item counts, discounted totals, money/currency and current variant media.

## Required states

- empty
- populated
- editing
- removing
- stock conflict
- network failure
- checkout pending

## Page-specific acceptance

- Keyboard focus is trapped and restored; close/Escape work.
- Totals reconcile after rejected or capped quantity requests.
- No duplicate add or auto-added cross-sell; no invented free-shipping threshold.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
