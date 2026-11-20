---
pageType: entity
id: entity.concept.opencode-web-ui
title: "OpenCode Web UI / serve 部署与扩展"
entityType: concept
aliases:
  - opencode web
  - opencode serve
  - OpenCode 网页版
tags: [opencode, web-ui, serve, sdk, 部署]
updatedAt: "2026-08-16"
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-15-1140-d8c05884
  - source.bridge.workspace-142ea9a2.memory-2026-08-15-2357-7813cab4
claims:
  - id: claim.opencode-web.ui
    text: "OpenCode 官方原生支持网页版，无需借助 OpenClaw：`opencode web` 起服务并打开浏览器，默认绑定 127.0.0.1 随机端口；`--port 4096` 固定端口，`--hostname 0.0.0.0` 供局域网/远程访问。体验与 TUI 一致（同样会话、工具调用、agent 配置），读取同一套 opencode.json 与认证（含 OmniRoute/CLIProxyAPI 代理的模型）。"
    status: supported
    confidence: 0.9
  - id: claim.opencode-web.serve
    text: "`opencode serve` 是 headless API 模式，暴露 OpenAPI 接口供 SDK/第三方 Web UI 对接，支持 --port/--hostname/--cors 与 `OPENCODE_SERVER_PASSWORD` 环境变量密码鉴权；社区增强 UI（如 pk-opencode-webui）即连接此外后端。"
    status: supported
    confidence: 0.9
  - id: claim.opencode-web.security
    text: "安全注意：web 模式绑定 0.0.0.0 后默认无鉴权，局域网任何人都能打开 agent 环境（可读文件、跑命令）。要么仅绑内网，要么用 serve + 密码，不要直接裸奔公网。"
    status: supported
    confidence: 0.9
  - id: claim.opencode-web.extend
    text: "扩展路径三层：(1) fork 官方 MIT 开源仓库（SolidJS Web UI）源码级改造，代价是跟随升级麻烦；(2) 官方推荐方案——用 `opencode serve` 的完整 REST API（session、消息流、config、provider OAuth、diff、fork 等）+ 官方 TypeScript SDK `@opencode-ai/sdk` 自建前端，`--cors` 放行自定义前端域名配 `OPENCODE_SERVER_PASSWORD` 鉴权；(3) 直接使用社区现成的扩展 UI。"
    status: supported
    confidence: 0.85
  - id: claim.opencode-web.systemd-user-service
    text: "本机把 opencode web 做成 systemd 用户级服务（`~/.config/systemd/user/`）实现开机自启，与 dsh web.service 同模式：Type=simple + ExecStart 绝对路径 + WorkingDirectory=%h + Restart=always，配合 linger 可在未登录时也启动；落地前先确认版本（opencode 1.18.15）及端口是否被占用（5899/5900 已被 Vibe-Trading 的 vite 前端占用，不冲突）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-15-2357-7813cab4
        weight: 0.8
---

# OpenCode Web UI / serve 部署与扩展

## 两种启动方式

| 方式 | 命令 | 说明 |
|---|---|---|
| 官方 Web UI | `opencode web [--port 4096] [--hostname 0.0.0.0]` | 起服务并打开浏览器，体验同 TUI |
| headless API | `opencode serve --cors --port ...` | 暴露 OpenAPI，供 SDK / 第三方前端对接 |

两者底层同一套服务，配置与认证共用 `opencode.json`（含 OmniRoute / CLIProxyAPI 代理模型）。

## 安全

- `web` 绑 0.0.0.0 默认无鉴权 = 把可读写文件、可执行命令的 agent 环境暴露给整个局域网
- 推荐：仅内网绑定，或 `serve` + `OPENCODE_SERVER_PASSWORD`

## 自定义 / 扩展

1. **源码级**：fork MIT 仓库改 SolidJS Web UI（维护成本高）
2. **官方推荐**：`serve` REST API + `@opencode-ai/sdk` 自建前端，`--cors` + 密码鉴权
3. **社区 UI**：直接用现成的第三方增强界面

## 相关

- [[opencode-permission-rule-order-bug]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-15-1140](../sources/bridge-workspace-142ea9a2-memory-2026-08-15-1140-d8c05884.md)
- [Memory Bridge (main): 2026-08-15-2357](../sources/bridge-workspace-142ea9a2-memory-2026-08-15-2357-7813cab4.md)
<!-- openclaw:wiki:related:end -->
