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
| tokens | `lab/_tokens.scss` | 设计 token 唯一来源（`$lab-*` / `--lab-*`，含断点 `$lab-bp-*`） |
| type | `lab/_type.scss` | 中文排印 mixin（display/section 标题） |
| grid | `lab/_grid.scss` | 栅格系统：断点 mixin、`lab-card-grid`、12 列基元、光学对齐 |
| abstracts | `lab/_abstracts.scss` | 共享 placeholder（标签/链接/箭头 vocabulary） |
| base | `lab/_base.scss` | 全局基础：对齐、gutters、导航、页脚 |
| controls | `lab/_controls.scss` / `lab/_menus.scss` | 复用控件：按钮、卡片基类、菜单 |
| views | `lab/_views-{results,people,pages,home,listing}.scss` | 各视图域样式 |
| dark | `lab/_dark.scss` | 暗色覆盖（保持在末段） |

## 栅格系统（lab/_grid.scss）

响应式网格的**唯一合法声明方式**——视图文件禁止手写 `repeat(n, minmax(...))` 和裸 px 媒体查询：

```scss
// 等宽卡片墙（3 → 2 → 1，gap = --lab-card-gap）：站点通用节奏
.lab-xxx-cards { @include lab-card-grid; }

// 指定列数（不做响应式降级时）
.lab-xxx { @include lab-grid-cols(2); }

// 断点（token：$lab-bp-sm/md/lg = 576/768/992）
@include lab-bp-down(lg) { … }  // ≤991（桌面优先，站内主流风格）
@include lab-bp-up(sm)   { … }  // ≥576（移动优先）
```

- `.lab-grid` 12 列基元 + `.lab-col-{1..12}` / `.lab-col-md-*` / `.lab-col-sm-*` / `.lab-col-full`：仅供未来**混合跨度**版面（杂志式 hero 等），等宽卡片墙禁止使用。
- 光学对齐：`$lab-align-glyph-nudge` / `$lab-align-arrow-nudge`（亚 4px 视觉补偿），工具类 `.lab-align-glyph` / `.lab-align-arrow`；"更多"链接箭头与卡片类型 glyph 已内置。
- 已知例外：`_base.scss` 页脚断点（768 含边界）与 `_views-pages.scss` 相册断点（639，内容驱动）保留裸值。

## Partials（layouts/partials/）

按领域分组，文件名不带前缀（目录即命名空间）：

- `components/` — 可复用组件：`status-label` / `resolve-author` / `detail-authors` / `featured-image` / `member-focus-*` / `member-research-pages` / `research-cards` / `section-lead`
- `listing/` — 列表页族：`list-page` / `filter-config` / `filter-body` / `filters` / `filter-script` / `header` / `collect-years`
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
