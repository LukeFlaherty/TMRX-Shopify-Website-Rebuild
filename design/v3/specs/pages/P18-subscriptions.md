# P18 — Subscription information, conditional

Routes: `/pages/subscribe-and-save`
Shopify surface: page.subscribe-and-save.json
Visual references: Written layout specification; no dedicated raster mockup in 3.0.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S10 (see [source ledger](../../research/sources.md)).

## Purpose

Explain a real subscription offering only after it exists.

## Content and section order

### 1. Availability gate

When real selling plans are absent, omit this page from navigation and offer one-time shopping.

### 2. Plan explanation

If enabled, show actual delivery schedules, discounts/price and management instructions from configured provider/Shopify.

### 3. How it works

Only genuine pause/cancel/renewal behavior, with current policy links.

### 4. Shopping

Eligible products and actual plan selection; no fake calculator.

## Responsive composition

**Desktop:** Calm text-led explanation and eligible product list.

**Phone:** Single-column explanation, tap-friendly plan controls only for real plans.

## Data contract

Actual selling plans, allocation pricing, provider management URL and approved terms.

## Required states

- disabled/no plans
- plans configured
- eligible product
- ineligible variant

## Page-specific acceptance

- Do not display a fixed10% discount or synthetic plan selector.
- Navigation hides unavailable program.
- Cancel/pause promises reflect actual service.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
