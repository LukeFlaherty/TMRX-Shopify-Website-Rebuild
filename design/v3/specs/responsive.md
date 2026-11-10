# Responsive composition and spacing

## Breakpoints and review widths

Phone: 0–767px. Tablet: 768–1023px. Desktop: 1024px+. Test 320, 360, 390, 430, 768, 1024, 1280 and 1440 CSS pixels; also 200% text zoom and 400% browser zoom. These are V3 implementation choices, not Shopify constraints.

| Region | Phone | Tablet | Desktop |
|---|---|---|---|
| Header | Hamburger, logo, search, bag; 44px targets | Same until nav fits without collision | Full nav and account action |
| Hero | Heading/copy/actions, then own mobile plate | Stacked or balanced split when readable | Copy left, stone/media right |
| Category switcher | Visible selected item; overflow rail + arrows or wrapping | Same behavior, more items visible | Underlined horizontal tabs/links |
| Homepage featured items | One full item plus next peek; controls | 2–3 items | 3–4 open items |
| Collection products | 2 columns, 16px column gap; natural wrapping | 2–3 columns | 3 columns with filter sidebar |
| Filters | Closed by default; labeled Filter and Sort controls | Drawer or sidebar according to width | 220–240px sidebar |
| PDP | Gallery → title/price → choices → add action | Gallery and buy box stack when tight | 55/45 gallery/buy box |
| Standards/story | Full image → heading → icon rows | Stacked until copy has adequate width | Editorial split |
| Related products | 2 open columns or controlled carousel | 2–3 columns | 3 columns |
| Journal | One featured story, latest stories as rows | 2 columns | Featured split + 2–3 columns |
| Article | Contents disclosure then body | Body max measure; optional sidebar | Narrow contents sidebar + reading column |
| Footer | Newsletter fields stack; link accordions | 2-column link groups | Logo + 3 link columns |

## Full-page mockup caveat

Generated reference PNGs are compressed visual representations, not screenshots from an implementation. Their raster widths do not define CSS viewport widths. Use the phone composition specifications even if a generated image contains a desktop-looking lower block. Do not implement tiny text to fit an arbitrary PNG height.

## Phone spacing acceptance

From the first featured product row through the footer, inspect every heading and boundary. Keep 16px before the first content after a heading, 12px between caption/price/action groups and roughly 36–40px between major sections. Consecutive sections should feel connected. Avoid 80–120px empty phone bands. Body text remains at least 16px, controls remain usable, and long product titles cannot collide with prices or the next row.

## Overlays

Mobile menu and filter drawer occupy the screen width with a clear close control, scrollable interior and safe-area bottom padding. Focus stays in the active modal, the background becomes inert, Escape closes, and focus returns to the opener. On phone, cart drawer may become a full-height sheet. Essential purchase controls cannot be hidden under a sticky element or virtual keyboard. Use `100dvh` with an appropriate fallback and account for safe-area insets.

## Loading and state restoration

Reserve intrinsic image sizes to avoid layout jumps. Keep the user's applied filters, query, sort and pagination in URL-backed state where supported. Returning from a PDP restores browsing context. Loading does not replace the entire grid with a blank white page. A failed request leaves the old results visible, adds a clear retry message and preserves controls.
