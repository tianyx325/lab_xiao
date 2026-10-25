# 智能感知与决策实验室网站

西安理工大学计算机科学与技术学院 · 智能感知与决策实验室（IPD Lab）静态站点。

基于 [Hugo](https://gohugo.io/) Extended + [Hugo Blox](https://hugoblox.com/) + 本地模块 [`modules/lab-ui`](modules/lab-ui)（可复用 UI）。

## 换实验室（可复用）

1. **只改** [`config/_default/params.yaml`](config/_default/params.yaml) 的 **`lab:`** 段（名称、学院、邮箱、地址、坐标、tagline/lead、CTA、招生文案、栏目导语）。
2. 运行身份同步（回写站名 / SEO / 页脚）：

```powershell
py -3 scripts\sync_lab_identity.py
```

3. 替换 `content/`（成员、方向、项目、专利等）与 `assets/media/welcome.png`。
4. 若改品牌色：改 `assets/scss/lab/_tokens.scss` 的 `$lab-blue`，并同步 `data/themes/minimal.toml` 的 `primary`。
5. 字段约定见 [`docs/SCHEMA.md`](docs/SCHEMA.md)。

首页 hero / 方向卡 / 联系页 / 列表导语均读 `params.lab`，不必改 HTML 硬编码文案。

## 本地预览

需 **Hugo Extended ≥ 0.135** 与 **Go ≥ 1.22**。

```powershell
.\start-server.ps1
```

http://127.0.0.1:1313/

## 生产构建

```powershell
hugo --gc --minify
```

`baseURL` 见 `hugo.yaml`；Netlify / GitHub Pages 会用 `-b $URL` 覆盖。

## 内容与脚本

| 内容 | 路径 |
|------|------|
| 成员 | `content/authors/*/` |
| 方向 | `content/research/`（`weight` 控制首页顺序） |
| 项目 / 专利 | `content/project/`、`content/patent/` |
| 字段契约 | [`docs/SCHEMA.md`](docs/SCHEMA.md) |

```powershell
# 身份：lab → hugo title / languages / marketing / footer
py -3 scripts\sync_lab_identity.py
py -3 scripts\sync_lab_identity.py --dry-run

# 成员 research_focus 从 bio 回填（不正文）
py -3 scripts\sync_research_focus.py
py -3 scripts\sync_research_focus.py --authors path\to\authors

# 项目/专利 Excel（默认读仓库上一级目录）
py -3 scripts\import_projects_patents.py --dry-run
py -3 scripts\import_projects_patents.py --xlsx-dir "D:\path\to\xlsx" --content ".\content"
```

约定：批量以 Excel 为准；日常改 MD；再导入会覆盖项目/专利页。成员**正文**不覆盖。

## 模块 lab-ui

可复用 shortcode / partial / Leaflet / archetype / 设计 token 在 `modules/lab-ui`。站点通过 [`config/_default/module.yaml`](config/_default/module.yaml) 的 **mounts** 挂载（无需拉取远程模块）。可拷贝该目录到其他 Hugo 站并同样 mounts。

## 设计

- Token：`assets/scss/lab/_tokens.scss`（站点唯一来源；`modules/lab-ui` 不挂载 SCSS）
- 站点皮肤：`assets/scss/template.scss`（`@import "lab/tokens"`）
