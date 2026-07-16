# Project Instructions

- Keep this Shopify theme repository up to date with versioned changes.
- Commit meaningful checkpoints before pushing changes to Shopify.
- Push source changes to GitHub whenever the draft Shopify theme is updated.
- Use the `draft` Shopify CLI environment in `shopify.theme.toml`; it targets the existing unpublished theme `TMRX Blank Rebuild Draft` (`189659021621`).
- Update the existing draft with `npm run theme:push`, not `--unpublished`, so a new Shopify draft theme is not created.
- Do not publish the Shopify theme over the live storefront unless explicitly requested.
