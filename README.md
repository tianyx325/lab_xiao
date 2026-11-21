# lab-xiao

智能感知与决策实验室（IPD Lab）官网 — [HugoBlox Kit](https://github.com/HugoBlox/kit)（Tailwind）。

生产域名：`https://lab.xaut.edu.cn/` · GitHub Pages 镜像：`https://tianyx325.github.io/lab_xiao/`

## 结构

| 路径 | 说明 |
|---|---|
| `site/` | Hugo 站点（内容、配置、`_vendor/`） |
| `kit-main/` | 本地 Kit 源码（`go.mod` replace） |
| `scripts/` | 一次性迁移 / 别名工具（内容已迁完，日常不用） |
| `.github/workflows/` | PR 构建检查 + Pages 发布 |

## 本地预览

```powershell
$env:Path = "D:\code-tyx\lab-xiao\lab-xiao\tools\go\bin;" + $env:Path
cd D:\code-tyx\lab-xiao\lab-xiao\site
npm ci
hugo server -D -p 1314
```

## 部署

推送 `main` → `.github/workflows/publish.yaml` 构建并发布到 `gh-pages`（`SITE_BASE_URL` 覆盖为 Pages 子路径）。

校内部署若指向同一产物，用 `baseURL: https://lab.xaut.edu.cn/`（见 `site/config/_default/hugo.yaml`）。
