# Data, content and Shopify contracts

## Ownership

The theme renders Shopify catalog, cart, market and content data. V3 JSON files are research/design inputs, not a runtime commerce database. No fixture in this package should overwrite live prices, inventory or variant IDs. Public research establishes product identity and design needs; it does not prove inventory availability or claims approval.

## Product content

| Field | Source | Missing behavior |
|---|---|---|
| Handle/title/vendor | Shopify product | Do not invent a product record |
| Price/currency/compare-at | Selected variant + market formatting | No fake price or savings |
| Options/quantity rules | Variant/options | No synthetic flavor/size menu |
| Availability/ID | Selected variant | Unavailable action, retain product information |
| Front/gallery/label | Actual product media, checked against source group | Neutral missing state; no unrelated photo |
| Description | Approved product content | Short neutral introduction or omit |
| Benefits/ingredients/directions/warnings | Approved current label and merchant-reviewed copy | Omit unsupported facts; maintain warnings where required |
| Reviews | Real published review data | Hide review module if absent; no seeded count/rating |
| Selling plan | Actual plan groups/allocations | One-time purchase; no advertised savings |

Proposed merchant fields: `custom.v3_short_description` (text), `custom.v3_goals` (list of controlled terms), `custom.v3_format` (controlled term), `custom.v3_label_media` (file reference), `custom.v3_usage_copy` (rich text), `custom.v3_warning_copy` (rich text), `custom.v3_related_products` (product references), `custom.v3_eligibility_reviewed` (boolean). These names are a proposal, not existing fields. Confirm field types and data with Shopify admin before wiring filters or quiz logic. Standard Shopify description/media can work before custom fields exist.

## Collection content

Real collection title, description, products and sort options. Page-specific collection image is optional; do not reuse homepage art as filler. Goal filters must be actually configured before they appear. Product-count text comes from real results. The category switcher can navigate to actual collections; do not retain legacy `tmrx_category` parameters unless the implementation deliberately supports and tests them.

## Editorial content

Native Shopify blog/articles: title, handle, excerpt, body, tags, image, author, publish/update dates. A source bibliography belongs in the article if substantive claims require it. Article mockup copy is a neutral layout sample, not a clinical review. Distinct original article imagery is needed per new article; text-first rows are the acceptable fallback. Author/reviewer credentials cannot be synthesized.

## Site settings

Announcement text/link; navigation menus; footer links; verified support contact; shipping threshold enable/amount/market; approved policy links; social URLs; quiz feature flag/rules; newsletter provider and consent language; logo; selected collection/article references. Defaults must be conservative. Do not derive a medical, refund or shipping promise from an image caption.

## Quiz fixture

`manifests/quiz-rules.example.json` documents the shape of an authored eligibility model. It is deliberately `enabled: false` and `review_status: pending-merchant-review`. No automatic clinical scoring is supplied. On production enablement, tie each rule to real product handles, review restrictions, use available variants, and provide an understandable reason. No email gate, no health diagnosis, no sensitive answer storage by default.

## Platform boundaries

Shopify JSON templates and sections implement storefront pages. Customer accounts and checkout depend on shop configuration and platform surfaces; their briefing documents describe a visual handoff, not a promise of Liquid control. Subscription offerings require real selling plans, ordinarily provisioned through an app/backend; theme styling alone does not create a subscription product. [Shopify templates](https://shopify.dev/docs/storefronts/themes/architecture/templates), [subscription architecture](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions).

## Existing-source audit observations

`sections/main-product.liquid` currently seeds review count and average when review metafields are absent, and computes a subscription price from a fixed percentage. Do not copy these into V3. `docs/storefront-build-plan.md` is an older plan and included red placeholders; V3 supersedes that visual fallback. Existing medical language and profile documents are not automatically approved V3 content. This package does not mutate those files.
