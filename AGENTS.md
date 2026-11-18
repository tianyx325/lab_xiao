# AGENTS.md

## Project Overview

Academic research lab site (智能感知与决策实验室) built with Hugo + HugoBlox (blox-bootstrap v5). Content is Markdown in `content/`; the theme lives at the repository root (`layouts/`, `assets/scss/`, `assets/js/`). Deployed to GitHub Pages via `gh-pages` branch.

## Build Commands

- Requires **Hugo 0.168 extended** and **Dart Sass** on `PATH` (standalone or `sass-embedded`; the plain `sass` npm package is pure JS and cannot speak the embedded protocol Hugo needs). CI installs it via `scripts/install-dart-sass.sh`.
- `hugo mod get/vendor/tidy` require a Go toolchain.
- Dev server: `.\scripts\dev.ps1`
- Production build: `hugo --gc --minify --noBuildLock`
- SCSS lint: `npm ci && npm run lint:css` (stylelint, correctness rules only)
- Performance budget: `python scripts/check_budget.py` (run after `hugo --minify`)
- Always verify zero warnings after changes. Known exception: blox-seo v0.3.1 ships a misplaced `sitemap.xml`, which Hugo 0.168 skips with one warning; do not hand-patch `_vendor`.

## Directory Structure

结构见 `content/`、`layouts/`、`assets/`、`config/`、`scripts/`。

## Constraints

- **Do NOT modify `_vendor/` directory.** It's managed by Hugo Modules. Override by placing files in `layouts/` with matching paths.
- **Do NOT add JavaScript framework dependencies.** This is a Hugo static site; use vanilla JS or Hugo Pipes.
- **All color/spacing values must use design tokens** (CSS custom properties `--lab-*` or SCSS variables `$lab-*`). Never hardcode raw values.
- **Chinese is the primary language.** Content and UI labels are in Chinese.
- **Browser baseline:** latest two versions of Chrome, Edge, Firefox and Safari. Modern CSS (`:has()`, `color-mix()`, `dvh`) may be used without fallbacks; revisit if the baseline changes.

## Theme Architecture

- Hugo Modules manage the base theme (`blox-bootstrap/v5`); site overrides live at the repository root.
- Template lookup: `layouts/<section>/single.html` for detail pages, `section/<name>.html` for list pages, `_default/list.html` as fallback.
- Shared partials in `layouts/partials/`, grouped by domain: `components/`, `listing/`, `article/`; vendor-override files keep their original top-level names.
- Shortcodes in `layouts/shortcodes/` for content-embeddable components.
- Lab JS: `assets/js/lab/lab-*.js`, loaded by `partials/custom_js.html`. `wowchemy-map.js` stays in `assets/js/`. Site `assets/media/` is logo/icon only.

## Content Types

| Section | Purpose | Key Front Matter |
|---------|---------|-----------------|
| publication | Academic papers | `publication_types`, `authors`, `abstract`, `doi` |
| outcomes | Outputs hub. Keep `type: publications` and `url: /publications/` so the public URL and hub layout stay put | `type`, `url` |
| patent | Patents | `authors` (inventors), `patent_number` |
| award | Awards/honors | `authors` (display), `level`, `rank` |
| project | Research projects | `project_type`, `funding`, `url_external`, `image` |
| research | Research directions | Used for overview cards |
| post | News/blog posts | `authors`, `tags`, `categories` |

## SCSS Conventions

- Design tokens: define in `assets/scss/lab/_tokens.scss` only. Prefer `var(--lab-*)` in rules; use `$lab-*` for Sass math / maps.
- `template.scss` import order is the cascade order. Do not reorder. View layers are `lab/views/{results,people,pages,home,listing}/`.
- Do not hardcode brand hex/rgba in view stylesheets — add a token, then reference it.
- Brand accent is Brand blue `#4176E6` (user-specified) (SCSS name `$lab-blue`, kept for legacy reasons) — interaction only: buttons, active, focus, hover borders. Body links inherit the same accent; page is `#F2FAFF` (user-specified) with white cards `#FDFEFF`. Ink is blue-tinted `#1E232C`; borders are ink-alpha (`rgba(30,35,44,.14)`), never standalone grays. Dark mode is near-black `#0A0A0A` with lifted blue `#6C9CF2` links. No gradients, no glow — premium comes from ink quality and whitespace (reference: deepseek.com `--ds-color-*` tokens).
- Color contrast (WCAG 2.1 AA) baseline: body text ≥4.5:1, large/incidental text and non-text UI (focus ring) ≥3:1 — verified pairs live in `scripts/check_contrast.py` (run after ANY `_tokens.scss` change). USER RULE: no blue may be deeper than the primary #4176E6 — body links/buttons sit ON the primary (4.19:1 / white-on-primary 4.23:1, user-approved AA exceptions); hover and link-soft LIGHTEN via white color-mix, never deepen toward ink. `--lab-color-text-faint` (.28) is decorative-only; information-bearing de-emphasis uses `--lab-color-text-tertiary` or muted.
- Display/section titles: medium weight (`$lab-weight-display` / `$lab-weight-heading`) + tight tracking; use mixins from `_type.scss`.
- Spacing: 8px base scale (`$lab-space-1..9` = 4/8/12/16/24/32/40/48/64) is the ONLY allowed set. Every margin/padding/gap must resolve to a `$lab-space-*` token or a semantic alias (`$lab-space-inline/stack/block/section/section-sm`); never write raw rem/px. 4px is a half-step for tight component internals only; sub-4px px tweaks are permitted. Exceptions require a comment and should be rare (current: two >4rem section offsets).
- Typography: the `$lab-text-*` steps are the complete scale — never introduce new font sizes. Text roles are mixins in `_type.scss` (`lab-type-caption` / `lab-type-ui` / `lab-type-body` / `lab-type-lead` + title mixins); components consume roles, not raw steps. Body = 16px / 1.75 leading (CJK-optimal). Reading columns: `$lab-read-width-detail` = 42rem ≈ 42 CJK chars/line (WCAG CJK advisory ≤40); `$lab-read-width` = 52rem for list rows.
- Prefer quiet academic motion (color/opacity); avoid glow shadows and layout-shifting font-weight toggles.
