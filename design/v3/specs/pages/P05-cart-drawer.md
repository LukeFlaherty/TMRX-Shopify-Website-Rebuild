# P05 — Cart drawer

Routes: `ui:cart-drawer`
Shopify surface: new V3 global section
Primary references: M13 desktop, M14 phone; M17 recommendation states, M18 empty state. M10 is historical and superseded for composition.
Product imagery: authentic current variant media from the product manifest/Shopify.
Evidence: S08, S12, S17, S18 in the [source ledger](../../research/sources.md).

## Purpose

Confirm additions, support editing and checkout, and let shoppers add relevant products while staying in the current shopping context. The drawer and full cart page share the same cart state and mutation coordinator.

## Content and section order

1. **Header:** Your bag, accurate item count and labelled Close control.
2. **Lines:** original thumbnail, linked name, real variant/options, unit/line price, quantity and Remove. Preserve line properties and selling plan where present. Use line keys for changes.
3. **Visual recommendations:** normally two eligible products. Each row includes an authentic photo, linked name, current price, actual option selector when needed and Add to bag. Never choose an unselected option silently. Recommended products must not already be in the cart and must pass current availability and merchant eligibility rules.
4. **Summary:** actual discounts/subtotal, approved shipping/tax note, Checkout, View bag and Continue shopping. No invented threshold or subscription offer.
5. **Empty state:** Your bag is empty, Shop supplements and up to two eligible visual starters with the same purchase controls. Hide checkout and the populated summary. If no eligible starters exist, retain the browse action.

## Responsive composition

**Desktop:** 440–480px panel on the right, inert dimmed backdrop and independent content scrolling. Recommendation photos remain legible at roughly 72–88px. Give rows 16–20px internal separation rather than compressing title, price and controls into one line. Summary sits outside the scrolling content only when it does not crowd the usable panel.

**Phone:** full-width sheet, `100dvh` with fallback and safe-area padding. Close is always reachable. Recommendation rows use a clear photo/details/action grouping, 16px body text and 44px V3 control targets. Scroll the content when necessary; avoid a large fixed footer that conceals recommendations or cart controls. Follow responsive spacing tokens; do not turn every row into a separate rounded card.

## No-reload behavior

Follow the shared [cart interaction specification](../cart-experience.md). Add to bag submits the exact selected variant through the locale-aware Ajax Cart API. Keep the drawer open, preserve scroll/focus, and update lines, count, discounts, totals and eligible recommendations from reconciled server state. The initiating control displays Adding, then an accessible Added confirmation. Do not navigate, reload, auto-add a second product or replay an uncertain write. Disable conflicting controls only while necessary. If HTML rendering fails after an add succeeds, recover the presentation without submitting the product again.

Recommendation states: loading, ready, choose options, adding, added/reconciled, unavailable, stock conflict, request failure, uncertain response and no eligible recommendations. Base cart states: empty, one/multiple lines, editing, removing, capped stock, update failure and checkout pending. Recommendation failure must not remove existing cart lines or block checkout.

## Page-specific acceptance

- Focus is trapped, background inert, Escape/Close work, and focus returns to the opener.
- Recommendations display actual products, images, prices and explicit option selection.
- Successful adds update this drawer, cart badge and `/cart` state without navigation or page reload.
- Quantity/removal and rejected or uncertain requests reconcile server totals; no duplicate writes.
- Removal of the last line switches to the designed empty state with working browse/eligible add actions.
- Execute [C01–C22](../../qa/cart-scenarios.md) on the actual implementation and record evidence.

## Implementation dependencies

Read [components and states](../components-and-states.md), [spacing and type](../design-system.md), [responsive rules](../responsive.md), [data contract](../data-contract.md) and [visual caveats](../../qa/visual-review.md). Written specs and current Shopify data override generated text. Use the [roadmap](../../DEVELOPMENT-ROADMAP.md), especially D050–D060 and tasks whose `page_ids` contain `P05`. No cart functionality is implemented by these design files.
