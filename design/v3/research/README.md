# Research approach and findings

Researched November 10, 2026, using public first-party store pages, Shopify documentation, W3C guidance, Google web.dev and Baymard's own public research. No authenticated Shopify admin, private analytics, paid Baymard findings or clinical literature review was available. Sources may be cached by the browsing service; collection/product identity was cross-checked where possible. Recheck operational data before launch.

## Evidence → V3 decision

| Evidence | Implication | V3 decision | Source |
|---|---|---|---|
| True Matrx public catalog includes powders, capsules, softgels, a spray and lozenges | One powder-specific PDP cannot describe all products | Shared structure, format-specific real product information | S01–S03 and product records |
| User repeatedly selected A and asked for modest breathing room | Density should be controlled in tokens rather than by image height | Explicit 36–40px phone section rhythm and local gaps | Conversation decision history |
| Shopify exposes native template/data patterns | The rebuild can remain theme-native | Fresh V3 JSON/section implementation; no headless rewrite | S04–S06 |
| Filter state is encoded in platform URLs | Navigation and result restoration need stable state | Native configured filters, applied-filter summary and clear-all | S07, S14 |
| Cart requests have inventory/error behavior | Optimistic visuals alone cannot prove successful update | Reconcile server cart, retain user selections and show errors | S08 |
| Subscriptions use actual selling plans | A styled “save” toggle is insufficient | Hide until real plans/allocations exist | S10 |
| Mobile browsing needs discoverable filtering and balanced product information | Desktop sidebars cannot simply shrink | Two-column phone products, Filter/Sort controls and a modal filter panel | S14–S15 |
| Reflow, focus, control size and contrast are essential interface constraints | Beautiful screenshots can still fail usable implementation | Accessible form/overlay contracts and real-width QA | S11–S12 |
| Loading, response and stability are measured separately | A large all-page image is not a website implementation | Responsive media, intrinsic sizes, conditional loading and field metrics | S13 |
| Transparent Labs offers goal/category discovery and a cart surface | The user's reference favors clear shopping paths | Keep useful commerce patterns; original V3 art/content | S16 |

## What the research does not establish

The storefront's claims are observations, not independently substantiated health claims. Public “Sold out” and “Add to cart” text may coexist in extracted templates; therefore this package intentionally does not certify variant availability. Public price examples are dated snapshots. Current shipping, selling-plan configuration, refund terms, doctor role, clinic affiliation and customer-account mode are unresolved unless the merchant supplies current approval.

## Design inference vs. evidence

Blue palette, stone staging, precise spacing, modest motion, typography scale, editorial image ownership and content order are V3 design decisions. They are not claimed to be a guaranteed conversion improvement or dictated by Shopify/WCAG. Baymard's public findings inform filter visibility and content organization; no proprietary guideline is reproduced. No competitor photograph, screenshot or copy is bundled as a V3 creative asset.

Read [the source ledger](sources.md), [catalog snapshot](catalog-snapshot.md), and [decision register](../DECISIONS.md) before treating a business detail as confirmed.
