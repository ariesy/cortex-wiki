---
pageType: entity
id: entity.tool.vercel
entityType: tool
name: "Vercel"
sourceIds:
  - https://docs.rsshub.app/deploy/
updatedAt: "2026-08-23"
---

# Vercel

Serverless 函数托管平台，RSSHub 官方支持的一键部署选项之一。提供 Git 集成、自动构建部署与全球 CDN，适合静态站 + Serverless Functions 的现代 Web 工作流。

## RSSHub 部署要点

- 支持"Instant deploy（免自动更新）"与"Automatic deploy upon update（PR 合并即自动更新）"两种方式。
- 自动更新方案：Fork RSSHub 仓库，配合 [Pull](https://github.com/apps/pull) GitHub App 保持与上游同步，Vercel 检测到 push 即自动重新部署。
- Node.js runtime 需注意 Vercel 对 ES Module 的 require 行为，详见 Vercel 官方文档的 advanced-node-configuration。

## 核心特性

- **Serverless Functions**：目录/函数即端点，按请求计费，自动扩缩容。
- **Preview Deployments**：每次 PR 生成独立预览 URL，利于联调。
- **Edge / Serverless 双运行时**：支持边缘渲染与 Node.js 服务端函数。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Cloudflare Workers](Cloudflare-Workers.md)
- [Fly.io](Fly.io.md)
- [Google App Engine（GAE）](Google-App-Engine.md)
- [Heroku](Heroku.md)
- [PikaPods](PikaPods.md)
- [Railway](Railway.md)
- [Sealos](Sealos.md)
- [Zeabur](Zeabur.md)
<!-- openclaw:wiki:related:end -->
