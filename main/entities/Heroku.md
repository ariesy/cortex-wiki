---
pageType: entity
id: entity.tool.heroku
entityType: tool
name: "Heroku"
sourceIds:
  - https://docs.rsshub.app/deploy/
updatedAt: "2026-08-23"
---

# Heroku

云平台即服务（PaaS）先驱，支持以 Git push 方式一键部署应用，曾是 RSSHub 官方推荐的部署选项之一（现已逐步移入历史方案）。

## RSSHub 部署要点

- **Instant deploy（免自动更新）** 与 **Automatic deploy upon update（GitHub 更新自动部署）** 两种方式。
- 通过 Heroku Git 或 GitHub 集成部署 Node.js 应用，RSSHub 为 Node.js 项目开箱即用。

## 核心特性

- **Git push 部署**：`git push heroku master` 即可部署，无需服务器运维。
- **Add-ons 生态**：Redis、Postgres 等数据库/缓存通过 Add-on 一键附加。
- **Dyno 运行时**：按 Dyno 计费的容器化进程，支持自动扩缩。
- **注意**：Heroku 已于 2022 年底起取消免费 Dyno，个人免费部署场景已基本消失。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Cloudflare Workers](Cloudflare-Workers.md)
- [Fly.io](Fly.io.md)
- [Google App Engine（GAE）](Google-App-Engine.md)
- [PikaPods](PikaPods.md)
- [Railway](Railway.md)
- [Sealos](Sealos.md)
- [Vercel](Vercel.md)
- [Zeabur](Zeabur.md)
<!-- openclaw:wiki:related:end -->
