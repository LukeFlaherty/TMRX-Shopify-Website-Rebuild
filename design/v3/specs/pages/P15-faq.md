# P15 — Frequently asked questions

Routes: `/pages/faq`
Shopify surface: page.v3-faq.json (proposed)
Visual references: Written layout specification; no dedicated raster mockup in 3.0.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S11, S12 (see [source ledger](../../research/sources.md)).

## Purpose

Answer common shopping questions while routing product-specific matters appropriately.

## Content and section order

### 1. Title and topics

Frequently asked questions; Orders/Products/Shipping & returns topic links.

### 2. Question groups

Approved Q&A accordions. Product questions link to their actual label/PDP; do not generalize safe-use answers across SKUs.

### 3. Need help

Contact link with short neutral invitation, no medical consultation promise.

## Responsive composition

**Desktop:** Topic rail and readable full-width question groups, max text measure.

**Phone:** Wrapped topic links and spacious52px+ question rows, no compressed tiny accordion list.

## Data contract

Merchant-approved answers and current policy links.

## Required states

- all closed
- one/multiple open
- deep link to question
- no approved answers

## Page-specific acceptance

- Expanded state is semantic and keyboard operable.
- No questions invent return terms, delivery windows or supplement doses.
- Rows with long questions expand naturally without overlap.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
