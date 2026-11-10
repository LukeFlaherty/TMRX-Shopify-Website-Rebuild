# P19 — Canonical policies and accessibility information

Routes: `/policies/:handle`, `/pages/accessibility`
Shopify surface: platform policy surface / page.v3-document.json
Visual references: Written layout specification; no dedicated raster mockup in 3.0.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S04, S11 (see [source ledger](../../research/sources.md)).

## Purpose

Keep official documents readable and clearly identified.

## Content and section order

### 1. Document header

Actual policy title and effective date if supplied.

### 2. Document body

Approved policy text; headings, lists and links preserve meaning.

### 3. Navigation

Return to support; policy cross-links and verified contact.

## Responsive composition

**Desktop:** Max720px reading measure with ordinary site shell when supported.

**Phone:** 20px gutters, natural wrapping, accessible long links and no horizontal overflow.

## Data contract

Current Shopify policy content and merchant-approved accessibility statement.

## Required states

- published policy
- long document
- missing/unpublished policy

## Page-specific acceptance

- Do not replace legal content with design placeholder copy.
- Do not promise legal or accessibility certification from this package.
- Platform-owned policy behavior is verified during build.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
