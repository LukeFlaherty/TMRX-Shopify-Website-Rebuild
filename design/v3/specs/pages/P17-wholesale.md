# P17 — Practitioner and wholesale inquiry

Routes: `/pages/wholesale`
Shopify surface: page.wholesale.json
Visual references: Written layout specification; no dedicated raster mockup in revision 3.1.0.
Page-owned photography: None; use authentic product media or intentional text-first layout as specified.
Evidence: S01, S04 (see [source ledger](../../research/sources.md)).

## Purpose

Provide a professional inquiry path without promising automatic eligibility or pricing.

## Content and section order

### 1. Intro

For practitioners and professional partners; concise approved statement, inquiry CTA.

### 2. Process

Three plain steps Submit an inquiry/Team review/Receive next steps; only if merchant approves actual workflow.

### 3. Inquiry form

Name, work email, business name, role, country, message; optional credentials submitted securely only if actually needed.

### 4. Status

Actual success/error confirmation, no automatic pricing unlock or acceptance.

## Responsive composition

**Desktop:** Text/process left, form right; no generic doctor photograph.

**Phone:** Intro/process then full-width form, clear field spacing and privacy link.

## Data contract

Merchant wholesale criteria, actual form endpoint and privacy terms.

## Required states

- blank
- validation
- sending
- sent
- failed
- existing partner link if real

## Page-specific acceptance

- No new discounts, MOQ or approval timing invented.
- No unconfigured upload/CRM action shown as working.
- Generated lifestyle subjects are not used as practitioner endorsements.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P17`. This brief specifies design; task status and implementation evidence live in the tracker.
