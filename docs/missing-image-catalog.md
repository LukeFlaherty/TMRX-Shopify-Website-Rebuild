# Missing Image Catalog

Working catalog for the red placeholder boxes that still need finished creative assets. These placeholders use `.tmrx-placeholder-media` today.

## Highest Priority

### PDP Benefit Cards

Location: `sections/main-product.liquid`

These appear in the PDP section after the buy box and before Key Ingredients. They are currently intentionally red placeholders.

1. Support Daily Performance
   - Current copy: "Purposeful nutrition support for training days, busy schedules, and consistent routines."
   - Needed asset: lifestyle image showing daily supplement use or an active daily routine.

2. Promote Recovery
   - Current copy: "Designed to help you stay steady between workouts and come back ready for the next session."
   - Needed asset: recovery-focused lifestyle image, stretching, post-workout cooldown, or wellness routine.

3. Fit a Clean Routine
   - Current copy: "Made for customers who want simple formulas without unnecessary fillers or artificial additives."
   - Needed asset: clean kitchen/counter supplement routine or ingredient-forward scene.

4. Support Long-Term Wellness
   - Current copy: "Built to pair with nutrition, hydration, movement, and practitioner-guided health goals."
   - Needed asset: wellness/longevity scene with hydration, movement, or practitioner-grade health cues.

## Homepage / Global Sections

### Home Hero

Location: `sections/tmrx-blank-home.liquid`

- Red fallback appears when no hero image is selected in Shopify customizer.
- Needed asset: first-viewport brand/product image that communicates practitioner-grade supplements and clean performance support.

### Shop By Goal Cards

Location: `sections/tmrx-shop-by-goal.liquid`

These are editable image picker blocks, but need default creative for the launch build.

1. Daily Protein
   - Needed asset: protein supplement routine, shaker, clean nutrition.

2. Strength & Performance
   - Needed asset: training/performance visual with supplement support.

3. Calm & Recovery
   - Needed asset: recovery, rest, calm evening routine, or low-stress wellness cue.

4. Foundational Wellness
   - Needed asset: daily health/wellness scene, morning routine, or supplement stack.

### Clean Standards

Location: `sections/tmrx-clean-standards.liquid`

- Red fallback appears when no section image is selected.
- Needed asset: clean ingredients / transparent-label standards image.

### Quiz CTA

Location: `sections/tmrx-quiz-cta.liquid`

- Red fallback appears when no section image is selected.
- Needed asset: personalized supplement stack or quiz/routine visual.

## Navigation And Cart Fallbacks

### Mega Menu Highlight Cards

Location: `snippets/tmrx-mega-products.liquid`

- One red placeholder highlight image per mega-menu category.
- Needed assets: compact category highlight images for Recovery, Improve Performance, and Health & Wellness.

### Empty Cart Category Tiles

Location: `sections/tmrx-cart-drawer.liquid`

- Red placeholders appear in the empty cart drawer category tiles.
- Needed assets: small tile images for Best Sellers, Protein, Build Muscle, and Health.

## Lower Priority Data Fallbacks

These only show red if Shopify content is missing and do not need bespoke generated art unless we want branded fallback assets.

- Product card image fallback: `snippets/tmrx-product-card.liquid`
- Supplement card image fallback: `snippets/tmrx-supplement-card.liquid`
- Stack card product image fallback: `snippets/tmrx-stack-card.liquid`
- Mega-menu product image fallback: `snippets/tmrx-mega-products.liquid`
- Mobile menu product image fallback: `snippets/tmrx-mobile-menu-group.liquid`
- Cart line item/recommendation image fallback: `sections/tmrx-cart-drawer.liquid`
- PDP gallery/product image fallback: `sections/main-product.liquid`
- Review modal product image fallback: `sections/main-product.liquid`
