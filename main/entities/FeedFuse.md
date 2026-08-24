---
pageType: entity
id: entity.tool.feedfuse
entityType: tool
name: "FeedFuse"
sourceIds:
  - https://github.com/BryanHoo/FeedFuse
  - https://github.com/FreshRSS/FreshRSS
updatedAt: "2026-08-24"
---

# FeedFuse

自托管 AI RSS 阅读器（[BryanHoo/FeedFuse](https://github.com/BryanHoo/FeedFuse)），定位是"把 RSS 阅读、全文抓取和 AI 辅助理解放进同一工作台"。保留 RSS 的开放/可迁移/可掌控，同时把全文抓取、过滤、AI 摘要、翻译和多源汇总串成一条连续阅读工作流。

## 基本信息

- **仓库：** BryanHoo/FeedFuse（AGPL-3.0）
- **创建时间：** 2026-02-22，新项目（截至 2026-08-24 约 6 个月）
- **热度：** ⭐496 / fork 30，单人主导开发，更新活跃（最新版 v0.4.2，2026-07-23 仍有 commit）
- **技术栈：** Next.js 16 + React 19 + TypeScript 5.9 + Tailwind 4.2 + PostgreSQL 16 + OpenAI 兼容 API

## 核心能力

- **RSS 管理**：集中管理订阅源、分类组织，支持 OPML 导入导出
- **阅读体验**：三栏界面 + 全文抓取，订阅/列表/正文在同一工作台
- **内容减噪**：关键词过滤、AI 过滤、重复/相似转载过滤
- **AI 辅助理解**：文章摘要、标题翻译、正文翻译、沉浸式双语阅读
- **AI 解读**：把多个信息源汇总成更高层的重点归纳，快速把握趋势
- **多账号**：管理员创建用户，按用户隔离订阅、设置、Fever 服务和阅读状态
- **自托管部署**：预构建镜像直接启动，也可源码运行调试

## 与 FreshRSS 对比

| 维度 | FeedFuse | FreshRSS |
|---|---|---|
| 定位 | RSS + 全文抓取 + AI 理解一体化工作台 | 成熟的自托管新闻聚合器（2012 年起） |
| 技术栈 | Next.js / React / PostgreSQL | PHP + MySQL/PostgreSQL/SQLite |
| 社区体量 | 新项目，⭐496，单人主导 | ⭐15.8k，1.2k forks，社区生态成熟 |
| AI 能力 | 原生内置：摘要、翻译、双语阅读、AI 过滤、多源 AI 解读 | 无原生 AI，需插件或外部工具配合 |
| 客户端接入 | 内置 Fever 兼容服务 | Fever + Google Reader 兼容 API，第三方 App 生态极广 |
| 资源占用 | Node 服务 + PostgreSQL，偏重 | PHP 传统栈，轻量，小 VPS 友好 |

**判断：** FreshRSS 是久经考验的"纯聚合器"，稳定性、轻量和移动端生态行业最强，但 AI 能力要自己外挂；FeedFuse 把"订阅 → 降噪 → AI 消化"做成原生闭环，产品方向更贴合 AI 时代的信息工作流，代价是项目只有半年历史、社区小、长期维护存在不确定性。优先稳定与生态选 FreshRSS，优先一体化 AI 阅读体验选 FeedFuse。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
