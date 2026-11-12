# V3 builder handoff

## Find a page without guessing

Read `manifests/pages.json`, match the incoming route against `routes`, open `spec`, and resolve `asset_ids` and `mockup_ids`. Exact special routes take precedence over generic `/pages/:handle`; article routes take precedence over blog routes. Collection families use one new V3 template with real collection content. A product template is a structural family, not permission to duplicate the Essential Aminos facts for all products.

Example: `/products/essential-aminos` → P04 → `specs/pages/P04-product.md` → M05/M06 → preferred A19/A20 (product-filled variants of A09/A10) and the `essential-aminos` product record. `/products/calm` also uses P04, but its original capsule media, variant data, directions and restrictions come from Calm, never from the Aminos example. Product-filled imagery already contains the packaging; do not add it again as an overlay.

Revision 3.1 adds M13/M14 for the drawer, M15/M16 for the full cart page, and M17/M18 for recommendation/empty states. These supersede M10 for cart composition. Read `specs/cart-experience.md`; both surfaces need visual variant-aware recommendations and no-reload cart updates.

## Read before writing theme code

1. `specs/design-system.md` and `specs/tokens.json`.
2. The matching page brief and linked state requirements.
3. `specs/data-contract.md` for required product/collection/editorial fields.
4. `specs/asset-production.md` for original-media handling and slot ownership.
5. `qa/visual-review.md` for intentional differences from generated screenshots.

Use newly named V3 sections/snippets/CSS, for example `v3-header`, `v3-product`, `v3-product-item`, and a scoped token sheet. Do not clone the old layout and recolor it. Reuse Shopify platform data and endpoints, and share new components across V3 pages where appropriate. Complete core functionality before decorative refinements.

## Development roadmap

V1 is live, V2 is the partial existing draft, and V3 is the new redesign. Preserve a recoverable V2 baseline before implementing V3 in draft theme `189659021621`. The comprehensive plan is [DEVELOPMENT-ROADMAP.md](DEVELOPMENT-ROADMAP.md), with [92 task records](manifests/development-roadmap.json), [full task details](development/tasks.md) and [iteration evidence](development/iteration-log.md). Work in one to three related tasks, respect dependencies, and record real verification before marking tasks complete. All tasks are currently planned.

The following table is an orientation only; the task registry governs sequencing and acceptance.

| Stage | Deliverable | Exit condition |
|---|---|---|
| 1 | Token mapping, fresh shell, typography, buttons, accordion, focus styles | 320/390/768/1280/1440 widths; no horizontal page overflow |
| 2 | Collection/product item, native filtering, search | Correct variant media, prices, availability and state restoration |
| 3 | PDP, gallery, form, cart drawer, full cart page and visual recommendations | Real variant ID added without reload; rejected/uncertain requests reconcile; both cart surfaces agree |
| 4 | Homepage using page-owned photography | Tabs work and degrade to links; moderate spacing holds below the fold |
| 5 | Quiz and editorial templates | No email gate; eligibility reviewed; correct empty/error paths |
| 6 | Brand/support forms and informational pages | Approved content and actual endpoints; no invented promises |
| 7 | Full QA and preview deployment | All applicable acceptance checks pass; no invented reviews, offers or facts |

## Decisions that must not be guessed

Selling plans are unverified. Until actual plans exist, show a one-time purchase and omit subscription discounts/upgrades. Shipping threshold is an old planning setting, not a confirmed current policy: keep progress messaging hidden until merchant-approved configuration exists. Current customer-account mode and checkout customization entitlement must be inspected before implementation. Use platform-native handoffs rather than promising a custom account or checkout template.

The quiz is product discovery, not a medical recommendation service. The supplied scoring fixture is disabled for production until catalog eligibility is reviewed. No product should be recommended only because its name resembles an answer. A missing label, testimonial or article image is a missing input, not permission to fabricate it.

## Source changes and deployment

This package changes documentation and design assets only. Do not push it to Shopify as a theme release. When the V3 implementation is separately requested, follow root AGENTS.md: edit locally, review and check, commit, push GitHub, then `npm run theme:push` to existing draft theme `189659021621`. Never create a replacement unpublished theme for a routine update and never publish live without explicit instruction.

## Builder completion report

Report routes implemented; real data connected; missing merchant inputs; widths and functional flows tested; remaining visual differences; Git commit; and the existing draft preview URL when a real theme update occurred. A screenshot-only review is not evidence that the cart or quiz works.
