# Visual reference review

Reviewed during generation on November 10, 2026. These are generated designs, not browser screenshots of implemented pages. The original attempted mobile homepage retained desktop navigation; the original mobile shop introduced nonexistent products; an initial PDP added a fabricated nutrition table. Those attempts were rejected and are excluded from the package. Selected mobile/PDP revisions use the corrected prompts in `prompts/revisions.json`.

## Selected reference caveats the builder must resolve

| Reference | Assessment | Written rule that wins |
|---|---|---|
| M01 home desktop | Correct overall direction; generated goal still lifes and lower repeated product grouping differ from final asset plan; footer year is synthetic | Use A03–A07 for mapped goals/standards, all four goal links; current year from implementation |
| M02 home phone | Correct stacked phone hero and menu; three goal rows shown, article photo and some inline signup styling are conceptual | Include four goals from P01; journal can be text-first; newsletter fields stack; actual prices must be added |
| M03 shop desktop | Correct grid/filter composition; some pack artwork and category/filter counts are synthetic | Use original product sources, actual results/filter counts, no invented properties |
| M04 shop phone | Correct two-column grid; intentionally reduced to four products and prices omitted to prevent generation drift | Render the actual complete paginated collection with current prices, not four hard-coded products |
| M05 product desktop | Rejected facts panel removed; concept still contains unapproved benefit prose and generated lifestyle portrait | Use neutral/approved copy, A10 editorial asset and authentic gallery; no fabricated claims |
| M06 product phone | Correct buying sequence and improved type; some lower blocks still appear side-by-side | Stack editorial/label and newsletter at phone width per responsive spec; preserve the 40px rhythm in real layout |
| M07 quiz | Clear question composition; generated image adds bottom product photo/newsletter not required in brief | P08 simplified flow wins: no recycled product photo or newsletter in questions, no email gate |
| M08 journal | Fresh feature photograph and clear hierarchy; generated CTA says article recommendations | Quiz remains product discovery, CTA Find my routine; no article-personalization feature is specified |
| M09 article | Coherent typography and fresh article photo; body copy is generated sample | Use approved editorial text and sources; real author/date and product values only |
| M10 cart | Correct two-line subtotal example $169.19 and visible controls | Actual current cart and server response determine all totals/counts; backdrop is illustration only |
| M11 search | Clear query/resource hierarchy; results and stone scene are illustrative | Actual search engine determines matches; no masthead photo is required on this functional page |
| M12 about | New dedicated people photo; extra product image and generated brand prose appear below | A14 is the only dedicated about photography; use approved factual company copy and text-led information block |

## Production use

Do not crop products or labels out of a generated mockup and use them as catalog assets. Do not OCR generated text into theme content. Original product media and page-owned photographic masters are supplied separately for precisely this reason. The small reference-image inaccuracies above do not authorize a builder to reproduce them; specifications, tokens, verified original media and Shopify data are authoritative.

The 14 new photographic masters were inspected for subject, composition, palette, obvious anatomy issues and unintended text. They are design-ready AI imagery, not verified photographs of real customers, staff or clinicians. They must not be captioned as testimonials or identities. Final merchant review and actual crop QA remain part of implementation.
