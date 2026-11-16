# lab-ui

站点自包含主题模块：layouts、SCSS、vanilla JS、archetype、Leaflet 静态资源。主题资产都在本目录；内容、配置和站点媒体留在仓库根。构建步骤见 [根 README](../../README.md)，约束见 [AGENTS.md](../../AGENTS.md)。

## 接入

`config/_default/module.yaml` 用 mounts 把 `layouts`、`assets`、`static`、`archetypes` 挂到站点。覆盖 Hugo Blox 时，在 `layouts/` 下放同路径文件，不要改 `_vendor/`。

## 模板

- 详情页：`layouts/<section>/single.html`
- 列表页：`layouts/<section>/list.html`，其次 `layouts/section/<name>.html`，再落到 `_default/list.html`
- 成果 hub 目录是 `content/outcomes/`，front matter `type: publications`，所以模板仍是 `layouts/publications/list.html`
- `layouts/partials/` 按 `components/`、`listing/`、`article/` 分组。顶层无前缀文件是 vendor 覆盖，保留原名
- Shortcode 在 `layouts/shortcodes/`

## SCSS

入口 `assets/scss/template.scss`。`@import` 顺序就是级联顺序，不要重排：

`tokens → type → grid → abstracts → base → controls → views/results → menus → views/people → views/pages → views/home → views/listing → dark`

视图按源文件顺序拆在 `assets/scss/lab/views/`。Token 只定义在 `lab/_tokens.scss`。等宽卡片墙用 `lab-card-grid` / `lab-grid-cols` 和 `lab-bp-*`，不要在视图里手写 `repeat()` 或裸 px 媒体查询。

## JS

`assets/js/lab/lab-*.js` 由 `layouts/partials/custom_js.html` 按页面加载。`assets/js/wowchemy-map.js` 留在原处，配合 `static/vendor/leaflet/`。
