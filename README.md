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

需要仓库内 `tools/dart-sass` 与 `tools/go`（Hugo Extended 0.168）。  
手动等价：`site/scripts/dev.ps1`（清 `resources/_gen` + `hugo server --disableFastRender`）。

## 校验

```powershell
cd site
npm run check   # theme sync + content schema + lab 裸值扫描
```

## 结构

| 路径 | 说明 |
|---|---|
| `site/` | Hugo 站点（内容 + `_vendor` blox-bootstrap） |
| `site/assets/scss/lab/` | **唯一**视觉层（tokens → chrome → views） |
| `site/content/` | Markdown page bundles（契约见 [`site/CONTENT-SCHEMA.md`](site/CONTENT-SCHEMA.md)） |
| `.github/workflows/` | 构建与发布 |

生产：`https://lab.xaut.edu.cn/` · Pages：`https://tianyx325.github.io/lab_xiao/`
