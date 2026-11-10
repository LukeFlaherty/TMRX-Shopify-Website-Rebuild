# P16 — Shipping and returns information

Routes: `/pages/shipping-returns`
Shopify surface: page.v3-policy-guide.json (proposed)
Visual references: Written layout specification; no dedicated raster mockup in 3.0.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S01 (see [source ledger](../../research/sources.md)).

## Purpose

Present current merchant policy clearly without making new commercial promises.

## Content and section order

### 1. Summary

Shipping & returns title; concise approved summary.

### 2. Shipping

Actual destinations, methods, charges and thresholds from current approved policy; no assumed $50 threshold.

### 3. Returns

Approved process, eligibility and contact steps; links to canonical Shopify policies.

### 4. Help

Support action; policy last-updated date only when actual.

## Responsive composition

**Desktop:** Simple readable content column, optional anchor sidebar; no decorative photo.

**Phone:** One-column document with clear subheads and44px policy/support links.

## Data contract

Current shipping/refund policies and operational approval.

## Required states

- approved policy present
- policy not yet supplied
- external canonical policy

## Page-specific acceptance

- No old generic exchange copy is silently carried forward.
- Policy link and summary agree.
- This brief supplies layout, not invented legal/policy text.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
