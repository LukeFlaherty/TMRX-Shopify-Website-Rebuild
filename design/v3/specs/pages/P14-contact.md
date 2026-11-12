# P14 — Contact and support

Routes: `/pages/contact-us`
Shopify surface: page.contact-us.json
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S04, S11 (see [source ledger](../../research/sources.md)).

## Purpose

Let shoppers contact the actual support team and find routine order help.

## Content and section order

### 1. Page header

How can we help?; short description and verified contact channels only.

### 2. Form

Name, email, optional order number, topic and message with persistent labels; actual Shopify contact form or configured handler.

### 3. Useful links

Shipping/returns, product information and FAQs, with no duplicated hero photography.

### 4. Confirmation

Honest sent/error state after real response; no invented reply-time commitment.

## Responsive composition

**Desktop:** Form 7 columns, concise support links 5 columns; restrained spacing.

**Phone:** Single-column form, full-width submit, help links below. Keep input16px to avoid phone zoom.

## Data contract

Verified support details, real contact handler, merchant privacy wording.

## Required states

- blank
- validation
- submitting
- success
- server error

## Page-specific acceptance

- Required fields clear; invalid email identified without clearing message.
- No sensitive diagnosis/medication information requested.
- No fake telephone/address or promised response window.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P14`. This brief specifies design; task status and implementation evidence live in the tracker.
