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
| `ui.people_lead` | 成员页导语；空则自动「{name}团队成员」 |
| `ui.section_leads.*` | 论文/项目/专利/奖项/动态等列表导语（中英文各自配置；与 `migrate_en_taxonomy.py` 词表无关） |
| `admit.sections` | 联系页招生三段（title / lead / bullets / show_email） |
| `research_home_count` | 首页研究方向卡片展示数量（默认 3） |

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

主题色：`assets/scss/lab/_tokens.scss` 的 `$lab-blue` 与 `data/themes/minimal.toml` 的 `primary` 保持一致。

## 成员 `content/authors/<slug>/_index.md`

| 字段 | 必填 | 说明 |
|------|------|------|
| title | 是 | 显示名 |
| role | 是 | 身份，如 研一 / 教授 |
| user_groups | 是 | 成员用细分分组：导师、博士生、硕士生、研一~研三、本科生、毕业生；成员页按 导师 / 在读学生（聚合）/ 毕业生（聚合）三大组渲染，聚合组按年级排序（博士在前、高年级在前、同年级按 weight） |
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
| tags | 主题词；方向筛选与英文 taxonomy 使用（英文页用译名） |
| placeholder_art | 可选；方向卡无图片时使用的插画标识（action / agent / depth / lowlight），由 `views/card.html` 消费 |

栏目 `_index.md` 的 `summary` 留空时，使用 `lab.ui.section_leads.<section>`。

## Excel 批量

```text
py -3 scripts/import_projects_patents.py --xlsx-dir <dir> --content <contentDir> [--dry-run]

py -3 scripts/sync_lab_identity.py [--dry-run]
py -3 scripts/lint_content.py [--quiet]
```

`lint_content.py` 校验数据模型（主键/外键/枚举/一致性），退出码非 0 表示存在错误，建议提交前或 CI 运行。

## 视觉风格边界（改版前必读）

基调：**DeepSeek-clean 克制极简**——白底/近黑双模式，蓝染墨色，品牌蓝只做交互通道，
premium 感来自墨色质量与留白，不靠渐变和光效。受众（准研究生/同行/基金评审）
决定了可信度优先于视觉冲击。以下边界是**制度**，不是惯例：

| 风格元素 | 允许出现的位置 | 禁止出现的位置 |
|---|---|---|
| 玻璃拟态（半透明+blur） | 悬浮层：navbar、下拉菜单、搜索弹层吸顶头 | 卡片、正文面板、footer |
| 网格渐变（低饱和 blob） | 仅 hero（三 blob，mask 渐隐，decorative） | 其余一切 section 背景、按钮、卡片 |
| 品牌蓝 `#4176E6` | 仅交互态：链接、按钮、active、focus | 大面积底色、标题文字 |
| 深色模式 | 独立调色（`$lab-blue-dark: #6C9CF2`），禁止黑白反转式适配 | — |
| 新拟态（软凸/软凹） | 仅三个无文字小控件：明暗切换钮、返回顶部钮、分页 prev/next pill；必须保留 1px 边框 + `:focus-visible` 焦点环；需坐在同色面上 | 内容卡片、文字承载面、跨色温处 |
| 阴影 | whisper 级（`$lab-card-shadow*`），hover 才可抬升；浮层 toast 允许功能性强阴影 | 高投影、彩色光晕 |
| 间距 | 只允许 `$lab-space-*` 刻度（8px 体系） | 任意裸值 |
| 粒子/噪点、新野兽派 | 一律禁止 | — |

风格落位总则：每种风格有明确领地，一个区域最多一种"性格"；冲突时极简主义优先。

统一性红线（审计已验证，改动时不得破坏）：
- 所有页面走 lab-* 组件与 token；不允许 vendor 默认 `.btn-primary`/`.card` 裸类出现在产物中。
- 双语（zh/en）视觉必须逐字节一致，仅文案不同。
- 对比度改动必须过 `scripts/check_contrast.py`（WCAG AA，16 组全过）。
