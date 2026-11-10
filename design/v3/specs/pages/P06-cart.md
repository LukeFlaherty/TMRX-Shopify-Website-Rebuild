# P06 — Cart page fallback

Routes: `/cart`
Shopify surface: cart.json (new)
Visual references: Written layout specification; no dedicated raster mockup in 3.0.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S04, S08 (see [source ledger](../../research/sources.md)).

## Purpose

Provide a complete bag page that works even if the drawer enhancement is unavailable.

## Content and section order

### 1. Page header

Your bag and Continue shopping link.

### 2. Items

Accessible line-item list with quantities, removal, variant detail and current totals.

### 3. Summary

Subtotal, true discount details, policy/tax note and real checkout submit.

### 4. Empty and recovery

Empty message plus Shop all. Failed updates preserve items and offer retry; no blank page.

## Responsive composition

**Desktop:** Items take 8 grid columns, summary 4. Form actions clear and aligned.

**Phone:** Each line stacks image/details/quantity; summary follows list; full-width Checkout.

## Data contract

Native cart form and cart data; no mock sample totals in implementation.

## Required states

- empty
- one line
- multiple lines
- update failure
- unavailable item
- discounted cart

## Page-specific acceptance

- Works as the no-drawer/no-optional-JS fallback.
- Quantity zero/removal and checkout have expected native behavior.
- Sidebar never covers item controls on small screens.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
