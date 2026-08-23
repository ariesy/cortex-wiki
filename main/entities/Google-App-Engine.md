---
pageType: entity
id: entity.tool.google-app-engine
entityType: tool
name: "Google App Engine"
sourceIds:
  - https://docs.rsshub.app/deploy/
updatedAt: "2026-08-23"
---

# Google App Engine（GAE）

Google Cloud 的 PaaS 托管平台，支持自动扩缩容与多运行时，RSSHub 官方支持的部署选项之一。

## RSSHub 部署要点

- **app.yaml 配置**：RSSHub 部署到 GAE 需要编写 `app.yaml` 声明运行时（Node.js）与资源。
- **Before You Begin**：部署前需准备 GCP 项目、启用 App Engine、安装 gcloud CLI。
- **支持自定义域名**：GAE 原生绑定 Google 管理域名或自定义域名。

## 核心特性

- **全托管 PaaS**：无需管理服务器，自动扩缩容。
- **app.yaml 声明式配置**：声明运行时、内存、实例数等。
- **多运行时**：Node.js、Python、Go、Java、PHP 等。
- **与 GCP 生态集成**：Cloud Storage、Cloud SQL、Cloud Scheduler 等无缝联动。
- **免费层存在**：标准环境有每日免费配额（曾有政策调整，需留意当前规则）。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Cloudflare Workers](Cloudflare-Workers.md)
- [Fly.io](Fly.io.md)
- [Heroku](Heroku.md)
- [PikaPods](PikaPods.md)
- [Railway](Railway.md)
- [Sealos](Sealos.md)
- [Vercel](Vercel.md)
- [Zeabur](Zeabur.md)
<!-- openclaw:wiki:related:end -->
