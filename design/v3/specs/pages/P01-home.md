# P01 — Homepage

Routes: `/`
Shopify surface: index.json
Visual references: M01, M02
Page-owned photography: A01, A02, A03, A04, A05, A06, A07
Evidence: S01, S02, S12, S15 (see [source ledger](../../research/sources.md)).

## Purpose

Introduce True Matrx and make the first useful shopping decision easy.

## Content and section order

### 1. Hero

Eyebrow Practitioner-grade nutrition; H1 Hold your supplements to a higher standard.; body Purpose-built support for your daily routine.; Shop supplements primary; Find my routine secondary. A01 desktop/A02 phone with authentic product layers. Avoid hard-coded prices in hero.

### 2. Daily essentials

Merchant-curated product group, underlined category switcher Bestsellers/Protein/Strength & recovery/Wellness. If sales ranking is unverified, label first group Featured. Real product title, current price and View options. No rating fallback.

### 3. Shop by goal

Four distinct photo links: daily nutrition A03, strength A04, recovery A05, foundational wellness A06. Each link reaches a real collection or configured filter. Phone rows, not four miniature tiles.

### 4. Standards

A07 plus A higher standard. An everyday routine.; three concise content principles. No certification or lab-performance badge unless substantiated. Phone image then heading and icon rows.

### 5. Routine and journal

One quiz CTA; native blog previews as text-first entries if their own unique imagery is absent; signup and white footer. Do not duplicate the quiz several times.

## Responsive composition

**Desktop:** Hero split with image right; 3–4 open product items; four goal links; standards split; a compact journal row.

**Phone:** Copy/actions above stone photo. Product rail shows one whole item and next peek with controls. Goal rows; standards image above text. Newsletter stacked, footer accordions.

## Data contract

Selected product/collection/article references; current variant media/prices; goal-link mapping; merchant announcement; newsletter handler.

## Required states

- curated group loaded
- switching/loading
- empty group
- group request failure
- no published articles
- newsletter success/error

## Page-specific acceptance

- Category switcher changes content and works by keyboard; collection links remain usable without JS.
- Every goal has its own mapped photograph and valid destination.
- Middle/lower sections retain 16px heading gaps and 36–40px section rhythm at 390px.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
