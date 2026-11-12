# V3 development roadmap

Revision 3.1.0 · November 12, 2026 · **Planning only: implementation has not started.**

## Version boundaries

| Version | Meaning | Treatment |
|---|---|---|
| V1 | Currently live storefront | Keep live and recoverable; do not modify or publish as part of this package update |
| V2 | Partial unpublished draft already in Shopify, theme `189659021621` | Capture its actual state and a restoration checkpoint before V3 implementation |
| V3 | Approved new redesign | Build fresh components in controlled iterations; package revision 3.1 is still V3 |

The review target remains the existing unpublished draft. Do not create another draft just to label the work V3. V2 is a baseline and recovery source, not a mandate to copy its layouts or fabricated fallbacks. V1 stays live until an explicit publish instruction.

## Working method

Choose **one to three related tasks** whose dependencies are satisfied. Read their page briefs, asset mappings and acceptance checks first. Implement a small useful slice, run relevant checks, record evidence, update status and commit. For deployable theme work, push GitHub before updating the existing draft and then verify the preview. Package-only changes do not deploy to Shopify.

The [machine-readable tracker](manifests/development-roadmap.json) contains **92 stable task IDs across 13 phases**, dependencies, page mappings, proposed file targets, inputs and acceptance conditions. The [detailed task list](development/tasks.md) includes every item; the [iteration log](development/iteration-log.md) carries progress between development chats. All tasks start as planned. Creating the package does not mark development complete.

A phase organizes work; its explicit task dependencies determine order. Independent eligible work may proceed while merchant inputs are pending. Conditional programs must be implemented or deliberately verified in their disabled state. No estimate or percentage-complete claim is implied.

## Phase map

| Phase | Work | Exit condition |
|---|---|---|
| R00 | Baseline, V1 protection and V2 recovery | Live target protected; actual V2 snapshot and restoration checkpoint exist |
| R01 | Catalog, content and media | All SKUs, options, labels, asset slots and merchant inputs have sources |
| R02 | New V3 foundation and shell | Tokens, primitives, navigation, overlays and footer work responsively |
| R03 | Shop, categories, filters and search | Actual products can be found and compared without losing context |
| R04 | PDP and 16 individual SKU checks | Every product has correct media, content, purchase states and format behavior |
| R05 | Shared cart engine, drawer, page and recommendations | Adds/edits/removal reconcile without reload; both surfaces agree |
| R06 | Homepage and product-led imagery | Approved A direction, working category swapper and moderate spacing |
| R07 | Quiz and results | Reviewed matching or honest browse fallback; no email gate or medical scoring |
| R08 | Journal and articles | Approved native content, comfortable reading and distinct imagery |
| R09 | Brand, support, FAQ, policies and wholesale | Useful real content and connected forms; unresolved inputs are explicit |
| R10 | Accounts, subscriptions and checkout | Actual Shopify capabilities verified; unavailable programs safely hidden |
| R11 | Whole-store acceptance | Responsive, functional, content, accessibility and performance evidence recorded |
| R12 | Draft review and launch handoff | Source and preview agree; live publishing waits for explicit instruction |

## Suggested first iterations

1. **Protect the baseline:** D001–D004. Confirm version identities, preserve V2, establish the implementation branch and checks.
2. **Verify data and media:** D010–D012 and D014; record inputs for D013/D015/D016. Select product-filled artwork before wiring the hero.
3. **Create the new shell:** D020–D025 in small batches. Review real phone widths rather than copying a PNG height.
4. **Complete a shopping slice:** product item → shop → one PDP → shared cart client → drawer/page → recommendation add. Use real data before polishing the homepage.
5. **Expand through the registry:** remaining SKUs, discovery, editorial and support. Every one of the 22 page/surface briefs is mapped to tasks.
6. **Review and release:** complete evidence and merchant decisions, update only the existing draft, obtain acceptance and await a separate live-publish instruction.

## Cart requirements

R05 is a complete subsystem. Drawer and standalone page both have visual recommendations with real images, prices, variant selection and Add to bag controls. Successful enhanced mutations keep the same URL and update the cart lines, count, totals and recommendation pool together. The normal cart form is the no-JS fallback. See [cart interaction requirements](specs/cart-experience.md) and [cart test scenarios](qa/cart-scenarios.md).

## Definition of verified

Acceptance is demonstrated on the actual implementation, relevant checks pass, evidence is recorded, and a Git commit identifies the result. A deployed checkpoint also has a verified draft preview. A generated mockup is not functional evidence. Statuses are planned, in_progress, needs_input, verified and deferred. A deferral needs a recorded reason and review decision.

## Deployment and recovery

Follow root AGENTS.md: review/check → commit → push GitHub → `npm run theme:push` to `189659021621` → verify `https://true-matrix.myshopify.com?preview_theme_id=189659021621`. Preserve the actual V2 draft before the first V3 push. Subsequent iterations each have a recoverable source checkpoint. Completing this roadmap does not authorize live publishing.
