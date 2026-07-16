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

Use the pinned environment so updates go to the same draft theme:

```bash
npm run theme:push
```

Do not use `--unpublished` for normal updates, because that creates a new Shopify draft theme.

Recommended update loop:

1. Edit the theme locally.
2. Commit the change to Git.
3. Push to GitHub.
4. Run `npm run theme:push` to update the existing Shopify draft.
