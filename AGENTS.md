# AGENTS.md

## Project Overview

Academic research lab site (智能感知与决策实验室) built with Hugo + HugoBlox (blox-bootstrap v5). Content is Markdown in `content/`, theme uses SCSS in `assets/scss/`. Deployed to GitHub Pages via `gh-pages` branch.

## Build Commands

- Dev server: `hugo server -D`
- Production build: `hugo --minify`
- Always verify zero warnings after changes.

## Directory Structure

- `content/` — Markdown content by section: `publication/`, `patent/`, `award/`, `project/`, `research/`, `post/`, `authors/`
- `modules/lab-ui/layouts/` — Custom Hugo templates (44 files). Override the vendor theme.
- `assets/scss/template.scss` — Main stylesheet (~3400 lines). All style changes go here.
- `assets/scss/lab/` — Additional SCSS partials imported by template.scss.
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
| patent | Patents | `inventors`, `patent_number` |
| award | Awards/honors | `recipients`, `award_date` |
| project | Research projects | `external_link`, `image` |
| research | Research directions | Used for overview cards |
| post | News/blog posts | `authors`, `tags`, `categories` |

## SCSS Conventions

- Design tokens: CSS custom properties (`--lab-*`) in `:root`, SCSS variables (`$lab-*`) for breakpoints and loop computation only.
- Three-tier token system: primitives (`--color-blue-500`) → semantic (`--color-text-link`) → component (`--card-bg`).
- Card accent colors generated via `@each` + Sass maps, not manual blocks.
- Use `@layer` for specificity management: `reset, base, layout, components, utilities`.
