# P22 — Checkout and order confirmation handoff

Routes: `platform:checkout`, `platform:order-confirmation`
Shopify surface: Shopify hosted surfaces; not a theme template
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S08 (see [source ledger](../../research/sources.md)).

## Purpose

Maintain a coherent purchase handoff within actual Shopify capabilities.

## Content and section order

### 1. Entry

Cart's real checkout action submits the current cart, not a fake checkout page.

### 2. Brand settings

Apply logo/colors only through supported current shop configuration and entitlements.

### 3. Confirmation

Platform-confirmed order details; no invented order-success screen within theme.

## Responsive composition

**Desktop:** Verify native checkout with actual cart and market; preserve readability.

**Phone:** Verify keyboard/address/payment layouts and return path on real phone viewport.

## Data contract

Actual checkout/cart/account configuration; real order state.

## Required states

- cart handoff
- shipping/payment validation
- payment failure
- confirmed order

## Page-specific acceptance

- No Liquid checkout template or unsupported customization promised.
- No order success before platform confirmation.
- Functional validation uses appropriate test mode, not a real charge by default.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P22`. This brief specifies design; task status and implementation evidence live in the tracker.
