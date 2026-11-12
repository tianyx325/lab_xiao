# 内容字段契约（可复用）

实体结构、主键/外键与关联关系见 [`DATA-MODEL.md`](DATA-MODEL.md)；本文件管逐字段怎么填。

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
| research | 建议 | 外键数组，取 `content/research/` 目录名；**非必填**；卡片"研究方向"文字由方向页标题自动派生，缺省时解析 bio |
| enroll_year | 建议 | 入学年份（研究生填，如 2025）；lint 每年自动核对学籍与分组 |
| personal_url | 可选 | 个人主页 / GitHub |
| destination | 可选 | 毕业去向，仅毕业生填（如「华为 · 算法工程师」） |
| bio | 可选 | 短简介；无 `research` 时从「研究方向为…」解析展示 |
| email / social | 可选 | 邮箱；social 只放 GitHub/Scholar 等真实社交链接（mailto 由 email 派生，勿重复） |

已废弃（lint 会提醒删除）：`research_focus`（由 research[] 派生）、`organizations`（默认取 `params.lab.org_name`，仅 admin 保留）、`highlight_name`。

新建：`hugo new authors/zhang-san/_index.md`（需 archetype 可用）。

## 作者 ID

- 实验室成员：写 `content/authors/<slug>` 的 slug（如 `admin`、`su-haonan`）
- 显示名 / 英文名映射见 `data/lab_author_aliases.yaml`（解析链接用）
- 外协可写中文或英文全名；站点**不启用** authors taxonomy，避免孤儿 `/author/` 页

## 论文 `content/publication/<slug>/index.md`

| 字段 | 必填 | 说明 |
|------|------|------|
| title | 是 | 英文原题 |
| authors | 是 | 成员填 slug，外协填姓名全名（双轨制见 DATA-MODEL） |
| date | 是 | 发表日期；列表年份筛选依赖 |
| publication_types | 是 | 枚举：article-journal / paper-conference / preprint / report / thesis |
| publication / publication_short | 是 / 建议 | 期刊会议全称 / 简称（卡片角标用简称） |
| doi / url_pdf / url_html | 可选 | 链接三件套 |
| volume / pages | 可选 | 卷期页码（BibTeX 导出依赖） |
| summary | 建议 | 中文摘要，列表卡片展示 |
| abstract | 可选 | 英文摘要 |
| ccf | 可选 | CCF 等级 A/B/C，卡片角标 |
| paper_award | 可选 | 论文获奖名（如 Best Paper Honorable Mention） |
| url_code | 可选 | 开源代码仓库 |
| featured | 是（默认 false） | 首页精选开关 |
| research | 建议 | 外键数组，取 `content/research/` 目录名（agent / low-light / depth / action）；方向筛选依赖 |

已废弃：`publishDate`（与 date 冗余）。

方向外键已批量补齐（一次性迁移，脚本用毕即删）；新内容走 archetype 与 CMS 表单兜底。

## 奖项 `content/award/<slug>/index.md`

| 字段 | 说明 |
|------|------|
| authors | 获奖人（成员用 slug） |
| date | 获奖日期；**唯一日期字段**，列表年份取此 |
| level | 枚举：national（国家级）/ provincial（省部级）/ university（校级）/ society（学会/行业） |
| rank | 可选枚举：special / first / second / third / excellent |
| tags | 仅主题词；级别与等级由 level/rank 表达，勿再填 |
| summary | 列表摘要 |

已废弃：`award_date`（与 date 强制同步的冗余字段）。

## 项目 `content/project/<slug>/index.md`

| 字段 | 说明 |
|------|------|
| project_code | 课题号；**纵向项目必填**，横向/定制项目可缺省（slug 即自然键） |
| project_type | 枚举：vertical（纵向）/ horizontal（横向） |
| funding | 资助类别全称（纵向填，如「国家自然科学基金面上项目」）；卡片角标读取 |
| project_status | `ongoing` / `completed` |
| tags | 仅主题词；资助类型已由 funding 表达，勿再填 |
| summary | 列表摘要 |

## 专利 `content/patent/<slug>/index.md`

| 字段 | 说明 |
|------|------|
| authors | 发明人（成员用 slug；外协可用中文名） |
| patent_number | 如 ZL…，导入 slug 依据 |
| patent_type | 枚举：invention / utility / design（默认 invention） |
| patent_status | `granted` → 卡片「已授权」 |
| tags | 仅主题词；类型与状态由 patent_type/patent_status 表达，勿再填 |
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

py -3 scripts/sync_lab_identity.py [--dry-run]
py -3 scripts/lint_content.py [--quiet]
```

`lint_content.py` 校验数据模型（主键/外键/枚举/一致性），退出码非 0 表示存在错误，建议提交前或 CI 运行。
