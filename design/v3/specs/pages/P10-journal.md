# P10 — Optimization Journal index

Routes: `/blogs/news`, `/blogs/news/tagged/:tag`
Shopify surface: blog.json
Visual references: M08
Page-owned photography: A12
Evidence: S04, S09 (see [source ledger](../../research/sources.md)).

## Purpose

Make educational content easy to browse and connect it to product understanding.

## Content and section order

### 1. Masthead

The Optimization Journal; Practical guidance for your daily routine.; article search and topic navigation.

### 2. Featured article

A12 image; actual title, excerpt and Read the guide link. The index image is distinct from the article hero.

### 3. Latest articles

Two/three-column desktop text-first editorial entries; phone rows. Actual categories/date/author only if supplied. No repeated stock thumbnails.

### 4. Next step

One optional Find my routine product-discovery CTA; signup/footer. It is not an article recommendation quiz.

## Responsive composition

**Desktop:** Featured image/text split, latest text-first grid with fine rules.

**Phone:** Title, field/topic rail, stacked feature and readable article rows; optional Load more with URL fallback.

## Data contract

Native blog/article objects and approved excerpts. New thumbnail per article or designed text-first fallback.

## Required states

- published articles
- topic selected
- search
- empty blog
- missing image
- pagination

## Page-specific acceptance

- Topic selection and pagination change actual content.
- Quiz CTA remains product discovery despite any generated-image wording.
- No author credentials/date is synthesized.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
