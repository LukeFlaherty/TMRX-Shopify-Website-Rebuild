# V3 design system

## Character

Confident, clear, relaxed everyday wellness. The blue logo and authentic black/silver containers carry brand recognition. White is the primary canvas; light blue supports section rhythm; tactile ivory stone warms product staging. Use strong black headings and restrained blue actions. Product information and actions stay prominent.

The user approved homepage A, the horizontal category swapper and natural pedestals, then asked for a small spacing increase through the middle and lower page. That feedback is a fixed V3 requirement, not an invitation to add oversized empty bands.

## Color and contrast

| Token | Value | Usage |
|---|---|---|
| `canvas` | `#FFFFFF` | Main page and product grid |
| `ink` | `#101820` | Main text and headings |
| `muted` | `#536270` | Secondary text, not disabled data |
| `action` | `#0067B8` | Primary button/link; white on blue |
| `actionHover` | `#005496` | Hover/pressed emphasis |
| `ice` | `#EDF7FE` | Quiet quiz or editorial band |
| `line` | `#C9E2F3` | Decorative separators only |
| `controlBorder` | `#708494` | Inputs/essential boundaries |
| `stone` | `#ECE3D6` | Photography cue; not a grid-card fill |
| `error` | `#A3212D` | Error text/icon plus explicit wording |
| `focus` | `#003F73` | 3px outline with 3px offset |

Contrast is measured by the package tooling for relevant pairs. Do not use faint decorative blue rules as the only indication of an input or selection. A selected category has an underline plus selected semantics; an error has a message, not red alone. [WCAG contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## Type

Use the existing system sans stack as the initial implementation baseline: `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. Inter is a preference, not a bundled licensed font file. If a webfont is selected later, acquire the proper font/license, use a limited set of weights and verify loading/CLS. Do not invent a font asset entry.

| Style | Phone | Tablet | Desktop | Weight / leading |
|---|---|---|---|---|
| Hero h1 | 34px | 42px | 56px | 750–800 / 1.08 |
| Inner-page h1 | 32px | 38px | 48px | 750–800 / 1.12 |
| Section h2 | 26px | 30px | 36px | 750 / 1.16 |
| h3/product name | 18px | 20px | 22px | 700 / 1.25 |
| Body | 16px | 16px | 17px | 400 / 1.5 |
| Small metadata | 14px | 14px | 14px | 400–600 / 1.4 |
| Eyebrow | 12px | 12px | 13px | 700 / 1.3; mild tracking |

Long product names wrap naturally; do not shrink all product names to fit the longest. Reading measure is 60–70 characters. Avoid all-caps paragraphs. Article h2s inherit the same family; no serif exception.

## Spacing and density

Base steps: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80px. Phone gutters 20px, tablet 32px, desktop 48px, maximum container 1320px. Phone major section padding 36–40px; desktop 56–64px. Dense functional blocks such as filter toolbars may use 16–24px. The global upper bound is 80px, reserved for a deliberate hero, not every section.

Heading to content: 16px phone / 20px desktop. Copy to button: 12–16px. Product image to category/name: 12px. Name to price: 8px. Price to button: 12px. Grid row gap: 28px phone / 36px desktop. Gap between goal rows: 12px. FAQ rows at least 52px tall, with 14–16px vertical padding when wrapping. Form labels sit 8px above controls; field groups 16px apart. A button is at least 48px tall; icon controls have a 44px hit area.

Avoid cumulative margins: the boundary between two sections uses one defined section gap, not two arbitrary margins plus two paddings. Judge spacing at actual 390px width through the entire page, especially standards, how-to, FAQs, recommendations, newsletter and footer. Height expands with content; never scale the bottom half down to match a generated screenshot.

## Layout and imagery

Desktop uses a 12-column grid with 24px gutters. PDP gallery/buy box is roughly 55/45. At 768px and below, all editorial splits stack; gallery precedes buying controls. Collections are 3 columns at 1024+, 2 below; at 320px with unusually long names they may use a single-column fallback if necessary. No permanent mobile filter sidebar.

Hero product photography uses text-free background plates plus authentic product layers; see the asset recipes. Individual products remain open on white, with no rounded cards around each. A panel is justified for a quiz question, cart or form, not a blanket styling rule for all content. Background curves are decorative CSS/SVG, low contrast, and never behind dense text.

## Motion and accessibility

Small transitions 160ms, drawer 220ms, no autoplay carousel. Respect reduced motion. Carousel controls and ordinary links provide alternatives to swiping. Maintain focus order, visible focus, and true input labels. Design target is 44px interaction areas; this exceeds WCAG AA's usual 24px minimum rather than mislabeling 44px as the AA requirement. [W3C target-size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). Reflow must work at 320 CSS pixels without page-level horizontal scrolling. [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
