# Project Instructions

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
