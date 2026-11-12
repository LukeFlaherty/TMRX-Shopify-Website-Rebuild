# Source ledger

Original research accessed November 10, 2026; cart technical sources S08/S17/S18 reviewed November 12, 2026. Links are the evidence trail; summaries are brief and specific. Source IDs in page records connect requirements to evidence. All design sizes not stated by a source are explicitly V3 decisions.

| ID | Primary source | Finding used |
|---|---|---|
| S01 | [True Matrx home](https://truematrx.com/) | Current brand positioning and catalog context |
| S02 | [True Matrx all products](https://truematrx.com/collections/all) | 16 public product identities and dated price examples |
| S03 | [Essential Aminos](https://truematrx.com/products/essential-aminos), [Bone Broth Protein](https://truematrx.com/products/bone-broth-protein), [Premium Omega](https://truematrx.com/products/true-omega) | Product identity, original-media and option verification starting points; not claims approval |
| S04 | [Shopify template architecture](https://shopify.dev/docs/storefronts/themes/architecture/templates) | Native storefront template model |
| S05 | [Shopify collection template](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) | Collection data/rendering surface |
| S06 | [Shopify product template](https://shopify.dev/docs/storefronts/themes/architecture/templates/product/overview) | Product and variant rendering surface |
| S07 | [Shopify storefront filtering](https://shopify.dev/docs/storefronts/themes/navigation-search/filtering/storefront-filtering) | Configured filter data and URL-backed selections |
| S08 | [Shopify Cart API](https://shopify.dev/docs/api/ajax/reference/cart) | Cart operations, server response reconciliation and error states |
| S09 | [Shopify predictive search](https://shopify.dev/docs/api/ajax/reference/predictive-search), [search template](https://shopify.dev/docs/storefronts/themes/architecture/templates/search) | Search suggestions and full-result fallback |
| S10 | [Shopify subscriptions](https://shopify.dev/docs/storefronts/themes/pricing-payments/subscriptions) | Selling-plan prerequisite; no fake theme-only subscription |
| S11 | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Accessibility baseline and contrast requirements |
| S12 | [W3C target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | AA minimum target guidance and 320 CSS pixel reflow; V3 chooses larger controls |
| S13 | [Google web.dev Web Vitals](https://web.dev/articles/vitals) | LCP, INP and CLS thresholds evaluated at the 75th percentile |
| S14 | [Baymard product-list/filter research](https://baymard.com/research-articles/current-state-product-list-and-filtering) | Applied-filter visibility and product-list organization |
| S15 | [Baymard mobile ecommerce research overview](https://baymard.com/research/mcommerce-usability) | Mobile filtering, product list information and gallery concerns |
| S16 | [Transparent Labs](https://www.transparentlabs.com/) | Public category/goal and cart patterns; used only as research, not copied creative |

| S17 | [Shopify Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering) | Targeted HTML updates without a document reload; limited requested section set |
| S18 | [Shopify product recommendations API](https://shopify.dev/docs/api/ajax/reference/product-recommendations) | Product-seeded related/complementary data, availability-dependent results and curated fallback requirements |

Original repo brand/product files are a separate user-owned source collection. Their byte-level provenance appears in the manifests. Earlier email references and prior concept screenshots were reviewed as history and are not shipped as new V3 creative.

## Cart research application — November 12

S08 supports locale-aware add/change/read operations and bundled section rendering. A mutation may succeed even if a section is null or section rendering fails; inspect/reconcile cart state before retrying an add. S17 supports replacing targeted cart regions while preserving the loaded document, with up to five requested sections. S18 is product-seeded recommendation data, not a general basket-personalization engine. V3 therefore specifies merchant-approved curation, eligibility filtering and a safe empty recommendation state. The proposed controls, spacing and mutation coordinator are V3 implementation decisions. No functional API integration was built or tested in this package revision.
