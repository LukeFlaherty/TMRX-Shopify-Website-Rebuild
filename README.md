# TMRX Blank Rebuild Draft

Blank Shopify Online Store 2.0 theme foundation for rebuilding the True Matrx website.

This is intended to be uploaded or pushed as an unpublished/draft theme only. Do not publish it over the current live theme until the rebuild is complete and reviewed.

## Structure

- `layout/theme.liquid` - global HTML shell.
- `templates/*.json` - Online Store 2.0 templates.
- `sections/tmrx-blank-home.liquid` - empty homepage starting point.
- `assets/tmrx-base.css` - tiny reset and blank workspace styles.

## Next Step

Start design work in `sections/tmrx-blank-home.liquid` and `assets/tmrx-base.css`, then add templates/sections as the rebuild takes shape.

## Versioned Draft Workflow

This repo is the source of truth for the Shopify rebuild. The existing unpublished Shopify draft theme is:

- Theme: `TMRX Blank Rebuild Draft`
- Theme ID: `189659021621`
- Environment: `draft`
- Preview: `https://true-matrix.myshopify.com?preview_theme_id=189659021621`

The `draft` environment is configured in `shopify.theme.toml` so Shopify CLI updates the same existing unpublished draft theme each time.

Use this command to confirm the target:

```bash
npm run theme:info
```

Use this command to deploy local source to the existing draft:

```bash
npm run theme:push
```

Do not use `--unpublished` for normal updates, because that creates a new Shopify draft theme. Do not publish to the live theme unless explicitly requested.

Recommended deployment loop:

1. Edit the theme locally.
2. Review the diff and run checks when relevant.
3. Commit the change to Git.
4. Push the commit to GitHub.
5. Run `npm run theme:push` to update Shopify draft theme `189659021621`.
6. Preview the draft at `https://true-matrix.myshopify.com?preview_theme_id=189659021621`.
