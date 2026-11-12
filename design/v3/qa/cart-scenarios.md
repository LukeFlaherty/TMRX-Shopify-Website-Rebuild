# Cart implementation scenario matrix

Future functional tests; none has run against a V3 implementation yet. Save actual evidence in the iteration log and mark roadmap D050–D060 verified only when appropriate.

| ID | Trigger | Expected outcome | Evidence |
|---|---|---|---|
| C01 | Add a single-variant recommendation in drawer | Same URL, drawer remains open, one correct line added, count/totals/candidates refreshed | Before/after cart JSON; request; DOM; no document navigation |
| C02 | Add from full cart page | Remain on `/cart`; update in place, no document reload | Network trace and actual cart state |
| C03 | Multi-variant recommendation | Require valid chosen options; add selected variant only | Selected ID/options and resulting line |
| C04 | Rapid double click | One deliberate add, busy state prevents duplicates | Request count and quantity |
| C05 | Add while a quantity change is pending | Serialized writes; newest cart wins | Request order, cart revision, final totals |
| C06 | Change/remove an existing line | Current line key used, all surfaces update | Server lines, header badge and displayed subtotal |
| C07 | Candidate already exists in cart | Candidate excluded rather than an accidental duplicate | Candidate pool compared with current product IDs |
| C08 | Product becomes unavailable after recommendations load | Clear local message, no false success; refresh candidates | Rejection plus reconciled server state |
| C09 | Stock cap/rejection on write | Reconcile actual resulting quantity before totals/retry | Response and follow-up cart read |
| C10 | Add succeeds but a returned section is null | Cart reconciles and targeted HTML recovers; no second add | Original write count; null section; recovered state |
| C11 | POST timeout or ambiguous outcome | No blind automatic retry; reconcile and explain unresolved uncertainty | Write/read trace and honest action state |
| C12 | Recommendations service fails | Existing cart and checkout remain usable | Error isolated to recommendation module |
| C13 | No eligible candidates | Hide module cleanly, no unrelated filler SKU | Empty pool and resulting layout |
| C14 | Add from empty page or drawer | Same surface becomes populated without reload | Empty/populated state and navigation trace |
| C15 | Remove final item | Empty message/starters replace lines; no active empty checkout | Zero-item cart plus UI |
| C16 | Change market/currency | Current money formatting and eligible options respected | Actual market context and rendered values |
| C17 | Real discount or selling-plan lines | Correct totals and distinct lines; no synthetic savings | Authoritative cart allocations and UI |
| C18 | Keyboard-only option choice/add/close | Clear focus, useful announcement, correct return target | Keyboard run and focus observations |
| C19 | Phone with safe areas/keyboard | Controls and checkout remain reachable; internal scrolling works | 320/390/430px screenshots and interactions |
| C20 | Section replacement followed by another add | No duplicate listener or stale candidate binding | Requests and resulting quantity |
| C21 | Disable JavaScript | Normal forms/links still allow purchase/editing | Real no-JS test; navigation expected for fallback |
| C22 | Close drawer during pending add, reopen | Closing does not undo or duplicate write; current state appears | Pending write and reconciled reopened cart |

Successful enhanced cart mutations must show no document navigation. Checkout and explicit View bag/Continue shopping links may navigate intentionally. Generated mockup prices and badge counts are not test fixtures for real inventory.
