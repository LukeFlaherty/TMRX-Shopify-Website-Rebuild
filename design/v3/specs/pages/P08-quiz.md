# P08 — Routine quiz entry and questions

Routes: `/pages/find-your-routine`
Shopify surface: page.v3-quiz.json (proposed)
Visual references: M07
Page-owned photography: A11
Evidence: S02, S12 (see [source ledger](../../research/sources.md)).

## Purpose

Support simple product discovery without asking for sensitive health details.

## Content and section order

### 1. Entry

A routine built around you.; brief description, start action and broad browse alternative. A11 owns the routine flat lay.

### 2. Questions

Three questions: primary goal, preferred format, daily routine context. One question at a time, radio group, progress 1 of 3, Back/Continue.

### 3. Trust and exit

Short product-discovery explanation; no diagnosis, symptom scoring or required email. Simplified footer, no newsletter inside the question flow.

## Responsive composition

**Desktop:** Image/context left, question right. Answer rows at least 52px tall.

**Phone:** Compact context, progress and question then full-width answer rows. Decorative photo can be reduced or omitted after entry.

## Data contract

Reviewed goal/format options and eligibility model; use disabled fixture only for shape, not production.

## Required states

- entry
- unselected
- selected
- validation
- back
- calculating
- configuration missing

## Page-specific acceptance

- No health, medication or email gate is added.
- Back preserves answers and focus moves to current question.
- Unreviewed rules fall back to browse links rather than fake recommendations.

## Implementation dependencies

Use the new V3 components in [components and states](../components-and-states.md), [spacing and type](../design-system.md), and [responsive rules](../responsive.md). Resolve asset IDs through [the manifest](../../manifests/assets.json) and product media through [product sources](../../manifests/products.json). Written specifications and runtime Shopify data override generated image text. Merchant-dependent launch decisions are listed in [the readiness register](../../DECISIONS.md).

## Preferred product-included photography — revision 3.1

Use these finished product-filled variants by default. Original plates remain alternate source material. Products are already present: do not overlay a second packshot. Verify visible packaging against current authentic source media before launch.

| Preferred asset | Original slot/source | Product identity |
|---|---|---|
| A21 | A11 | essential-aminos, true-omega |

## Development lookup

Use the [development roadmap](../../DEVELOPMENT-ROADMAP.md) and filter [task records](../../manifests/development-roadmap.json) by `page_ids` containing `P08`. This brief specifies design; task status and implementation evidence live in the tracker.
