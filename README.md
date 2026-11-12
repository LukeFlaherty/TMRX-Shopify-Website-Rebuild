# TMRX Blank Rebuild Draft

## V3 redesign package

The current redesign direction and builder handoff are in [design/v3/README.md](design/v3/README.md). Start there for V3 page specifications, fresh photography, desktop/mobile references, data contracts and route-to-asset lookup. Open [the local visual catalog](design/v3/index.html) to browse the package. This package does not deploy or replace the current theme.

Revision 3.1 adds product-filled B-roll, full cart page/drawer references and a [92-task development roadmap](design/v3/DEVELOPMENT-ROADMAP.md). V1 is the live store, V2 is the partial existing draft, and V3 is the new redesign.

Blank Shopify Online Store 2.0 theme foundation for rebuilding the True Matrx website.

This is intended to be uploaded or pushed as an unpublished/draft theme only. Do not publish it over the current live theme until the rebuild is complete and reviewed.

## Structure

- `layout/theme.liquid` - global HTML shell.
- `templates/*.json` - Online Store 2.0 templates.
- `sections/tmrx-blank-home.liquid` - empty homepage starting point.
- `assets/tmrx-base.css` - tiny reset and blank workspace styles.

## Next Step

When V3 implementation is requested, begin with roadmap D001–D004 to protect V1 and preserve the actual V2 draft. Build new V3 components from the page briefs and tokens, then progress through eligible task batches with recorded checks and source checkpoints.

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
