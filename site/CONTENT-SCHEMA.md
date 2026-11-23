# Content schema (authoritative IA)

Entities live in **one** directory each. Hubs are shells that list those entities.

| User URL | Hub shell | Entity bundles |
|---|---|---|
| `/publications/` | `content/publications/_index.md` | `content/publications/*` |
| `/publications/patents/` | `content/publications/patents/_index.md` (`hub_section: patent`) | `content/patent/*` |
| `/publications/awards/` | `content/publications/awards/_index.md` (`hub_section: award`) | `content/award/*` |
| `/people/` | `content/people/_index.md` | `content/authors/*` |
| `/projects/` | `content/projects/_index.md` | `content/projects/*` |
| `/research/` | `content/research/_index.md` | research pages |
| `/blog/` | `content/blog/_index.md` | `content/blog/*` |
| `/contact/` | contact | — |

Retired list URLs (redirect only — do not put entities here as second source):

- `/patent/` → `/publications/patents/` (`content/patent/_index.md` layout: redirect)
- `/award/` → `/publications/awards/` (`content/award/_index.md` layout: redirect)
- `/outcomes/` → `/publications/` (alias on publications)
- `/outcomes/awards/`, `/outcomes/patents/` → hub aliases on the new hubs

## Front matter contracts

**authors/\*/_index.md**: `title`, `user_groups`, `weight` (optional: `role`, `email`, `organizations`, `superuser`)

**publications/\*/index.md**: `title`, `authors`, `date` (optional: `publication_types`, `doi`, `url_*`)

**patent/\*/index.md**: `title` (optional: `url_patent`, `url_pdf`, `date`)

**award/\*/index.md**: `title` (optional: `date`, `authors`)

**projects/\*/index.md**: `title` (optional: `authors`, `external_link`)

Validate: `npm run check:content`
