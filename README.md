# 智能感知与决策实验室网站

西安理工大学计算机科学与技术学院 · 智能感知与决策实验室（IPD Lab）静态站点。基于 Hugo 0.168 extended + Hugo Blox，自定义主题在 [`modules/lab-ui`](modules/lab-ui)。部署到 GitHub Pages（`gh-pages`）。

## 本地运行

需要 **Hugo 0.168 extended** 和 **Dart Sass**（独立 `sass` 或 `sass-embedded`）。npm 上的纯 JS `sass` 不能走 Hugo 的 embedded protocol。

```powershell
.\scripts\dev.ps1
```

打开 http://127.0.0.1:1313/ 。脚本优先使用 `Get-Command hugo`，否则回退到 `D:\Claude code\tools\hugo\hugo.exe`；若存在 `D:\Claude code\tools\dart-sass`，会把它加入 `PATH`。

## 构建与校验

```powershell
$env:PATH = "D:\Claude code\tools\dart-sass;" + $env:PATH
hugo --gc --minify --noBuildLock
npm run lint:css
python scripts/check_contrast.py
```

通过标准：命令 exit 0，lint 0，对比度全过。已知仅剩一条警告：blox-seo 自带的 `sitemap.xml` 被 Hugo 跳过。不要改 `_vendor/`。

## 仓库地图

| 路径 | 内容 |
|------|------|
| `content/` | 中文内容。论文 `publication/`，成果 hub `outcomes/`（公开地址仍是 `/publications/`），以及 `patent/`、`award/`、`project/`、`research/`、`post/`、`people/`、`authors/` |
| `modules/lab-ui/` | 模板、SCSS、JS。说明见 [modules/lab-ui/README.md](modules/lab-ui/README.md) |
| `config/_default/` | `hugo.yaml`、`params.yaml`、`languages.yaml`、`menus.yaml`、`module.yaml` |
| `data/` | `fonts/lab.toml`、`themes/minimal.toml` |
| `assets/media/` | 站点 logo / icon |
| `scripts/` | 本地预览、Dart Sass 安装、对比度、身份同步与导入 |
| `docs/` | [SCHEMA](docs/SCHEMA.md)、[DATA-MODEL](docs/DATA-MODEL.md)、[CMS](docs/CMS.md)、[色板](docs/design/color-system.html) |

身份与字段只改 `config/_default/params.yaml` 的 `lab:`，再跑 `scripts/sync_lab_identity.py`。字段约定见 [docs/SCHEMA.md](docs/SCHEMA.md)。

## 更多

- 约束与主题规则：[AGENTS.md](AGENTS.md)
- 内容与数据：[docs/](docs/)
