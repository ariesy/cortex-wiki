---
pageType: entity
id: entity.project.omniroute-cliproxyapi
title: OmniRoute CLIProxyAPI 集成
entityType: project
aliases:
  - CLIProxyAPI
  - OmniRoute + CLIProxyAPI
updatedAt: 2026-08-18T07:06:49.041Z
status: active
claims:
  - id: claim.cliproxy.what
    text: "CLIProxyAPI（router-for-me/CLIProxyAPI）是 OmniRoute 的可选 sidecar 服务，把 Claude Code、Codex、Gemini CLI、Qwen Code 等 CLI 形态 AI 工具包装成 OpenAI 兼容 API 供 OmniRoute 路由；跑在 omniroute 容器内，端口 8317，配置在 `/app/data/services/cliproxy/config.yaml`（omniroute-data 数据卷内，重建容器不丢）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-422c0c63
        weight: 0.85
  - id: claim.cliproxy.management-key
    text: "CLIProxyAPI 必须配置 `remote-management.secret-key`（并设 allow-remote: true），否则 `/v0/management/*` 全部返回 404、管理页面无法登录；密钥在 `~/.openclaw/.env` 的 OMNIROUTE_MANAGE_KEY；管理页面是 `http://<host>:8317/management.html`（根路径 `/` 是 API 信息页）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-422c0c63
        weight: 0.85
  - id: claim.cliproxy.provider-expose
    text: "version_manager 表的 `provider_expose` 字段决定服务模型是否参与路由：1 = expose service models in routing，0 = fallback-only（CLIProxyAPI 默认）；面板看不到 CLIProxyAPI 模型就是因为它为 0，需在面板 enable 后重启。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-422c0c63
        weight: 0.85
  - id: claim.cliproxy.panel-status-mismatch
    text: "OmniRoute 面板 embedded services 状态来自内存中 supervisor 实例（`getSupervisor(tool).getStatus().state`），不是 version_manager.status；手动 docker exec 起的进程与 supervisor spawn 的进程抢 8317 端口会造成面板显示 stopped/error。修复：杀光 cliproxyapi 进程 → version_manager.status 重置为 stopped → docker restart omniroute → 由 supervisor auto_start 干净拉起；面板显示 running 时不要再点启动。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-422c0c63
        weight: 0.85
  - id: claim.cliproxy.kimi-vs-direct
    text: "CLIProxyAPI 接 kimi 与 OmniRoute 直连 kimi web provider 的区别：认证路径（CLI OAuth vs 开放平台 API key）、额度（CLI 账号免费额度 vs API 按量付费）、模型列表（CLI 有 code 系列）、token 维护方；旧的 kimi-coding 直连连接 token 已过期停用，走 CLIProxyAPI 更省心。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-422c0c63
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-08-09-422c0c63.md

---
# OmniRoute CLIProxyAPI 集成

把 CLI 工具（Claude Code / Codex / Gemini CLI / Qwen Code 等）转成 OpenAI 兼容 API，供 OmniRoute 统一路由。

## 服务形态

| 项 | 值 |
|---|---|
| 上游项目 | `router-for-me/CLIProxyAPI` |
| 运行位置 | omniroute 容器内（omniroute-data 卷） |
| 端口 | 8317（需 docker-compose 映射 `8317:8317`） |
| 配置文件 | `/app/data/services/cliproxy/config.yaml` |
| 管理页面 | `http://vm002-ubuntu:8317/management.html` |

## 关键配置

1. `host` 从 `127.0.0.1` 改为 `0.0.0.0`（备份 config.yaml.bak）
2. `remote-management.secret-key` **必须配置**，否则 `/v0/management/*` 全 404、管理页登录不了；密钥见 `~/.openclaw/.env` 的 `OMNIROUTE_MANAGE_KEY`，并设 `allow-remote: true`
3. `version_manager.provider_expose = 1`，否则模型进不了路由（0 = fallback-only，CLIProxyAPI 默认）

## 踩坑：面板状态与数据库不一致

- 面板状态取自内存 supervisor（`getSupervisor(tool).getStatus().state`），status route 逻辑为 `state: liveStatus?.state ?? row?.status`
- 手动 `docker exec` 起的进程与 supervisor spawn 的进程抢 8317 → `bind: address already in use` → 面板 stopped/error
- 修复顺序：杀光 cliproxyapi 进程 → version_manager.status 重置 stopped → `docker restart omniroute` → supervisor auto_start
- 面板显示 running 时不要重复点「启动」

## 其他

- APIKey.fun 只是赞助商广告（README 致谢 + 返佣链接），非必需
- kimi：CLI OAuth 走免费额度、含 code 系列模型，比 OmniRoute 直连 kimi web provider 更省心

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
