# Future implementation acceptance checklist

This checklist applies when a real V3 theme is built. It is not a claim that these tests have already run on a website.

## Content and identity

- Every product title, price, currency, option and inventory state comes from current Shopify data.
- Original packaging/label media matches the selected variant. No generated nutrition facts or invented certifications.
- No review count, star average, discount, sales ranking, doctor endorsement or medical result is fabricated.
- No old V2 section/CSS is silently reused; shared V3 components are newly implemented.
- Page-owned photography is used only in assigned slots. No old campaign image or unrelated SKU fallback.
- Policies, shipping promises, support addresses, professional credentials and wholesale terms have current merchant approval.

## Desktop and phone composition

- Review 320/360/390/430/768/1024/1280/1440px widths at natural scale.
- No page-level horizontal overflow; product/category rails have accessible controls.
- Header controls do not collide; mobile has a real menu and usable search/bag actions.
- Two-column phone collection grid wraps names without collisions; filter sidebar becomes a dialog.
- PDP gallery stacks above buying controls; options/action are not obscured.
- Every mid/lower section follows spacing tokens. Headings, icon rows, FAQ answers and buttons do not crowd.
- No giant empty bands, tiny scaled-down lower sections or fixed-height content clipping.

## Functional flows

- Category switching updates products or navigates to actual collections and has no-JS fallback.
- Apply/remove/clear filters; sort; paginate; open PDP; return to results with state retained.
- Select available/unavailable variant; adjust quantity; add; handle network failure; handle stock conflict.
- Cart quantities, remove, discounts and totals reconcile with Shopify response; empty cart and cart page work.
- Checkout uses current Shopify flow. No unsupported custom checkout/account assumptions.
- Search supports ordinary submission, predictive keyboard use, no results and failed requests.
- Quiz retains answers, has accessible validation, no email gate and safe missing-rules/no-match states.
- Contact/newsletter/wholesale forms submit to real configured handlers; preserve input after errors; honest success.

## Accessibility

- Keyboard-only journey includes menu, filter, gallery zoom, buy controls, cart, quiz and forms.
- Modals trap focus, background is inert, Escape closes, focus returns to opener.
- Visible focus, persistent labels, headings/landmarks, non-color states and meaningful live announcements.
- Text contrast and essential control boundaries meet intended requirements; decorative pale rules are not sole boundaries.
- Reflow and text resizing work; reduced motion respected; no autoplay or drag-only functionality.
- Decorative plates/icons have empty alt; meaningful photos/product media have useful context-appropriate alt text.

## Performance and resilience

- Responsive image candidates, accurate sizes, width/height; main image prioritized, below-fold media lazy.
- No full-page mockup PNG shipped as the site; no upload of all masters indiscriminately.
- V3 internal media budgets checked. Field targets: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1 at 75th percentile, measured separately for phone/desktop. These are [Web Vitals targets](https://web.dev/articles/vitals), not measured package results.
- JS failure leaves essential links/forms usable. No blank search/grid during failed refresh.
- Build/theme check passes; visual and purchase checks run on actual draft after deployment.

## Release

- Commit and push source before updating existing Shopify draft `189659021621`.
- Follow root AGENTS.md; never publish live or create another draft without instruction.
- Report tested routes/states, missing inputs, current commit and draft preview after an actual release.

## Cart expansion — 3.1

- Execute [C01–C22](cart-scenarios.md) for both drawer and full page, at desktop and phone widths.
- Verify visual recommendation photos, actual prices, eligibility, option choice and Add to bag.
- Observe successful enhanced adds/edits/removal without a document reload or navigation.
- Test duplicate clicks, overlapping mutations, stock conflicts, section-render failure and uncertain writes without duplicating products.
- Record real implementation evidence in the [development tracker](../manifests/development-roadmap.json); generated states do not prove behavior.
