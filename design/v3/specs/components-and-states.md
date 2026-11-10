# Components and state contracts

These are new V3 component requirements. Existing theme code is audit context only. Page-specific composition comes from the page brief; shared interactions follow this document.

## C01 Global shell and navigation

Desktop header height 76px plus optional 28px announcement; phone header 64px plus optional 28px announcement. Announcement is one merchant-authored message, not a rotating promotion. Logo retains its 500:115 aspect ratio and enough room for adjacent 44px controls. Menu items are actual destinations, with submenus as progressive disclosure rather than hover-only targets. Current destination has a visible state.

Mobile menu states: closed; opening; open; submenu expanded; closing. Only one modal overlay is active. Open moves focus to close/menu heading; Escape, close button or explicit backdrop interaction closes; focus returns to opener. Focus cannot escape to obscured content. Menu links remain functional without optional animation. Account is accessible from the menu if removed from the narrow header. Never hide search just to preserve a decorative logo size.

## C02 Category switcher

An in-place product group switcher uses buttons with tab semantics and associated panels; navigating to a new collection uses links with current-page semantics. Do not mix the two models. Selected state combines blue text, a 2px underline, and programmatic selection. Arrow keys work for a true tablist. Scroll selected tab into view without scrolling the page unexpectedly. Phone rail has visible next-content cue and usable previous/next controls when needed; selection does not require dragging.

States: selected; hover/focus; loading; empty group; fetch failed. During failure, preserve the current group, show a retry or collection link. Without JS, collection links provide the products. Stable region height reduces jumping, but do not clip content or fix a height based on the shortest panel.

## C03 Open product item

An intrinsic-ratio image region, category/format if useful, linked name, current money-formatted price, optional genuine compare-at price, availability and one action. Images use contain, not cover. No surrounding rounded rectangle. Item links have distinct accessible names; action text is not the only navigable target. Two-column phone text wraps without fixed-height clipping.

Default: View options. Quick add is optional only for a real unambiguous available variant. Sold out: show text and product link, no enabled add action. Missing image: neutral illustration-free space with product name, not another SKU's photo. Missing price: hide purchase action and explain unavailable product information; never display $0. A no-review product has no stars or fabricated count.

## C04 Filter, sort and result state

Desktop sidebar uses actual configured Shopify filters; mobile uses a full-height dialog. Filters have labels and counts from the real response. Display applied filters above results with individual remove and clear-all actions. Use Shopify-generated filter URLs and preserve sort/query across updates; custom goal/category fields require real configured metafields/collections.

Mobile selection stays draft until Apply; Cancel restores prior filters. Opening focuses dialog heading/first control; Apply announces updated result count and restores focus meaningfully. Zero results retains all active filters and offers Clear filters. Network error retains prior items and a retry. Sort updates the real result ordering, not only the dropdown label. See [Shopify filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering).

## C05 Gallery and label viewer

Maintain original product media order and aspect ratio. Thumbnail buttons include position/description and selected state. Next/previous buttons supplement swiping. Zoom is an accessible dialog with close and focus return. Label assets open at readable resolution. A generated Supplement Facts table is prohibited. If no current approved label exists, use an honest unavailable state and suppress that label view.

States: first image; alternate image; zoom; loading; unsupported media; missing label. Do not lazy-load the primary product image. Lower media can lazy-load. Non-photo media has an equivalent accessible title and controls.

## C06 Product purchase form

Use an actual Shopify product form and selected variant ID. Title, current price, compare-at price, option names/values, availability and selling-plan allocations come from the selected variant, not a hand-maintained V3 file. Changes update gallery/price/URL when appropriate. Quantity minimum/increments follow actual rules. Submit button labels: Add to bag; Adding…; Added; Sold out; Unavailable. Reserve enough width to avoid layout jumps.

States: valid default; valid alternate variant; nonexistent combination; sold out; quantity invalid; adding; success; stock conflict; network failure; selling plan unavailable. Announce success/errors through a live status region. Disable duplicate submissions while pending. On error preserve the selection and entered quantity where valid; do not empty the form. Real subscription controls are conditional on actual selling plans and allocation pricing. [Shopify product template](https://shopify.dev/docs/storefronts/themes/architecture/templates/product/overview), [subscriptions](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions).

## C07 Cart drawer and cart page

Right-side desktop panel 440–480px; phone full-width sheet. Header has count and close. Each line uses Shopify line key, exact variant/options, image, price, quantity and remove. Item count, line totals, discounts and subtotal reconcile with cart response. Checkout action stays reachable, with its footer outside the scrollable line list when space allows. Cart page is a complete fallback, not a dead link.

States: empty; one/multiple lines; editing quantity; removing; item became unavailable; quantity capped by stock; successful change; failed update; checkout pending. A stock rejection can still leave a changed server cart, so refresh/reconcile before showing totals. Preserve current items and show a retry for failure. Remove is an explicit action, not a tiny unlabelled icon. No auto-added recommendations. Free-shipping progress is hidden until the threshold and applicable market are verified; no fake countdown or subscription upgrade. [Shopify Cart API](https://shopify.dev/docs/api/ajax/reference/cart).

## C08 Search

Search entry is a form with labeled field and real submit. Predictive suggestions can group products, collections and articles using supported platform results. Debounce requests, cancel/ignore stale responses and retain typed query. Keyboard navigation and Escape behavior must be explicit; a submit fallback always reaches `/search`.

States: closed; empty query; typing; loading; results; no match; error. A no-match screen includes the query, editable field, clear action and real category links; it does not invent matching products. Search result pages preserve query/filter/sort in URL and separate resource types. [Predictive Search API](https://shopify.dev/docs/api/ajax/reference/predictive-search).

## C09 Quiz

Three steps: broad goal, preferred format, routine context. Native radio groups/fieldset legends; a visible progress indicator; Back retains values; Continue requires a current answer. Escape is not a reset. No health-condition, medication or email question. Recommendations are individual available eligible products, with plain rationale and product links; never a diagnosis, medical score or treatment plan.

States: initial; answer selected; validation; back; calculating; matched results; no eligible matches; missing configuration; retry/reset. On missing/unreviewed rules, provide browse-by-goal links. Do not use the disabled fixture in production. Optional email signup can appear after results, never as a gate and never with quiz answers silently attached.

## C10 Accordion, forms and newsletter

Use native details/summary or buttons with expanded state and linked regions. Space wrapped questions comfortably. Forms have persistent labels, appropriate autocomplete, inline errors plus a summary when useful. Submitting and success states must correspond to actual server responses. Keep user input after failure. Do not claim delivery, account creation or subscription success before confirmation. Newsletter can use the Shopify customer form; any provider integration must be deliberately configured.

## C11 Editorial and recommendations

Render actual article title, excerpt, image, author/date when provided. Missing thumbnail uses a text-first row, not reused stock art. Article contents links land on real heading IDs and do not collide with sticky header. Product recommendations use real handles/variants, omit the current item, exclude unavailable or inappropriate products as configured, and do not imply a clinician recommendation. Related reading avoids self-links.

## Required shared failure language

| Situation | Copy direction |
|---|---|
| Request failed | “We couldn’t update that. Please try again.” |
| Out of stock | “This option is currently unavailable.” |
| No collection matches | “No products match these filters.” + Clear filters |
| No search results | “No results for ‘[query]’.” + editable search |
| Quiz not configured | “Explore products by your goal.” + browse links |
| Form error | Identify the field and correction, preserve other input |

Final exact wording should fit the true cause. Do not show a generic success while an error is present.
