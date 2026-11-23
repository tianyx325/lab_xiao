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

```powershell
cd D:\code-tyx\lab-xiao\lab-xiao\site
npm run dev
```

需要 Hugo Extended 0.168 和 Dart Sass 1.77.8（仓库内 `tools/dart-sass` 已自带）。  
`dev.ps1` 会自动把 `tools/dart-sass` 加入 PATH；在 Bash 下直接跑 `hugo` 前需手动：

```bash
export PATH="$PWD/tools/dart-sass/dart-sass:$PATH"
```

手动预览等价：清 `site/resources/_gen` 后 `hugo server --disableFastRender`。
`tools/go` 仅在改动 `go.mod` 重新 `hugo mod vendor` 时需要。

## 校验

```powershell
cd site
npm run check   # theme sync + content schema + lab 裸值扫描
```

## 结构

| 路径 | 说明 |
|---|---|
| `site/` | Hugo 站点（内容 + 已提交的 `_vendor`，离线可构建） |
| `site/assets/scss/lab/` | **唯一**视觉层（tokens → chrome → views） |
| `site/content/` | Markdown page bundles（契约见 [`site/CONTENT-SCHEMA.md`](site/CONTENT-SCHEMA.md)） |
| `.github/workflows/` | 构建与发布 |

部署：GitHub Pages `https://tianyx325.github.io/lab_xiao/`（`baseURL` 在 `site/config/_default/hugo.yaml`）。
包管理：npm（`site/package-lock.json`）。Hugo 版本统一定在 `0.168.0`。
