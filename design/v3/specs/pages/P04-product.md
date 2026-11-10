# P04 — Product detail and product-format variants

Routes: `/products/:handle`
Shopify surface: product.json
Visual references: M05, M06
Page-owned photography: A09, A10
Evidence: S03, S06, S08, S10 (see [source ledger](../../research/sources.md)).

## Purpose

Make it clear what the product is, which option is selected and how to purchase it confidently.

## Content and section order

### 1. Gallery and purchase

Authentic media gallery, title, current money-formatted price, short approved introduction, actual option selectors, quantity, Add to bag, availability. A09 is Essential Aminos-only staging; other products use their own original media until dedicated imagery exists.

### 2. Product information

Accordions Overview/Label/Shipping. Label opens actual current media. No synthetic facts table.

### 3. Routine editorial

Essential Aminos uses A10; short neutral routine copy and three open principles. Other product families omit this imagery unless their own fresh asset is commissioned.

### 4. Usage and questions

Approved directions/warnings from the current label. Generic layout steps are not a dose instruction. FAQs reflect the actual product. Capsule/softgel, powder, lozenge and spray formats must not inherit one another's directions.

### 5. Related products

Real related items, exclude current product, correct prices and availability. One small quiz CTA, signup/footer.

## Responsive composition

**Desktop:** 55/45 gallery/purchase split; buying controls within first meaningful viewport; lower editorial split. Current price is mandatory despite older concepts.

**Phone:** Gallery then title/price then selectors, quantity and full-width action. All lower editorial splits stack; label information full-width; FAQ rows at least 52px. Never fit text beside a tiny label image.

## Data contract

Real selected variant/ID/options/availability/price; approved label/directions/warnings; authentic product media group; actual review and selling-plan data only.

## Required states

- available variant
- alternate variant
- invalid combination
- sold out
- quantity invalid
- adding
- add success
- stock conflict
- network failure
- label missing
- no reviews
- no selling plans

## Page-specific acceptance

- Add succeeds using the selected real variant and accurate quantity; server cart is reconciled.
- A product without review data renders no stars/counts.
- No mockup nutrition table, option name or related-item price is used as source.
- Powder/capsule/softgel/spray/lozenge variants render their own information.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).
