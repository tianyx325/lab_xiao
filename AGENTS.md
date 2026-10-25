# AGENTS.md

## Project Overview

Academic research lab site (智能感知与决策实验室) built with Hugo + HugoBlox (blox-bootstrap v5). Content is Markdown in `content/`, theme uses SCSS in `assets/scss/`. Deployed to GitHub Pages via `gh-pages` branch.

## Build Commands

- Dev server: `hugo server -D`
- Production build: `hugo --minify`
- Always verify zero warnings after changes.

## Directory Structure

- `content/` — Markdown content by section: `publication/`, `patent/`, `award/`, `project/`, `research/`, `post/`, `authors/`
- `modules/lab-ui/layouts/` — Custom Hugo templates. Override the vendor theme.
- `assets/scss/template.scss` — Main stylesheet. All style changes go here.
- `assets/scss/lab/_tokens.scss` — Sole design-token source (`$lab-*` / `--lab-*`).
- `assets/scss/lab/_type.scss` — Typography mixins (display/section titles).
- `data/fonts/lab.toml` — Inter + Noto Sans SC (`appearance.font: lab`).
- `config/_default/` — Hugo config split into `hugo.yaml`, `params.yaml`, `languages.yaml`, `menus.yaml`, `module.yaml`.

## Constraints

- **Do NOT modify `_vendor/` directory.** It's managed by Hugo Modules. Override by placing files in `modules/lab-ui/layouts/` with matching paths.
- **Do NOT add JavaScript framework dependencies.** This is a Hugo static site; use vanilla JS or Hugo Pipes.
- **All color/spacing values must use design tokens** (CSS custom properties `--lab-*` or SCSS variables `$lab-*`). Never hardcode raw values.
- **Chinese is the primary language.** Content and UI labels are in Chinese.

## Theme Architecture

- Hugo Modules manage the base theme (`blox-bootstrap/v5`). Custom overrides live in `modules/lab-ui/`.
- Template lookup: `modules/lab-ui/layouts/<section>/single.html` for detail pages, `section/<name>.html` for list pages, `_default/list.html` as fallback.
- Shared partials in `modules/lab-ui/layouts/partials/` prefixed with `lab-` (e.g., `lab-article-shell-start.html`).
- Shortcodes in `modules/lab-ui/layouts/shortcodes/` for content-embeddable components.

## Content Types

| Section | Purpose | Key Front Matter |
|---------|---------|-----------------|
| publication | Academic papers | `publication_types`, `authors`, `abstract`, `doi` |
| patent | Patents | `authors` (inventors), `patent_number` |
| award | Awards/honors | `authors` (display), `award_date` (keep in sync with `date`) |
| project | Research projects | `external_link`, `image` |
| research | Research directions | Used for overview cards |
| post | News/blog posts | `authors`, `tags`, `categories` |

## SCSS Conventions

- Design tokens: define in `assets/scss/lab/_tokens.scss` only. Prefer `var(--lab-*)` in rules; use `$lab-*` for Sass math / maps.
- Do not hardcode brand hex/rgba in `template.scss` — add a token, then reference it.
- Brand purple (`$lab-blue`) is accent-only (links, active, focus); page atmosphere stays neutral.
- Display/section titles: medium weight (`$lab-weight-display` / `$lab-weight-heading`) + tight tracking; use mixins from `_type.scss`.
- Prefer quiet academic motion (color/opacity); avoid glow shadows and layout-shifting font-weight toggles.
