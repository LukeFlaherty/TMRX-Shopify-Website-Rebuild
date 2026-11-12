# P12 — About True Matrx

Routes: `/pages/about`
Shopify surface: page.v3-about.json (proposed)
Visual references: M12
Page-owned photography: A14
Evidence: S01 (see [source ledger](../../research/sources.md)).

## Purpose

Explain the brand in an approachable, factual way.

## Content and section order

### 1. Introduction

A higher standard for your daily routine.; concise purpose statement and A14 everyday movement image.

### 2. Principles

Purpose/Clarity/Consistency, expressed as practical brand intentions not verified clinical outcomes.

### 3. Information

Links to product information/standards and the journal.

### 4. Next action

Shop supplements; signup/footer. No fabricated founder story, clinic or doctor endorsement.

## Responsive composition

**Desktop:** Hero text/photo split, principles in open columns, restrained editorial text.

**Phone:** Photo below introduction, principles as stacked icon/text rows with comfortable spacing.

## Data contract

Merchant-approved company story; any team biography requires current credentials and permission.

## Required states

- normal
- no verified team content
- optional approved profile future

## Page-specific acceptance

- No generated lifestyle person is labeled as staff, doctor or customer.
- No invented founding date, manufacturing certification or clinical proof.
- A14 is not reused as home goal imagery.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P12`. This brief specifies design; task status and implementation evidence live in the tracker.
