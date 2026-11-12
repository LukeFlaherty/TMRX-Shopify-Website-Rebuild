# Project Instructions

## V3 Redesign Design Lookup

- For V3 design/build requests, start with `design/v3/README.md` and `design/v3/BUILDER-HANDOFF.md`.
- Use `design/v3/DEVELOPMENT-ROADMAP.md` and its task registry for iterative development; record actual acceptance evidence in `design/v3/development/iteration-log.md`. V1 is live, V2 is the existing partial draft, and V3 is the redesign. Preserve V2 before the first V3 theme update.
- Look up the requested route in `design/v3/manifests/pages.json`, then read its individual page specification before implementation.
- Written V3 specifications, tokens and current Shopify data override generated screenshot text. Resolve images through the asset/product manifests; do not invent prices, reviews, labels, claims or subscription offers.
- Use new V3 creative and new V3 theme components. Only authentic logo/product source media are the documented identity exceptions; page-specific editorial photography must not be recycled as filler.
- V3 spacing should be relaxed but compact, especially halfway down the page: follow the explicit responsive spacing tokens.
- Prefer the product-filled assets in each page's `preferred_asset_ids`; do not overlay products again. For cart work read `design/v3/specs/cart-experience.md`: both drawer and full cart page need visual recommendations and variant-aware enhanced adds that update without reloading.
- The V3 package is a design handoff, not a deployed theme. Documentation/asset-package changes alone do not require a Shopify push; real deployable theme changes follow the workflow below.

## Email Marketing Memory

- Before creating True Matrx email marketing graphics, read `docs/email-marketing/README.md` for saved user preferences and prior email references.
- Use the archived emails as inspiration, not as layouts or copy to duplicate.
- The user prefers a white background with subtle light-blue background decals; avoid boxes or rounded cards around individual product sections.

## Source of Truth

- This GitHub repository is the source of truth for the Shopify rebuild theme.
- Keep the repository up to date with versioned changes.
- Commit meaningful checkpoints before pushing changes to Shopify.
- Push source changes to GitHub whenever the draft Shopify theme is updated.

## Shopify Draft Target

- Use the `draft` Shopify CLI environment in `shopify.theme.toml`.
- The `draft` environment targets the existing unpublished Shopify theme `TMRX Blank Rebuild Draft` (theme ID `189659021621`).
- Update the existing draft with `npm run theme:push`.
- Do not use `--unpublished` for normal updates, because that creates a new Shopify draft theme.
- Do not publish the Shopify theme over the live storefront unless explicitly requested.

## Deployment Workflow

For every deployable change:

1. Edit the theme locally.
2. Review the diff and run relevant checks when available.
3. Commit the change to Git with a clear message.
4. Push the commit to GitHub.
5. Run `npm run theme:push` from the repo root to update the existing unpublished Shopify draft.
6. Share the preview URL: `https://true-matrix.myshopify.com?preview_theme_id=189659021621`.

Use `npm run theme:info` to verify the CLI is still pinned to theme `189659021621` before pushing if there is any doubt.
