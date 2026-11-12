# P21 — Customer account handoff

Routes: `/account`, `/account/login`
Shopify surface: Shopify account surface, configuration-dependent
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S04 (see [source ledger](../../research/sources.md)).

## Purpose

Send customers to the configured account experience without a false custom-login promise.

## Content and section order

### 1. Storefront entry

Accessible Account action in desktop header/mobile menu.

### 2. Native experience

Use actual Shopify account routes. Inspect classic/new mode before any styling work.

### 3. Return journey

Preserve useful shopping context where supported. Order/history links must be actual platform destinations.

## Responsive composition

**Desktop:** Shell action and brand consistency where platform permits; no bespoke auth screen assumed.

**Phone:** Account in menu if header lacks space; platform pages tested on phone.

## Data contract

Shop account mode and official routes; no credentials handled by theme custom code.

## Required states

- signed out
- signed in
- login failure handled by platform
- return to shop

## Page-specific acceptance

- No custom authentication built merely to match an image.
- Current account flow inspected in actual shop.
- No unsupported order/account access promised.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P21`. This brief specifies design; task status and implementation evidence live in the tracker.
