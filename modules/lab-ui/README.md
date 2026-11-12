# lab-ui

实验室站点自包含主题模块：layouts（模板与组件）、SCSS 设计体系、交互 JS、内容 archetype、Leaflet 静态资源。**模块搬走即用**——所有主题资产都在本目录内，站点层只保留内容（`content/`）、配置（`config/`）与站点媒体（`assets/media/`）。

## 接入

站点 `config/_default/module.yaml` 用 mounts 挂载本模块（本地离线，无需网络）：

```yaml
mounts:
  - source: modules/lab-ui/layouts
    target: layouts
  - source: modules/lab-ui/assets
    target: assets
  - source: modules/lab-ui/static
    target: static
  - source: modules/lab-ui/archetypes
    target: archetypes
  # …并保留站点自身 layouts/assets/static/content/data/i18n mounts
```

站点 `params.lab` 为品牌与 UI 文案的唯一配置源（见 `docs/SCHEMA.md`）。改完后跑 `scripts/sync_lab_identity.py`。

## SCSS 体系（assets/scss/）

入口 `template.scss` 覆盖 vendor 同名文件（asset overlay 机制）。**层级顺序即级联顺序，勿重排**：

| 层 | 文件 | 职责 |
|----|------|------|
| tokens | `lab/_tokens.scss` | 设计 token 唯一来源（`$lab-*` / `--lab-*`） |
| type | `lab/_type.scss` | 中文排印 mixin（display/section 标题） |
| base | `lab/_base.scss` | 全局基础：对齐、gutters、导航、页脚 |
| controls | `lab/_controls.scss` / `lab/_menus.scss` | 复用控件：按钮、卡片基类、菜单 |
| views | `lab/_views-{results,people,pages,home,listing}.scss` | 各视图域样式 |
| dark | `lab/_dark.scss` | 暗色覆盖（保持在末段） |

## Partials（layouts/partials/）

按领域分组，文件名不带前缀（目录即命名空间）：

- `components/` — 可复用组件：`status-label` / `resolve-author` / `detail-authors` / `featured-image` / `member-focus-*` / `member-research-pages` / `research-cards` / `section-lead`
- `listing/` — 列表页族：`list-page` / `filters` / `filter-script` / `header` / `collect-years`
- `article/` — 详情页族：`shell-start` / `shell-end` / `gallery` / `videos` / `build-meta-and-shell` / `meta-tags`
- 顶层无前缀文件（`page_author.html`、`views/`、`blocks/` 等）为 **vendor 覆盖文件，保留原名，勿改名勿分组**

## JS（assets/js/）

单一职责 vanilla 组件：`lab-navbar-scroll` / `lab-mailto` / `lab-member-works` / `lab-gallery`（由 `partials/custom_js.html` 统一加载）、`wowchemy-map.js`（高德瓦片地图，配合模块 `static/vendor/leaflet/`）。

## Shortcodes

- `lab-hero` — 首页英雄区（`lab.name` / tagline / lead）
- `lab-section-head` — 区块标题 +「全部」链接
- `lab-research-cards` — 从 `content/research/` 取前 N 条（`count` 可覆盖）
- `lab-research-lead` — 方向列表导语（`lab.seo_description`）
- `lab-contact` — 联系与招生（`lab.admit.*` + 邮箱地址地图）
