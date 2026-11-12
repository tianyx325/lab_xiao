# CMS 后台（Sveltia CMS）使用与配置指南

学生在浏览器里用表单维护网站内容，不需要懂 Markdown、YAML 或 Git。

- 访问入口：**`<站点地址>/admin/`**
- CMS：[Sveltia CMS](https://github.com/sveltia/sveltia-cms)（Decap CMS 的现代替代，界面中文友好，脚本已自托管于 `static/admin/sveltia-cms.js`，不依赖 CDN）
- 表单结构：`data/decap_cms_config.yaml`（与 `docs/DATA-MODEL.md` 数据模型一一对应）
- 提交即发布：在 CMS 里点「保存 → 发布」会直接 commit 到 `main` 分支，GitHub Actions 自动构建上线

## 首次配置（仅管理员做一次）

Sveltia 通过 GitHub OAuth 登录，需要一个免费的中转授权服务。全程约 15 分钟：

### 1. 创建 GitHub OAuth App

1. 打开 <https://github.com/settings/developers> → **New OAuth App**
2. 填写：
   - Application name：`实验室 CMS`
   - Homepage URL：站点地址（如 `https://tianyx325.github.io/lab_xiao/`）
   - Authorization callback URL：`https://<你的auth域名>/callback`（下一步部署后确定）
3. 记下生成的 **Client ID**，并生成 **Client Secret**

### 2. 部署授权中转（Cloudflare Workers，免费）

使用官方推荐的 [sveltia-cms-auth](https://github.com/sveltia/sveltia-cms-auth)：

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → Workers → 创建 Worker，一键部署该项目的 `worker.js`
2. 配置环境变量：
   - `GITHUB_CLIENT_ID` / `GITHUB_CLIENT_SECRET`：上一步的值
   - `ALLOWED_DOMAINS`：站点域名（如 `tianyx325.github.io`）
3. 记下 Worker 地址（如 `https://xxx.workers.dev`）

### 3. 回填回调地址

回到 GitHub OAuth App，把 Authorization callback URL 改为：

```
https://<你的auth域名>/callback
```

然后在 `data/decap_cms_config.yaml` 的 `backend:` 段加一行：

```yaml
base_url: https://<你的auth域名>
```

重新构建发布即完成。此后访问 `/admin/` → 用 GitHub 账号登录 → 开始编辑。

## 日常使用

| 要做的事 | 在 CMS 里 |
|----------|-----------|
| 新增论文 | 论文 → 新建 → 填表单（作者成员填 slug，外协填全名）→ 保存发布 |
| 新增成员 | 团队成员 → 新建 → 分组必选一个（分组名勿自创） |
| 发新闻 | 新闻动态 → 新建 → 填正文 |
| 首页精选论文 | 编辑论文 → 打开「精选」开关 |
| 上传配图 | 表单里的图片控件直接上传，自动存进该条目所在目录 |

注意事项：

- **slug 一经发布不可改**（URL 即承诺），新建时想好命名
- 作者字段规则见 `docs/DATA-MODEL.md` 第 3 节（双轨制）
- 批量导入项目/专利请继续走 Excel：`py -3 scripts/import_projects_patents.py`

## 双语（zh / en）

CMS 已开启多语言（Sveltia 顶部可切换 中文 / English）：

- 新建条目时**先填中文**保存，再切到 English 补翻译；日期、编号、链接、枚举等共用字段会自动带出，无需重复填写
- 只维护中文也可以正常发布——英文页会暂时缺失，lint 会以 `E-i18n` 提醒补齐（不阻塞发布）
- 文件层面即 `index.md`（中文）与 `index.en.md`（英文）成对存放，详见 `docs/DATA-MODEL.md` 第 8 节

## 本地开发

本地 `hugo server -D` 时 CMS 配置自动切换为 local backend（由 blox-plugin-decap-cms 处理）。本地纯写作仍建议直接改 Markdown；CMS 主要面向线上编辑场景。

## 故障排查

| 现象 | 处理 |
|------|------|
| `/admin/` 显示「内容管理加载失败」 | `static/admin/sveltia-cms.js` 缺失或未发布；重新构建 |
| 登录跳转报 redirect_uri 错误 | OAuth App 的 callback URL 与 Worker 域名不一致 |
| 保存时报 403 | GitHub 账号无该仓库写权限，找管理员加 collaborator |
| 表单字段和文档对不上 | 以 `data/decap_cms_config.yaml` 为准；改它须同步 `docs/DATA-MODEL.md` |
