# P06 — Full cart page

Route: `/cart`
Shopify surface: new `cart.json` and V3 sections
Primary references: M15 desktop, M16 phone; M17 recommendation states, M18 empty state.
Product imagery: authentic current variant media from the product manifest/Shopify.
Evidence: S04, S08, S17, S18 in the [source ledger](../../research/sources.md).

## Purpose

A fully designed primary destination for reviewing the bag, editing items, adding relevant products and proceeding to checkout. It also supports a functional native form when JavaScript is unavailable.

## Content and section order

1. Global header and breadcrumb, Your bag with current count and Continue shopping.
2. Accessible line list with authentic photos, linked names, current options/properties, unit/line prices, quantity and Remove.
3. Order summary with actual discounts/subtotal, approved policy/tax note and real Checkout action.
4. **Complete your routine:** two to four eligible visual recommendations. Show authentic product photo, linked name, current price, actual variant selector when required and Add to bag. A single-variant product can add directly only when its purchasable variant is known. Exclude cart products, unavailable items and products lacking approved eligibility.
5. Restrained footer and approved newsletter treatment; avoid unnecessary interstitial promotions.

## Responsive composition

**Desktop:** items occupy approximately eight grid columns, summary four. Align summary with the item list; any sticky behavior stops before the footer and must not overlap controls. Recommendations sit in a dedicated section below the main cart content; two to four columns depending on available width, with no tiny packshots or cropped label artwork.

**Phone:** a standalone page with normal site navigation, not a modal; do not copy the generated M16 close X. Stack each line's photo/details, then accessible quantity/removal. Summary follows items. Recommendations use comfortable full-width rows or a single-column list when variant controls make a two-column layout cramped. Keep 16px body copy, 44px V3 controls, 24px between product entries and approximately 36–40px major section rhythm as defined in the tokens. Stack newsletter inputs/actions.

## No-reload behavior and fallback

Use the [shared cart contract](../cart-experience.md). Enhanced quantity, removal and recommendation adds keep `/cart` loaded and update the lines, badge, summary, discounts and recommendation eligibility together. Use server-rendered sections with recovery, serialize mutations and never replay an uncertain add. Preserve scroll and useful focus after a removed row or successful recommendation. A selected option must map to a current Shopify variant ID.

The native cart form remains functional for no-JS quantity/update/checkout. Recommendation controls progressively enhance a genuine purchase action or link to a PDP for unresolved options. A native fallback may navigate; the enhanced normal experience must update in place.

## Empty and failure states

No cart items: friendly empty title, Shop supplements and two to four eligible visual starters with working option/add controls. Hide populated totals and inactive checkout. No eligible recommendations: omit that section and retain a helpful browse link. Failed recommendation requests leave the main cart functional. Cart errors preserve visible items and provide an accessible recovery action; totals come from reconciled server state.

Required states include empty, one/multiple lines, discounts, quantity editing, removal, unavailable item, stock conflict, failed/uncertain write, recommendation loading/options/adding/added/error and checkout pending.

## Page-specific acceptance

- `/cart` is directly reachable, shareable and useful independently of the drawer.
- Both cart surfaces use the same server state and recommendation eligibility rules.
- Every eligible recommendation has a real image, current price and variant-aware Add to bag.
- Enhanced add/update/remove keeps the page URL and document loaded; no full-page refresh.
- Totals, discounts and badges reconcile after successful, rejected and uncertain operations.
- Full keyboard/mobile and no-JS journeys pass; execute [C01–C22](../../qa/cart-scenarios.md) and record actual evidence.

## Implementation dependencies

Read [components and states](../components-and-states.md), [data contract](../data-contract.md), [responsive rules](../responsive.md) and [visual caveats](../../qa/visual-review.md). Runtime Shopify data and written specifications override generated text. Use the [roadmap](../../DEVELOPMENT-ROADMAP.md), especially D050–D060 and tasks whose `page_ids` contain `P06`. These are design requirements, not implemented Ajax behavior.
