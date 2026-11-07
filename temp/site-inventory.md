# Docs site inventory (Thread D, round 2, 2026-11-08)

Measured on a clean worktree of `origin/main` (419be0a9) with mkdocs 1.6.1, Material 9.8.1: `mkdocs build --strict` (49 s, 16 GB limit).

| Finding | Number |
|---------|--------|
| Markdown pages (`en/` 1423, `de/` 1631) | 3054 |
| Pages not in `nav` (never reachable by menu) | 2148 (en 975, de 1173) |
| Hand-written `nav` entries (mkdocs.yml, 1238 lines) | 96 |
| Nav entries whose title is the path (`de/programs/apps/wiki/`) | 87 |
| Top-level menu entries | 71 (de/en mixed, no order) |
| Strict-mode warnings (all dead links) | 102 |
| `docs/index.md` (site root) | missing |
| `theme.language` | `de`, although `en/` is the source |
| Palette / font | Material default (indigo, Roboto) |

Dead links: all generated index pages that point at `latest/description.md` or `index.md` of frontends that do not exist:
`en/programs/platform/desktop/frontends` (24), `suites/workflows|marketplace|erp|crm/frontends` (12 each),
`platform/desktop` (12), `suites/workflows|erp|crm` (6 each). Cause: `scripts/gen_frontend_indexes.py` lists frontends
that are not on disk (to be fixed in step 5).

Cause of the broken menu: nav is written by hand, one entry per program and language side by side, instead of
following the folders; new pages were never added.
