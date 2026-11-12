# V3 cart experience — page, drawer and visual recommendations

Revision 3.1.0 · User direction confirmed November 12, 2026. This is the implementation contract for P05/P06, not a claim that cart code is already built.

## Intended experience

The bag is available as both a drawer and a full `/cart` page. Both show actual line items, editable quantities, removal, current totals and useful visual recommendations. Each recommendation has an original product image, linked name, current price, relevant option control and an Add to bag action. Recommendations never add automatically.

On an enhanced successful add, the browser stays on the same URL. The drawer stays open if open; the cart page stays the cart page. Lines, item count, subtotal/discounts, availability and eligible recommendations refresh together. No full reload, redirect to `/cart`, popup cart or second nested drawer is part of the success path. The normal form remains a fallback when JavaScript is absent; checkout and explicit navigation are intentional document transitions.

## Layout

Desktop drawer: 440–480px, close/count header, scrolling lines and recommendation area, stable reachable checkout summary. Recommendations are two compact photo rows with text, price and action. Phone drawer: full-width sheet, 44px minimum hit areas, safe-area padding, visible close and a scrollable body. Do not let recommendation content push checkout behind browser controls.

Full cart page: a first-class destination, not merely a fallback. Desktop uses a line-item region and summary column, then an open visual recommendation row. Phone shows items, summary/checkout, then recommendation rows. The product suggestions are visually useful but secondary to completing the existing purchase. No large B-roll banner is needed. Empty cart surfaces offer starter products with images and Add to bag; no enabled zero-item checkout.

Visual references: M13 desktop drawer, M14 phone drawer, M15 desktop cart page, M16 phone cart page, M17 recommendation states, M18 empty surfaces. M10 remains historical and is superseded by the richer drawer references. Exact generated labels/prices are illustrative; real HTML uses current Shopify data.

## Recommendation candidates

Start with merchant-authored complementary-product references or a supported Shopify recommendation response seeded from a real cart product. The API is product-based, not a complete basket-personalization engine. Keep a deterministic merchant-curated fallback when that service returns nothing. [Shopify Product Recommendations API](https://shopify.dev/docs/api/ajax/reference/product-recommendations).

Default rules: remove already-in-cart products at product level, unavailable/unpublished products, invalid variants, duplicates and any merchant-excluded product. Respect market availability and reviewed merchandising eligibility. Recommendations are not medical advice or a reason to pair products with overlapping ingredients. Do not infer pairings from names. When no valid candidate exists, hide the module without leaving a blank heading.

Use at most two suggestions in the drawer and a modest two-to-four on the full page. Empty-cart starters come from a real configured collection. Use original catalog packshots, not screenshots or B-roll crops, for interactive tiles. Fetch current variant/price data and show appropriate currency. Missing data removes that candidate; never invent a price or a fallback SKU.

## Variant-aware actions

For a genuinely single eligible variant, Add to bag can add one unit directly. For multiple options, require a deliberate valid selection in an inline compact chooser or an accessible option panel that returns to the same cart. Show the selected format/flavor/size and update its price/availability. Do not silently select the first available variant just to keep quick add working. A selling plan must also be deliberately chosen if actually required; no fake subscription upgrade is added here.

States: ready, choosing options, selection invalid, adding, added, error, unavailable and removed from recommendations. During adding, disable duplicate submission for that item and announce progress without moving focus. After success, briefly confirm the added product, update the cart and retire or replace the candidate. If it becomes unavailable, preserve an explanation and refresh alternatives. Error copy is near that action, not an alert popup that closes the cart.

## Shared mutation coordinator

Use one new V3 cart client for PDP, drawer, full cart and recommendations. All writes enter a serialized queue so concurrent add/change/remove responses cannot overwrite newer state. Track a cart revision; ignore stale read/recommendation responses. Do not reuse pre-update line keys after cart changes. Closing the drawer must not imply a pending write was canceled or undone.

Use locale-aware Shopify cart endpoints for add, change and authoritative read. Add submits a real variant ID, quantity and any actual plan/properties. Changes identify the current line key. Request actual section IDs for server-rendered updates where appropriate. The final DOM and totals reflect the confirmed server cart, not arithmetic over a static design fixture. [Shopify Cart API](https://shopify.dev/docs/api/ajax/reference/cart).

No success handler calls `location.reload`, replaces the document or submits a second add form after the Ajax request. Native form submission is only the deliberate no-JS fallback. Avoid binding the same add listener again after every section replacement; delegated events or controlled component lifecycles prevent double adds.

## Partial rendering and recovery

Plan a bounded update set for line regions, summary, header badge, recommendations and announcements; resolve real section IDs at implementation. Shopify can bundle section HTML with a cart operation, but failed section rendering may return null after the mutation has already happened. Recover with a cart read and targeted re-render, never by blindly repeating the write. [Shopify bundled cart sections](https://shopify.dev/docs/api/ajax/reference/cart#bundled-section-rendering), [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering).

Preserve keyboard focus and the local scroll position when replacing markup. Reinitialize only the required controls. Recompute candidate eligibility using the confirmed cart revision. If a recommendation request fails, keep the valid cart usable and hide or retry only that module; it must not prevent checkout.

## Failures and uncertainty

Stock rejection can leave a different server quantity than expected. An invalid section request or a timeout is not proof that the write did nothing. Reconcile first. An unknown POST outcome must not trigger an automatic second add: read/reconcile, explain uncertainty if it persists and offer a controlled retry. Keep user-selected options and show the real current quantity. Do not remove other bag contents because one suggestion failed.

During an unconfirmed cart write, avoid presenting stale totals as final checkout state. Once the authoritative bag is known, checkout remains available even if the optional recommendation module fails. Rate limits and transient reads get bounded backoff; do not endlessly retry. Never show Added before confirmation.

## Accessibility and progressive enhancement

Drawer focus trapping, background inertness, Escape and focus return remain required. Product action labels identify the specific product. Status/error messages use a useful live region without repeatedly announcing every entire cart line. Inline option controls have persistent labels. When an added tile disappears, move focus predictably to a confirmation/next useful control rather than to the document body. Without JavaScript, normal product/cart forms and product links still allow shopping; fallback navigation is not presented as the enhanced no-reload behavior.

## Evidence required to complete cart tasks

Record actual server cart state before/after, selected variant, request outcome, displayed count/subtotal and the network document-navigation trace. Test page and drawer, phone and desktop, empty-to-populated, quantity edits, removals, rapid clicks, stock conflicts, failed section HTML, unavailable recommendations and uncertain writes. Screenshots prove appearance only. See [the cart scenario matrix](../qa/cart-scenarios.md) and roadmap R05.
