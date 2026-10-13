# lab-ui

实验室站点可复用 UI 层：成员/卡片/详情壳、联系页、地图 Leaflet、内容 archetype、设计 token。

## 接入

在站点 `config/_default/module.yaml` 用 mounts 挂载本目录（推荐，无需网络）：

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

站点 `params.lab` 为品牌与 UI 文案的唯一配置源（见主站 README / `docs/SCHEMA.md`）。改完后跑 `scripts/sync_lab_identity.py`。

## Shortcodes

- `lab-hero` — 首页英雄区（`lab.name` / tagline / lead / `lab.ui.cta_*`）
- `lab-section-head` — 区块标题 +「全部」链接
- `lab-research-cards` — 从 `content/research/` 取前 N 条（`count` 可覆盖）
- `lab-research-lead` — 方向列表导语（`lab.seo_description`）
- `lab-contact` — 联系与招生（`lab.admit.*` + 邮箱地址地图）

## Partials

- `lab-section-lead` — 列表导语（页面 summary → `lab.ui.section_leads.<key>`）
- `lab-list-header` / `lab-status-label` / `lab-member-focus-line` / article shell 等

## Layouts（随模块挂载）

成员块、卡片视图、作者详情、项目/专利/论文详情、列表壳、导航返回、Leaflet。

## Tokens

`assets/scss/lab/_tokens.scss` — 站点 `template.scss` 应 `@import "lab/tokens"`，勿重复定义 `$lab-*`。
