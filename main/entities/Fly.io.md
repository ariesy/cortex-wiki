---
pageType: entity
id: entity.tool.fly-io
entityType: tool
name: "Fly.io"
sourceIds:
  - https://docs.rsshub.app/deploy/
updatedAt: "2026-08-23"
---

# Fly.io

基于全球边缘网络的容器 / 应用托管平台，主打"把应用部署到离用户最近的地区"，RSSHub 官方支持的部署选项之一。

## RSSHub 部署要点

- **Method 1: Fork** — Fork RSSHub 仓库，用 flyctl CLI 一键部署。
- **Method 2: 自行维护 fly.toml** — 手动编写 fly.toml 配置并部署。
- **内置 Upstash Redis 缓存** — Fly 内置 Upstash Redis 作为 RSSHub 缓存方案，避免自带 Redis 运维负担。

## 核心特性

- **Anycast 全球部署**：应用可按地区就近部署（如新加坡、东京、法兰克福），降低延迟。
- **fly.toml 声明式配置**：通过配置文件声明应用、机器与网络拓扑。
- **内置托管 Redis（Upstash）**：免运维的 Redis 缓存，适合 RSSHub 这类需要缓存的抓取服务。
- **支持自定义域名绑定**：文档中提供域名绑定指引。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Cloudflare Workers](Cloudflare-Workers.md)
- [Google App Engine（GAE）](Google-App-Engine.md)
- [Heroku](Heroku.md)
- [PikaPods](PikaPods.md)
- [Railway](Railway.md)
- [Sealos](Sealos.md)
- [Vercel](Vercel.md)
- [Zeabur](Zeabur.md)
<!-- openclaw:wiki:related:end -->
