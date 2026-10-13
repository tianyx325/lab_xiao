# 内容字段契约（可复用）

换实验室或批量新增内容时，按此表填写。展示层依赖这些字段；`---` 之后的正文为自定义，脚本默认不覆盖。

## 单一配置源 `params.lab`

见 [`config/_default/params.yaml`](../config/_default/params.yaml) 的 **`lab:`** 段。

| 键 | 用途 |
|----|------|
| `name` / `name_en` | 实验室中英文名（hero、导航需 sync） |
| `org_name` / `org_url` | 学院名与链接（页脚） |
| `email` / `address` / `latitude` / `longitude` | 联系与地图 |
| `tagline` / `lead` | 首页标语与导语 |
| `seo_description` | SEO / 方向页导语默认 |
| `admit_lead` | 联系页页头导语 |
| `ui.cta_*` | 首页按钮文案 |
| `ui.people_lead` | 成员页导语；空则自动「{name}团队成员」 |
| `ui.section_leads.*` | 论文/项目/专利/奖项/动态等列表导语 |
| `admit.sections` | 联系页招生三段（title / lead / bullets / show_email） |
| `links` / `research_home_count` | 首页链接与方向卡数量 |

改完 `lab:` 后执行：

```powershell
py -3 scripts/sync_lab_identity.py
# 或预览：
py -3 scripts/sync_lab_identity.py --dry-run
```

脚本回写（勿手改这些派生字段）：

- `hugo.yaml` → `title`
- `languages.yaml` → `zh.title` / `zh.params.description`
- `params.yaml` → `marketing.seo.org_name` / `description`、`footer.copyright.notice`

主题色：`modules/lab-ui/assets/scss/lab/_tokens.scss` 的 `$lab-blue` 与 `data/themes/minimal.toml` 的 `primary` 保持一致。

## 成员 `content/authors/<slug>/_index.md`

| 字段 | 必填 | 说明 |
|------|------|------|
| title | 是 | 显示名 |
| role | 是 | 身份，如 研一 / 教授 |
| user_groups | 是 | 与 `/people/` 分组名一致：导师、博士生、研三、研二、研一、本科生、毕业生 |
| research_focus | 建议 | 研究方向短句；卡片与详情优先用此字段 |
| bio | 可选 | 短简介；无 `research_focus` 时尝试从「研究方向为…」解析 |
| organizations | 可选 | 单位 |
| email / social | 可选 | 联系方式 |

新建：`hugo new authors/zhang-san/_index.md`（需 archetype 可用）。

## 项目 `content/project/<slug>/index.md`

| 字段 | 说明 |
|------|------|
| project_code | 课题号，导入 slug 依据 |
| project_status | `ongoing` / `completed` |
| tags | 含「面上项目」「重点项目」等时卡片显示类型角标 |
| summary | 列表摘要 |

## 专利 `content/patent/<slug>/index.md`

| 字段 | 说明 |
|------|------|
| patent_number | 如 ZL…，导入 slug 依据 |
| patent_status | `granted` → 卡片「已授权」 |
| summary | 列表摘要 |

## 研究方向 `content/research/<slug>/index.md`

| 字段 | 说明 |
|------|------|
| weight | 越小越靠前；首页 `lab-research-cards` 取前 N 条 |
| summary | 卡片摘要 |

栏目 `_index.md` 的 `summary` 留空时，使用 `lab.ui.section_leads.<section>`。

## Excel 批量

```text
py -3 scripts/import_projects_patents.py --xlsx-dir <dir> --content <contentDir> [--dry-run]
py -3 scripts/sync_research_focus.py [--authors <authorsDir>]
py -3 scripts/sync_lab_identity.py [--dry-run]
```
