# P11 — Editorial article

Routes: `/blogs/news/:article`
Shopify surface: article.json
Visual references: M09
Page-owned photography: A13
Evidence: S04, S11 (see [source ledger](../../research/sources.md)).

## Purpose

Provide a comfortable reading experience with clear sources and useful related links.

## Content and section order

### 1. Article header

Category, actual H1, deck, byline/date when provided, share links and A13 hero for the example whole-foods article.

### 2. Reading body

60–70 character measure, meaningful headings, contents links and actual approved article text. No clinical authority inferred from image.

### 3. Contextual product

Optional actual related product with real price and View product; never interrupt every paragraph with a sale.

### 4. Next reading

Related article links excluding current article; signup/footer.

## Responsive composition

**Desktop:** Contents sidebar plus narrow reading column; media may extend beyond text measure.

**Phone:** Contents disclosure above body; comfortable16px/1.5 copy, full-width meaningful images, product spotlight stacked.

## Data contract

Native article content and metadata; references for substantive health claims must be separately reviewed.

## Required states

- long/short article
- no image
- no author
- no related product
- anchored section
- unpublished/not found

## Page-specific acceptance

- Headings and contents IDs agree; sticky header does not cover target heading.
- Do not publish the mockup's generated prose as researched medical content.
- A13 belongs to this example article only; new articles need distinct art or text-first layout.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Preferred product-included photography — revision 3.1

Use these finished product-filled variants by default. Original plates remain alternate source material. Products are already present: do not overlay a second packshot. Verify visible packaging against current authentic source media before launch.

| Preferred asset | Original slot/source | Product identity |
|---|---|---|
| A23 | A13 | bone-broth-protein |

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P11`. This brief specifies design; task status and implementation evidence live in the tracker.
