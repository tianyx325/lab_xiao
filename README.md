# lab-xiao

智能感知与决策实验室官网。视觉栈：**Hugo Blox（薄宿主）+ lab SCSS（唯一视觉层）**。

## 样式权威（必读）

| 做 | 不做 |
|---|---|
| 改 [`site/assets/scss/lab/_tokens.scss`](site/assets/scss/lab/_tokens.scss) | 往 `assets/css/custom.css` 塞整包 lab |
| 改 `site/assets/scss/lab/**` 组件 | 依赖 `npm run build:lab-css` 当线上 CSS |
| 用 `npm run dev` 预览（会清 `_gen`） | 改完 SCSS 却不清缓存就断言「没生效」 |

**真源管线**：`main.scss` → `template.scss` → `lab/*` → Hugo 打成 `/css/wowchemy.css`。

## 本地预览

前置：Node.js 20+、Hugo Extended 0.168（Dart Sass 无需单独安装）。

```bash
cd site
npm ci
npm run dev     # http://127.0.0.1:1314/
```

`npm ci` 会安装自带 Dart Sass 的 `sass-embedded`；`scripts/hugo.mjs` 负责把它加入 PATH、清理 `resources/_gen`，再启动 Hugo。

构建：`npm run build`。

可选：仓库外存在 `tools/dart-sass` 时会优先使用；`tools/go` 仅在改动 `go.mod` 后执行 `hugo mod vendor` 时需要。

## 校验

```bash
cd site
npm run check        # theme sync + content schema + i18n 键一致性 + lab 裸值扫描
npm run build        # 产出 public/
npm run check:links  # 构建后校验站内链接与锚点
```

`npm test` 等价于 `npm run check`；CI 在构建后还会跑 `check:links`。

## 结构

| 路径 | 说明 |
|---|---|
| `site/` | Hugo 站点（内容 + 已提交的 `_vendor`，离线可构建） |
| `site/assets/scss/lab/` | **唯一**视觉层（tokens → chrome → views） |
| `site/content/` | Markdown page bundles（契约见 [`site/CONTENT-SCHEMA.md`](site/CONTENT-SCHEMA.md)） |
| `.github/workflows/` | 构建与发布 |

部署：GitHub Pages `https://tianyx325.github.io/lab_xiao/`（`baseURL` 在 `site/config/_default/hugo.yaml`）。
包管理：npm（`site/package-lock.json`）。Hugo 版本统一定在 `0.168.0`。
