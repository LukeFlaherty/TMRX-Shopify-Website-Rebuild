# V3 task-by-task implementation list

Future development tasks; proposed filenames are targets, not files already created. The [tracker](../manifests/development-roadmap.json) owns task state and dependencies.

## R00 — Baseline, V1 protection and V2 recovery

Exit: V1 remains untouched; V2 can be restored; the first V3 work is isolated and reproducible.

### D001 — Record version boundaries and protected live target

- **Status:** planned
- **Depends on:** None
- **Pages:** Shared/global work
- **Deliverable:** A written record of the live store, existing draft and planned redesign.
- **Acceptance:** V1 remains live and protected. V2 is the existing partial draft, theme 189659021621. V3 is planned work; package revision 3.1.0 does not mean it is implemented.
- **Proposed targets:** design/v3/development/iteration-log.md; shopify.theme.toml (verify target)
- **Inputs:** Root AGENTS.md deployment workflow; shopify.theme.toml and actual current Git/Shopify state

### D002 — Capture recoverable V2 source and configuration snapshot

- **Status:** planned
- **Depends on:** D001
- **Pages:** Shared/global work
- **Deliverable:** A recoverable snapshot of the actual V2 draft and relevant configuration.
- **Acceptance:** Save the current remote draft before replacing its sections. Record the backup, Git checkpoint and restoration procedure without creating another remote theme.
- **Proposed targets:** design/v3/development/iteration-log.md; shopify.theme.toml (verify target)
- **Inputs:** Root AGENTS.md deployment workflow; shopify.theme.toml and actual current Git/Shopify state

### D003 — Isolate the V3 implementation branch and environment

- **Status:** planned
- **Depends on:** D002
- **Pages:** Shared/global work
- **Deliverable:** An isolated implementation branch and verified draft environment.
- **Acceptance:** Preserve user changes and confirm the draft target. Documentation-only changes do not trigger a Shopify deployment.
- **Proposed targets:** design/v3/development/iteration-log.md; shopify.theme.toml (verify target)
- **Inputs:** Root AGENTS.md deployment workflow; shopify.theme.toml and actual current Git/Shopify state

### D004 — Establish build checks and iteration evidence template

- **Status:** planned
- **Depends on:** D003
- **Pages:** Shared/global work
- **Deliverable:** Baseline checks and a repeatable iteration report.
- **Acceptance:** Record existing failures separately. Each implementation batch has checks, a commit and, when deployed, a matching draft preview.
- **Proposed targets:** design/v3/development/iteration-log.md; shopify.theme.toml (verify target)
- **Inputs:** Root AGENTS.md deployment workflow; shopify.theme.toml and actual current Git/Shopify state

## R01 — Catalog, content and media preparation

Exit: Every current SKU, real option, label, route and required merchant input has an explicit source.

### D010 — Audit current products, variants and markets

- **Status:** planned
- **Depends on:** D003
- **Pages:** P02, P03, P04
- **Deliverable:** A current Shopify catalog and variant audit.
- **Acceptance:** Resolve actual IDs, options, prices, markets and availability. Compare all 16 known identities; the public research snapshot is not a runtime database.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P02-shop.md; specs/pages/P03-category.md; specs/pages/P04-product.md

### D011 — Verify labels, warnings, directions and product formats

- **Status:** planned
- **Depends on:** D010
- **Pages:** P04, P13
- **Deliverable:** A current label and approved content checklist for each SKU.
- **Acceptance:** Directions, warnings, ingredients and media match the actual product. Preserve third-party branding; no generated facts table or copied directions.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** Merchant approval of product content; manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P04-product.md; specs/pages/P13-standards.md

### D012 — Map original media and approve product-filled variants

- **Status:** planned
- **Depends on:** D010, D011
- **Pages:** P01, P02, P04, P08, P10, P11, P12
- **Deliverable:** An approved slot and crop map for original media and product-filled variants.
- **Acceptance:** Products are visible in intended B-roll. Check packaging against original sources and never layer additional bottles over an already product-filled image.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P01-home.md; specs/pages/P02-shop.md; specs/pages/P04-product.md; specs/pages/P08-quiz.md; specs/pages/P10-journal.md; specs/pages/P11-article.md; specs/pages/P12-about.md

### D013 — Resolve low-resolution Secretropin source

- **Status:** planned
- **Depends on:** D011
- **Pages:** P04
- **Deliverable:** A better authentic Secretropin source or a documented limited gallery.
- **Acceptance:** Do not upscale the 265 × 503 source into a large hero. Confirm readable required label media before that SKU is launch-ready.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** Merchant supplies better original media; manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P04-product.md

### D014 — Configure real collections, goal fields and filters

- **Status:** planned
- **Depends on:** D010
- **Pages:** P02, P03
- **Deliverable:** Actual collection destinations and configured goal/format filters.
- **Acceptance:** Every menu destination exists. Only configured facets appear; product membership is deliberate rather than inferred from a name.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P02-shop.md; specs/pages/P03-category.md

### D015 — Confirm shipping, returns, contact and wholesale inputs

- **Status:** planned
- **Depends on:** D003
- **Pages:** P14, P15, P16, P17, P19
- **Deliverable:** Approved operational information and a record of unresolved inputs.
- **Acceptance:** Do not assume shipping thresholds, refund terms, support response times or wholesale eligibility.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** Merchant policy and contact approval; manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P14-contact.md; specs/pages/P15-faq.md; specs/pages/P16-shipping-returns.md; specs/pages/P17-wholesale.md; specs/pages/P19-policies.md

### D016 — Approve navigation, legacy URL preservation and editorial plan

- **Status:** planned
- **Depends on:** D014
- **Pages:** P01, P03, P10, P11, P20
- **Deliverable:** Approved navigation, legacy URL mapping and first-article plan.
- **Acceptance:** Keep existing product handles or record real redirects. Authors, reviewers and editorial approvals are real.
- **Proposed targets:** Shopify admin content/configuration; design/v3/manifests/products.json; design/v3/manifests/assets.json
- **Inputs:** manifests/products.json and manifests/assets.json; Current authenticated Shopify catalog/content/market configuration; specs/pages/P01-home.md; specs/pages/P03-category.md; specs/pages/P10-journal.md; specs/pages/P11-article.md; specs/pages/P20-not-found.md

## R02 — New V3 foundation and shared shell

Exit: Fresh V3 primitives, responsive shell and accessible overlays work with real data and no legacy fabricated fallbacks.

### D020 — Implement fresh V3 tokens and typography

- **Status:** planned
- **Depends on:** D004, D012
- **Pages:** Shared/global work
- **Deliverable:** A fresh scoped V3 token and typography implementation.
- **Acceptance:** Follow the specified colors, spacing and type. Phone body text remains 16px; old V2 CSS and fabricated data fallbacks are not copied.
- **Proposed targets:** assets/v3-base.css (proposed); sections/v3-header.liquid (proposed); sections/v3-footer.liquid (proposed)
- **Inputs:** specs/tokens.json; specs/design-system.md; specs/components-and-states.md; specs/responsive.md

### D021 — Implement new V3 buttons, forms, icons and accordions

- **Status:** planned
- **Depends on:** D020
- **Pages:** P14, P15, P17
- **Deliverable:** Accessible buttons, inputs, icons and accordions.
- **Acceptance:** Controls have usable targets and visible focus. Labels and validation are persistent; individual products remain open on white.
- **Proposed targets:** assets/v3-base.css (proposed); sections/v3-header.liquid (proposed); sections/v3-footer.liquid (proposed)
- **Inputs:** specs/tokens.json; specs/design-system.md; specs/components-and-states.md; specs/responsive.md; specs/pages/P14-contact.md; specs/pages/P15-faq.md; specs/pages/P17-wholesale.md

### D022 — Implement desktop header and real navigation

- **Status:** planned
- **Depends on:** D021, D016
- **Pages:** Shared/global work
- **Deliverable:** A new desktop header and actual navigation menus.
- **Acceptance:** Logo proportions remain correct. Destinations resolve, submenus work by keyboard, and no empty program appears.
- **Proposed targets:** assets/v3-base.css (proposed); sections/v3-header.liquid (proposed); sections/v3-footer.liquid (proposed)
- **Inputs:** specs/tokens.json; specs/design-system.md; specs/components-and-states.md; specs/responsive.md

### D023 — Implement phone header, menu and overlay controller

- **Status:** planned
- **Depends on:** D022
- **Pages:** Shared/global work
- **Deliverable:** Phone navigation and a shared modal controller.
- **Acceptance:** Escape, close and focus return work. Lock background scrolling, handle safe areas and prevent overlapping modals.
- **Proposed targets:** assets/v3-base.css (proposed); sections/v3-header.liquid (proposed); sections/v3-footer.liquid (proposed)
- **Inputs:** specs/tokens.json; specs/design-system.md; specs/components-and-states.md; specs/responsive.md

### D024 — Implement footer, newsletter and policy links

- **Status:** planned
- **Depends on:** D021, D015, D016
- **Pages:** P19
- **Deliverable:** A responsive footer, actual newsletter handler and policy links.
- **Acceptance:** Phone fields stack. Only confirmed server success displays success; omit unverified social links and promises.
- **Proposed targets:** assets/v3-base.css (proposed); sections/v3-header.liquid (proposed); sections/v3-footer.liquid (proposed)
- **Inputs:** specs/tokens.json; specs/design-system.md; specs/components-and-states.md; specs/responsive.md; specs/pages/P19-policies.md

### D025 — Implement responsive media and page-level layout primitives

- **Status:** planned
- **Depends on:** D020, D012
- **Pages:** Shared/global work
- **Deliverable:** Responsive media and layout primitives.
- **Acceptance:** Use correct image sizes and intrinsic dimensions. Prioritize the hero, lazy-load below-fold images, and preserve readable lower-page spacing at 320px.
- **Proposed targets:** assets/v3-base.css (proposed); sections/v3-header.liquid (proposed); sections/v3-footer.liquid (proposed)
- **Inputs:** specs/tokens.json; specs/design-system.md; specs/components-and-states.md; specs/responsive.md

## R03 — Catalog browsing and search

Exit: Visitors can find, narrow and compare actual products and retain browsing context.

### D030 — Implement open product item and real money/availability

- **Status:** planned
- **Depends on:** D010, D025
- **Pages:** P02, P03, P07
- **Deliverable:** An open product item component using actual commerce data.
- **Acceptance:** Original media, current price and availability are accurate. Long titles wrap; no synthetic review badge or enclosing card.
- **Proposed targets:** sections/main-v3-collection.liquid (proposed); sections/main-v3-search.liquid (proposed); snippets/v3-product-item.liquid (proposed)
- **Inputs:** specs/data-contract.md; Current published collections/products and configured filters; specs/pages/P02-shop.md; specs/pages/P03-category.md; specs/pages/P07-search.md

### D031 — Implement Shop All desktop and mobile

- **Status:** planned
- **Depends on:** D030, D014, D023, D024
- **Pages:** P02
- **Deliverable:** The complete Shop All template.
- **Acceptance:** Use real counts, sorting and pagination, three desktop columns and two phone columns. The masthead uses its own product-filled asset.
- **Proposed targets:** sections/main-v3-collection.liquid (proposed); sections/main-v3-search.liquid (proposed); snippets/v3-product-item.liquid (proposed)
- **Inputs:** specs/data-contract.md; Current published collections/products and configured filters; specs/pages/P02-shop.md

### D032 — Implement category/goal collection family

- **Status:** planned
- **Depends on:** D031
- **Pages:** P03
- **Deliverable:** Category and goal collection pages.
- **Acceptance:** Each collection has the correct scope and destination. Missing photography uses the designed text-first masthead rather than borrowed filler.
- **Proposed targets:** sections/main-v3-collection.liquid (proposed); sections/main-v3-search.liquid (proposed); snippets/v3-product-item.liquid (proposed)
- **Inputs:** specs/data-contract.md; Current published collections/products and configured filters; specs/pages/P03-category.md

### D033 — Implement native filters, applied overview and mobile sheet

- **Status:** planned
- **Depends on:** D031
- **Pages:** P02, P03, P07
- **Deliverable:** Native filtering, applied selections and a phone filter sheet.
- **Acceptance:** Selections survive browsing history. Clear and cancel work; zero results preserve context and offer recovery.
- **Proposed targets:** sections/main-v3-collection.liquid (proposed); sections/main-v3-search.liquid (proposed); snippets/v3-product-item.liquid (proposed)
- **Inputs:** specs/data-contract.md; Current published collections/products and configured filters; specs/pages/P02-shop.md; specs/pages/P03-category.md; specs/pages/P07-search.md

### D034 — Implement search results and zero-result states

- **Status:** planned
- **Depends on:** D030, D033
- **Pages:** P07
- **Deliverable:** Search results and no-result layouts.
- **Acceptance:** Submit real queries, separate resource types and keep the query editable. Empty results do not invent products.
- **Proposed targets:** sections/main-v3-collection.liquid (proposed); sections/main-v3-search.liquid (proposed); snippets/v3-product-item.liquid (proposed)
- **Inputs:** specs/data-contract.md; Current published collections/products and configured filters; specs/pages/P07-search.md

### D035 — Implement predictive search and keyboard selection

- **Status:** planned
- **Depends on:** D034, D023
- **Pages:** P07
- **Deliverable:** Predictive search with accessible keyboard selection.
- **Acceptance:** Ignore stale responses. Escape and ordinary submission work when enhancement fails.
- **Proposed targets:** sections/main-v3-collection.liquid (proposed); sections/main-v3-search.liquid (proposed); snippets/v3-product-item.liquid (proposed)
- **Inputs:** specs/data-contract.md; Current published collections/products and configured filters; specs/pages/P07-search.md

## R04 — Product detail and all-SKU completion

Exit: Every known product identity has correct current media, options, price, warnings and purchase states.

### D040 — Implement PDP gallery, thumbnails and label viewer

- **Status:** planned
- **Depends on:** D011, D025, D030
- **Pages:** P04
- **Deliverable:** A product media gallery with thumbnails and readable label viewer.
- **Acceptance:** Use the current product and variant media. Zoom and focus return work; a missing label stays honestly unavailable.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### D041 — Implement variant, price, quantity and product form

- **Status:** planned
- **Depends on:** D010, D040
- **Pages:** P04
- **Deliverable:** A product form bound to real selected variants.
- **Acceptance:** Price, media and options synchronize. Submit the actual variant ID and quantity; unavailable combinations cannot be purchased.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### D042 — Implement PDP content modules and responsive lower page

- **Status:** planned
- **Depends on:** D041, D021
- **Pages:** P04
- **Deliverable:** Responsive product information, routine, usage, FAQ and related-item modules.
- **Acceptance:** Use approved product-specific content. Phone editorial blocks stack; related items exclude the current product.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### D043 — Remove all fabricated commerce and review fallbacks

- **Status:** planned
- **Depends on:** D042
- **Pages:** P04
- **Deliverable:** A V3 source audit for fabricated commerce data.
- **Acceptance:** No seeded review counts or averages, synthetic discount price, or unconfigured subscription offer remains.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### D044 — Validate purchase and display across format families

- **Status:** planned
- **Depends on:** D041, D042
- **Pages:** P04
- **Deliverable:** Verification across powder, capsule, softgel, spray and lozenge families.
- **Acceptance:** Each family uses its own directions, warnings, labels and purchase controls; no powder instructions leak into other products.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU01 — Complete and verify product: bone-broth-protein

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for bone-broth-protein.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for bone-broth-protein. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product bone-broth-protein; assets/products/08-bone-broth-protein-60095949603125.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU02 — Complete and verify product: calm

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for calm.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for calm. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product calm; assets/products/47-calm-40565553430837.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU03 — Complete and verify product: true-creatine

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for true-creatine.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for true-creatine. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product true-creatine; assets/products/57-true-creatine-39924672299317.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU04 — Complete and verify product: creatine-hcl

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for creatine-hcl.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for creatine-hcl. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product creatine-hcl; assets/products/04-creatine-hcl-62242702098741.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU05 — Complete and verify product: dna-support

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for dna-support.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for dna-support. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product dna-support; assets/products/34-dna-support-44141053935925.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU06 — Complete and verify product: essential-aminos

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for essential-aminos.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for essential-aminos. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product essential-aminos; assets/products/21-essential-aminos-58348251808053.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU07 — Complete and verify product: hormone-support

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for hormone-support.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for hormone-support. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product hormone-support; assets/products/42-hormone-support-39976632844597.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU08 — Complete and verify product: liver-support

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for liver-support.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for liver-support. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product liver-support; assets/products/37-liver-support-40565565161781.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU09 — Complete and verify product: methylation-support

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for methylation-support.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for methylation-support. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product methylation-support; assets/products/13-methylation-support-59834122666293.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU10 — Complete and verify product: mito-revive

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for mito-revive.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for mito-revive. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product mito-revive; assets/products/01-mito-revive-63989518795061.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU11 — Complete and verify product: myos-md-vanilla

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for myos-md-vanilla.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for myos-md-vanilla. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product myos-md-vanilla; assets/products/11-myos-md-vanilla-59626407821621.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU12 — Complete and verify product: n1o1-nitric-oxide-lozenges

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for n1o1-nitric-oxide-lozenges.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for n1o1-nitric-oxide-lozenges. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product n1o1-nitric-oxide-lozenges; assets/products/18-n1o1-nitric-oxide-lozenges-57776795615541.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU13 — Complete and verify product: true-omega

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for true-omega.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for true-omega. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product true-omega; assets/products/52-true-omega-40565451424053.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU14 — Complete and verify product: secretropin

- **Status:** planned
- **Depends on:** D044, D011, D013
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for secretropin.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for secretropin. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product secretropin; assets/products/07-secretropin-63989622866229.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU15 — Complete and verify product: true-greens

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for true-greens.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for true-greens. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product true-greens; assets/products/26-true-greens-40565473378613.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

### SKU16 — Complete and verify product: vitamin-d-k2

- **Status:** planned
- **Depends on:** D044, D011
- **Pages:** P04
- **Deliverable:** A completed V3 product record and page for vitamin-d-k2.
- **Acceptance:** Bind current Shopify options, price, availability, approved copy, original media and label for vitamin-d-k2. Test purchase, unavailable and error states, format-specific directions and phone/desktop gallery behavior. Do not inherit another product's data.
- **Proposed targets:** sections/main-v3-product.liquid (proposed); assets/v3-product.js (proposed)
- **Inputs:** Current Shopify product vitamin-d-k2; assets/products/31-vitamin-d-k2-44141112557877.png; specs/data-contract.md; manifests/products.json; Current approved variant labels, options, availability and content; specs/pages/P04-product.md

## R05 — Cart engine, drawer, page and visual recommendations

Exit: All mutations reconcile to Shopify without page reload; drawer and full cart agree and recommendation controls work.

### D050 — Build single shared Ajax cart mutation coordinator

- **Status:** planned
- **Depends on:** D041, D023
- **Pages:** P04, P05, P06
- **Deliverable:** A single shared Ajax cart coordinator.
- **Acceptance:** Use real variant IDs and line keys with locale-aware endpoints. Serialize cart mutations; successful enhanced actions do not reload or navigate the document.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P04-product.md; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D051 — Build coordinated cart sections and partial-render recovery

- **Status:** planned
- **Depends on:** D050
- **Pages:** P05, P06
- **Deliverable:** A shared contract for cart sections and recovery.
- **Acceptance:** Update cart lines, header count, summary and recommendations from authoritative state. Null section HTML triggers a read/render recovery, never a second add.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D052 — Implement populated desktop cart drawer

- **Status:** planned
- **Depends on:** D051, D021
- **Pages:** P05
- **Deliverable:** The populated desktop drawer.
- **Acceptance:** Cart lines and checkout remain usable within a 440–480px panel. Keep the drawer open, retain focus and preserve scroll position after updates.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md

### D053 — Implement phone cart drawer and safe-area behavior

- **Status:** planned
- **Depends on:** D052
- **Pages:** P05
- **Deliverable:** The phone drawer layout and behavior.
- **Acceptance:** Use a full-width sheet with safe-area padding and usable controls. Recommendations must not obscure checkout or require tiny taps.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md

### D054 — Implement standalone full cart page

- **Status:** planned
- **Depends on:** D051, D024
- **Pages:** P06
- **Deliverable:** A complete standalone cart page.
- **Acceptance:** Desktop and phone layouts support real totals, discounts, quantities and removal. Ajax enhancement updates in place; a normal form remains the no-JS fallback.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P06-cart.md

### D055 — Implement recommendation source and eligibility rules

- **Status:** planned
- **Depends on:** D010, D051
- **Pages:** P05, P06
- **Deliverable:** A recommendation candidate source and eligibility filter.
- **Acceptance:** Use merchant curation or supported product recommendations. Exclude unavailable, unpublished, restricted and already-in-cart products; hide an empty module.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D056 — Implement visual recommendation item and inline variant choice

- **Status:** planned
- **Depends on:** D055, D021
- **Pages:** P05, P06
- **Deliverable:** Visual recommendation rows and inline option selection.
- **Acceptance:** Show original packshot, name, real price and action. Multiple variants require a deliberate valid selection; never silently pick the wrong option.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D057 — Wire recommendation add without reloading

- **Status:** planned
- **Depends on:** D056, D052, D053, D054
- **Pages:** P05, P06
- **Deliverable:** Recommendation adds connected to the shared cart.
- **Acceptance:** Add one selected variant, update the cart, count, subtotal and candidate pool in place, and announce success. Keep the same URL and prevent duplicate submissions.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D058 — Implement empty cart page and drawer recommendations

- **Status:** planned
- **Depends on:** D054, D055, D056
- **Pages:** P05, P06
- **Deliverable:** Empty page and drawer states with visual starters.
- **Acceptance:** Do not enable checkout for an empty bag. Adding a starter changes the same surface to populated without a document reload.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D059 — Handle rapid actions, inventory conflicts and failure recovery

- **Status:** planned
- **Depends on:** D057, D058
- **Pages:** P05, P06
- **Deliverable:** Recovery for rapid actions, stock conflicts and unknown outcomes.
- **Acceptance:** Do not apply stale state or reuse obsolete line keys. Reconcile the cart after uncertain writes before offering a retry; recommendation errors do not break checkout.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D060 — Verify cart consistency and no-reload network evidence

- **Status:** planned
- **Depends on:** D059
- **Pages:** P04, P05, P06
- **Deliverable:** An end-to-end cart verification record.
- **Acceptance:** Drawer, cart page and header agree. Record network evidence of no successful document navigation and test empty transitions, quantities, currency, discounts and focus.
- **Proposed targets:** assets/v3-cart.js (proposed); sections/v3-cart-drawer.liquid (proposed); sections/main-v3-cart.liquid (proposed); snippets/v3-cart-recommendation.liquid (proposed)
- **Inputs:** specs/cart-experience.md; qa/cart-scenarios.md; Current Shopify cart/variant data and merchant-approved recommendation candidates; specs/pages/P04-product.md; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

## R06 — Homepage and product-led visual polish

Exit: Homepage A direction is complete with product-filled imagery and moderate lower-page spacing.

### D070 — Implement homepage hero and product-filled responsive media

- **Status:** planned
- **Depends on:** D025, D030, D031
- **Pages:** P01
- **Deliverable:** The homepage hero with product-filled responsive artwork.
- **Acceptance:** Use A15/A16 or an approved original-layer composition. Keep headline and actions as HTML; do not add duplicate products over the filled images.
- **Proposed targets:** sections/v3-home-*.liquid (proposed); templates/index.json (future implementation)
- **Inputs:** manifests/assets.json and preferred product-filled variants; specs/tokens.json; Current native collections and published editorial content; specs/pages/P01-home.md

### D071 — Implement featured category/product swapper

- **Status:** planned
- **Depends on:** D070, D033
- **Pages:** P01
- **Deliverable:** The working featured-product category swapper.
- **Acceptance:** Keyboard and no-JS navigation work. Real prices and honest featured/bestseller labels remain correct through loading, empty and error states.
- **Proposed targets:** sections/v3-home-*.liquid (proposed); templates/index.json (future implementation)
- **Inputs:** manifests/assets.json and preferred product-filled variants; specs/tokens.json; Current native collections and published editorial content; specs/pages/P01-home.md

### D072 — Implement goal discovery and standards section

- **Status:** planned
- **Depends on:** D071
- **Pages:** P01
- **Deliverable:** Four goal destinations and the standards section.
- **Acceptance:** Use A24/A25/A26 and A06, plus the dedicated standards variant. No repeated filler; phone layouts follow the moderate spacing scale.
- **Proposed targets:** sections/v3-home-*.liquid (proposed); templates/index.json (future implementation)
- **Inputs:** manifests/assets.json and preferred product-filled variants; specs/tokens.json; Current native collections and published editorial content; specs/pages/P01-home.md

### D073 — Implement routine CTA, native journal preview and signup

- **Status:** planned
- **Depends on:** D072, D024
- **Pages:** P01
- **Deliverable:** The routine CTA, actual blog previews and newsletter.
- **Acceptance:** Avoid duplicate quiz prompts. Missing article art uses the designed text-first preview; signup reports real results.
- **Proposed targets:** sections/v3-home-*.liquid (proposed); templates/index.json (future implementation)
- **Inputs:** manifests/assets.json and preferred product-filled variants; specs/tokens.json; Current native collections and published editorial content; specs/pages/P01-home.md

### D074 — Review complete homepage at all target widths

- **Status:** planned
- **Depends on:** D073, D060
- **Pages:** P01
- **Deliverable:** A complete homepage review at every target width.
- **Acceptance:** The middle and lower page feel relaxed without empty bands. Categories, shopping links and cart interactions work.
- **Proposed targets:** sections/v3-home-*.liquid (proposed); templates/index.json (future implementation)
- **Inputs:** manifests/assets.json and preferred product-filled variants; specs/tokens.json; Current native collections and published editorial content; specs/pages/P01-home.md

## R07 — Routine quiz and product-discovery results

Exit: Accessible quiz has reviewed eligibility or honest browse fallback, no email gate and no medical scoring.

### D080 — Approve nonmedical quiz options and eligibility inputs

- **Status:** planned
- **Depends on:** D010, D011
- **Pages:** P08, P09
- **Deliverable:** Reviewed quiz options and product eligibility, or a disabled decision.
- **Acceptance:** Do not ask for diagnosis, medication or email. Production matching remains disabled until its rules are reviewed.
- **Proposed targets:** sections/v3-routine-quiz.liquid (proposed); assets/v3-quiz.js (proposed)
- **Inputs:** Merchant eligibility approval; manifests/quiz-rules.example.json; DECISIONS.md quiz eligibility decision; specs/pages/P08-quiz.md; specs/pages/P09-quiz-results.md

### D081 — Implement quiz entry and accessible question flow

- **Status:** planned
- **Depends on:** D021, D023, D025
- **Pages:** P08
- **Deliverable:** An accessible three-step quiz.
- **Acceptance:** Progress, fieldsets, radio choices, Back and Continue work with retained answers. Use the product-filled entry image and no email gate.
- **Proposed targets:** sections/v3-routine-quiz.liquid (proposed); assets/v3-quiz.js (proposed)
- **Inputs:** manifests/quiz-rules.example.json; DECISIONS.md quiz eligibility decision; specs/pages/P08-quiz.md

### D082 — Implement reviewed matches, no-match and browse fallback

- **Status:** planned
- **Depends on:** D080, D081, D030
- **Pages:** P09
- **Deliverable:** Results, no-match and browse fallback states.
- **Acceptance:** Show eligible available individual products with understandable reasons. Missing rules lead to real browsing rather than invented matches.
- **Proposed targets:** sections/v3-routine-quiz.liquid (proposed); assets/v3-quiz.js (proposed)
- **Inputs:** manifests/quiz-rules.example.json; DECISIONS.md quiz eligibility decision; specs/pages/P09-quiz-results.md

### D083 — Verify quiz analytics/privacy and optional follow-up

- **Status:** planned
- **Depends on:** D082
- **Pages:** P08, P09
- **Deliverable:** A privacy and analytics verification record for the quiz.
- **Acceptance:** Do not attach answers silently to email signup. Edit and reset work; no sensitive fields are collected by default.
- **Proposed targets:** sections/v3-routine-quiz.liquid (proposed); assets/v3-quiz.js (proposed)
- **Inputs:** manifests/quiz-rules.example.json; DECISIONS.md quiz eligibility decision; specs/pages/P08-quiz.md; specs/pages/P09-quiz-results.md

## R08 — Journal and article system

Exit: Native editorial browsing and reading work with approved content and distinct imagery.

### D090 — Prepare approved native blog/articles and taxonomy

- **Status:** planned
- **Depends on:** D016
- **Pages:** P10, P11
- **Deliverable:** Approved native editorial content and taxonomy.
- **Acceptance:** Do not publish generated mockup prose as researched medical content. Any displayed author or reviewer is real.
- **Proposed targets:** sections/main-v3-blog.liquid (proposed); sections/main-v3-article.liquid (proposed)
- **Inputs:** Merchant editorial approval; Merchant-approved native blog/article content; manifests/assets.json; specs/pages/P10-journal.md; specs/pages/P11-article.md

### D091 — Implement journal index, topics and pagination

- **Status:** planned
- **Depends on:** D030, D024, D090
- **Pages:** P10
- **Deliverable:** The journal index, topic filtering and pagination.
- **Acceptance:** Use actual articles and A22 for the example feature. Text-first rows replace missing unique thumbnails.
- **Proposed targets:** sections/main-v3-blog.liquid (proposed); sections/main-v3-article.liquid (proposed)
- **Inputs:** Merchant-approved native blog/article content; manifests/assets.json; specs/pages/P10-journal.md

### D092 — Implement article layout, contents and product context

- **Status:** planned
- **Depends on:** D091
- **Pages:** P11
- **Deliverable:** The article reading layout and contextual links.
- **Acceptance:** Use readable measure, working contents anchors and A23 for the example article. Product and author metadata come from real sources.
- **Proposed targets:** sections/main-v3-blog.liquid (proposed); sections/main-v3-article.liquid (proposed)
- **Inputs:** Merchant-approved native blog/article content; manifests/assets.json; specs/pages/P11-article.md

### D093 — Verify long, short, missing-image and unpublished articles

- **Status:** planned
- **Depends on:** D092
- **Pages:** P10, P11, P20
- **Deliverable:** Verification of article and blog edge cases.
- **Acceptance:** Check long and short content, no image, no author, zero articles and unpublished URLs. Anchors are not hidden by the sticky header.
- **Proposed targets:** sections/main-v3-blog.liquid (proposed); sections/main-v3-article.liquid (proposed)
- **Inputs:** Merchant-approved native blog/article content; manifests/assets.json; specs/pages/P10-journal.md; specs/pages/P11-article.md; specs/pages/P20-not-found.md

## R09 — Brand, support and operational pages

Exit: All planned informational pages and forms are complete or explicitly gated on merchant input.

### D100 — Implement About and standards information pages

- **Status:** planned
- **Depends on:** D024, D011, D025
- **Pages:** P12, P13
- **Deliverable:** The About and standards pages.
- **Acceptance:** Use A14 only where assigned. Company facts, report links and standards claims are approved; no invented clinical authority.
- **Proposed targets:** New V3 page sections/templates (proposed)
- **Inputs:** Merchant-approved brand/support/legal content and actual form destinations; specs/data-contract.md; specs/pages/P12-about.md; specs/pages/P13-standards.md

### D101 — Implement contact form and support channels

- **Status:** planned
- **Depends on:** D021, D024, D015
- **Pages:** P14
- **Deliverable:** The contact form and support links.
- **Acceptance:** Persistent labels and real validation preserve messages after failure. No fake contact details or delivery confirmation.
- **Proposed targets:** New V3 page sections/templates (proposed)
- **Inputs:** Merchant-approved brand/support/legal content and actual form destinations; specs/data-contract.md; specs/pages/P14-contact.md

### D102 — Implement categorized FAQ content and deep links

- **Status:** planned
- **Depends on:** D101
- **Pages:** P15
- **Deliverable:** Approved FAQ groups and deep links.
- **Acceptance:** Questions wrap naturally. Product-specific safety or dosing answers are not generalized; accordions work by keyboard.
- **Proposed targets:** New V3 page sections/templates (proposed)
- **Inputs:** Merchant-approved brand/support/legal content and actual form destinations; specs/data-contract.md; specs/pages/P15-faq.md

### D103 — Implement shipping/returns and canonical policy surfaces

- **Status:** planned
- **Depends on:** D015, D024
- **Pages:** P16, P19
- **Deliverable:** Current shipping, returns and canonical policy layouts.
- **Acceptance:** Summary and policy agree. No assumed threshold, guarantee or substitute legal text is published.
- **Proposed targets:** New V3 page sections/templates (proposed)
- **Inputs:** Merchant-approved brand/support/legal content and actual form destinations; specs/data-contract.md; specs/pages/P16-shipping-returns.md; specs/pages/P19-policies.md

### D104 — Implement wholesale inquiry and operational handoff

- **Status:** planned
- **Depends on:** D015, D021, D024
- **Pages:** P17
- **Deliverable:** A professional wholesale inquiry flow.
- **Acceptance:** Connect a real handler. Do not promise automatic approval, discount tiers or response times.
- **Proposed targets:** New V3 page sections/templates (proposed)
- **Inputs:** Merchant-approved brand/support/legal content and actual form destinations; specs/data-contract.md; specs/pages/P17-wholesale.md

### D105 — Implement 404 and missing-resource recovery

- **Status:** planned
- **Depends on:** D034, D024
- **Pages:** P20
- **Deliverable:** A correct 404 recovery page.
- **Acceptance:** Return the correct status, retain usable search and real category links, and do not conceal missing routes with automatic redirects.
- **Proposed targets:** New V3 page sections/templates (proposed)
- **Inputs:** Merchant-approved brand/support/legal content and actual form destinations; specs/data-contract.md; specs/pages/P20-not-found.md

## R10 — Accounts, subscriptions and checkout handoffs

Exit: Actual Shopify capabilities are respected and conditional programs cannot advertise unconfigured offers.

### D110 — Inspect actual account and checkout configuration

- **Status:** planned
- **Depends on:** D003, D060
- **Pages:** P21, P22
- **Deliverable:** An actual account/checkout capability record.
- **Acceptance:** Inspect configured account mode and customization entitlement. No unsupported custom login or Liquid checkout is assumed.
- **Proposed targets:** Actual Shopify account/checkout and selling-plan surfaces
- **Inputs:** Actual Shopify account, checkout and selling-plan configuration; Root AGENTS.md deployment workflow; specs/pages/P21-accounts.md; specs/pages/P22-checkout.md

### D111 — Implement account entry and native return journeys

- **Status:** planned
- **Depends on:** D110, D022, D023
- **Pages:** P21
- **Deliverable:** Native account entry and return journeys.
- **Acceptance:** Use actual account routes. Do not collect credentials in a custom theme form; verify phone signed-in and signed-out access.
- **Proposed targets:** Actual Shopify account/checkout and selling-plan surfaces
- **Inputs:** Actual Shopify account, checkout and selling-plan configuration; Root AGENTS.md deployment workflow; specs/pages/P21-accounts.md

### D112 — Decide subscription scope from actual selling plans

- **Status:** planned
- **Depends on:** D010, D110
- **Pages:** P18, P04
- **Deliverable:** A subscription enable/disable decision based on actual plans.
- **Acceptance:** Use real allocation prices and provider terms. Missing plans hide the program instead of generating a fixed discount.
- **Proposed targets:** Actual Shopify account/checkout and selling-plan surfaces
- **Inputs:** Merchant subscription configuration/decision; Actual Shopify account, checkout and selling-plan configuration; Root AGENTS.md deployment workflow; specs/pages/P18-subscriptions.md; specs/pages/P04-product.md

### D113 — Implement eligible subscription information/controls only if enabled

- **Status:** planned
- **Depends on:** D112, D041
- **Pages:** P18, P04, P05, P06
- **Deliverable:** Conditional subscription information and purchase controls.
- **Acceptance:** When enabled, use real plan IDs, schedules and prices. Preserve separate cart lines for distinct plans; otherwise verify the hidden state.
- **Proposed targets:** Actual Shopify account/checkout and selling-plan surfaces
- **Inputs:** Actual Shopify account, checkout and selling-plan configuration; Root AGENTS.md deployment workflow; specs/pages/P18-subscriptions.md; specs/pages/P04-product.md; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md

### D114 — Verify checkout and order confirmation handoff in test mode

- **Status:** planned
- **Depends on:** D110, D111, D113, D060
- **Pages:** P22
- **Deliverable:** A test-mode checkout and order confirmation verification.
- **Acceptance:** Check shipping/address/payment errors and real confirmation. No real charge by default and no synthetic successful-order page.
- **Proposed targets:** Actual Shopify account/checkout and selling-plan surfaces
- **Inputs:** Actual Shopify account, checkout and selling-plan configuration; Root AGENTS.md deployment workflow; specs/pages/P22-checkout.md

## R11 — Whole-store QA and content readiness

Exit: Functional, visual, responsive, accessibility, performance and data acceptance evidence is recorded.

### D120 — Run real-width full-store visual and spacing review

- **Status:** planned
- **Depends on:** D001, D002, D003, D004, D010, D011, D012, D013, D014, D015, D016, D020, D021, D022, D023, D024, D025, D030, D031, D032, D033, D034, D035, D040, D041, D042, D043, D044, D050, D051, D052, D053, D054, D055, D056, D057, D058, D059, D060, D070, D071, D072, D073, D074, D080, D081, D082, D083, D090, D091, D092, D093, D100, D101, D102, D103, D104, D105, D110, D111, D112, D113, D114, SKU01, SKU02, SKU03, SKU04, SKU05, SKU06, SKU07, SKU08, SKU09, SKU10, SKU11, SKU12, SKU13, SKU14, SKU15, SKU16
- **Pages:** Shared/global work
- **Deliverable:** A whole-store visual review matrix.
- **Acceptance:** Review 320, 360, 390, 430, 768, 1024, 1280 and 1440px. Eliminate cramped lower sections, overflow, tiny desktop columns and excessive blank bands.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence

### D121 — Run keyboard, screen reader and overlay acceptance

- **Status:** planned
- **Depends on:** D120
- **Pages:** Shared/global work
- **Deliverable:** Keyboard, assistive technology and reflow evidence.
- **Acceptance:** Verify menu, filters, gallery, cart, quiz and forms; visible focus, useful announcements and reduced-motion behavior.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence

### D122 — Run commerce regression and no-reload recommendation tests

- **Status:** planned
- **Depends on:** D120, D060, D114
- **Pages:** P04, P05, P06, P22
- **Deliverable:** Commerce regression and no-reload recommendation evidence.
- **Acceptance:** Test add/change/remove, variants, plans, stock, discounts and timeouts. Same-URL Ajax updates do not duplicate items and never rely on static research prices.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence; specs/pages/P04-product.md; specs/pages/P05-cart-drawer.md; specs/pages/P06-cart.md; specs/pages/P22-checkout.md

### D123 — Verify search, filters, history and no-JS fallbacks

- **Status:** planned
- **Depends on:** D121
- **Pages:** P01, P02, P03, P07, P20
- **Deliverable:** Search, filter, history and no-JS evidence.
- **Acceptance:** Restore context after product browsing. Ordinary links and forms remain usable when enhancement fails.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence; specs/pages/P01-home.md; specs/pages/P02-shop.md; specs/pages/P03-category.md; specs/pages/P07-search.md; specs/pages/P20-not-found.md

### D124 — Optimize media, loading and performance budgets

- **Status:** planned
- **Depends on:** D120
- **Pages:** Shared/global work
- **Deliverable:** Media and runtime performance measurements.
- **Acceptance:** Use selected responsive derivatives, not every master. Record loading/layout stability and an appropriate lab baseline plus field-measurement plan.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence

### D125 — Audit content, links, metadata, indexing and approved analytics

- **Status:** planned
- **Depends on:** D120, D123
- **Pages:** Shared/global work
- **Deliverable:** A final content, link and metadata audit.
- **Acceptance:** No fabricated reviews, offers or claims; actual product/currency values and preserved canonical destinations. Approved analytics and consent settings are preserved or deliberately reconnected; a test shopping journey does not emit duplicate add-to-cart events after section replacement.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence

### D126 — Close merchant decisions or explicitly gate unavailable modules

- **Status:** planned
- **Depends on:** D125, D112, D080, D015, D013
- **Pages:** Shared/global work
- **Deliverable:** A closed decision register or safe gating of unresolved modules.
- **Acceptance:** Do not declare launch readiness while an unresolved business or media requirement is silently bypassed.
- **Proposed targets:** Future V3 implementation QA evidence
- **Inputs:** qa/implementation-checklist.md; qa/cart-scenarios.md; Actual completed V3 implementation and recorded task evidence

## R12 — Draft releases, review and launch handoff

Exit: A reviewed V3 draft has reproducible source and rollback; live publish remains an explicit user decision.

### D130 — Prepare reviewable draft release candidate

- **Status:** planned
- **Depends on:** D120, D121, D122, D123, D124, D125, D126
- **Pages:** Shared/global work
- **Deliverable:** A reproducible review candidate with recovery checkpoint.
- **Acceptance:** All required acceptance evidence and SKU checks pass; source, checks and rollback record identify the same candidate.
- **Proposed targets:** Git/source checkpoints; Existing unpublished Shopify draft
- **Inputs:** Root AGENTS.md deployment workflow; development/iteration-log.md and verified roadmap evidence; Existing unpublished draft 189659021621 and recoverable source checkpoints

### D131 — Push source and update only the existing unpublished draft

- **Status:** planned
- **Depends on:** D130
- **Pages:** Shared/global work
- **Deliverable:** A source checkpoint pushed before updating the existing draft.
- **Acceptance:** Verify theme 189659021621 and use the normal draft command. Do not use --unpublished or publish live.
- **Proposed targets:** Git/source checkpoints; Existing unpublished Shopify draft
- **Inputs:** Root AGENTS.md deployment workflow; development/iteration-log.md and verified roadmap evidence; Existing unpublished draft 189659021621 and recoverable source checkpoints

### D132 — Run post-push preview smoke tests and merchant review

- **Status:** planned
- **Depends on:** D131
- **Pages:** Shared/global work
- **Deliverable:** Post-deployment preview smoke tests and merchant review.
- **Acceptance:** Confirm the deployed preview matches the commit and test desktop/phone navigation, PDP, recommendations, bag and checkout handoff.
- **Proposed targets:** Git/source checkpoints; Existing unpublished Shopify draft
- **Inputs:** Root AGENTS.md deployment workflow; development/iteration-log.md and verified roadmap evidence; Existing unpublished draft 189659021621 and recoverable source checkpoints

### D133 — Record V3 acceptance and remaining rollout decisions

- **Status:** planned
- **Depends on:** D132
- **Pages:** Shared/global work
- **Deliverable:** Merchant acceptance or clearly scoped follow-up tasks.
- **Acceptance:** Review feedback becomes discrete tasks with evidence. No automatic promotion to live.
- **Proposed targets:** Git/source checkpoints; Existing unpublished Shopify draft
- **Inputs:** Root AGENTS.md deployment workflow; development/iteration-log.md and verified roadmap evidence; Existing unpublished draft 189659021621 and recoverable source checkpoints

### D134 — Publish V3 only after explicit live-publish instruction

- **Status:** planned
- **Depends on:** D133
- **Pages:** Shared/global work
- **Deliverable:** An explicitly authorized V3 launch.
- **Acceptance:** Wait for a direct user instruction to publish live. Preserve V1 recovery and use an approved launch/rollback plan.
- **Proposed targets:** Git/source checkpoints; Existing unpublished Shopify draft
- **Inputs:** Explicit user authorization to publish live; Root AGENTS.md deployment workflow; development/iteration-log.md and verified roadmap evidence; Existing unpublished draft 189659021621 and recoverable source checkpoints

### D135 — Verify production and close rollout

- **Status:** planned
- **Depends on:** D134
- **Pages:** Shared/global work
- **Deliverable:** Production verification and final handover.
- **Acceptance:** Verify the published theme and customer journeys; record monitoring and recovery ownership.
- **Proposed targets:** Git/source checkpoints; Existing unpublished Shopify draft
- **Inputs:** Root AGENTS.md deployment workflow; development/iteration-log.md and verified roadmap evidence; Existing unpublished draft 189659021621 and recoverable source checkpoints
