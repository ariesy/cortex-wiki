---
pageType: entity
id: entity.tool.cloudflare-workers
entityType: tool
name: "Cloudflare Workers"
sourceIds:
  - https://docs.rsshub.app/deploy/
updatedAt: "2026-08-23"
---

# Cloudflare Workers

Cloudflare 提供的无服务器（Serverless）函数计算平台，基于 V8 隔离技术在全球边缘节点运行代码，RSSHub 官方支持的部署选项之一。

## RSSHub 部署要点

- RSSHub 在 Cloudflare Workers 上部署时，缓存通常使用 **Cloudflare Workers KV**（全球分布式键值存储）。
- 涉及浏览器抓取 / 渲染的 RSS 源需要 **Cloudflare Browser Rendering**（浏览器渲染服务）配合。
- 无服务器函数默认运行在边缘节点，就近响应，冷启动极快（毫秒级）。

## 核心特性

- **边缘执行**：代码在全球 300+ 数据中心就近运行，天然 CDN 分发。
- **Workers KV**：全球最终一致的键值存储，适合缓存、配置、小型数据。
- **Browser Rendering**：基于 Playwright 的浏览器渲染服务，可做页面截图 / JS 渲染抓取。
- **免费额度友好**：提供慷慨的免费层，个人项目常可零成本运行。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Fly.io](Fly.io.md)
- [Google App Engine（GAE）](Google-App-Engine.md)
- [Heroku](Heroku.md)
- [PikaPods](PikaPods.md)
- [Railway](Railway.md)
- [Sealos](Sealos.md)
- [Vercel](Vercel.md)
- [Zeabur](Zeabur.md)
<!-- openclaw:wiki:related:end -->
