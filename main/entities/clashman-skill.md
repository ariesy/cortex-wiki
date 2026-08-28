---
pageType: entity
id: entity.tool.clashman-skill
title: clashman 技能
entityType: tool
aliases:
  - clashman
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.clashman.origin
    text: "clashman 技能于 2026-04-06 基于需求规划创建，属于 OpenClaw 运维/网络排查类技能。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-06-clashman-test-8c8c3a8c
        weight: 0.85
  - id: claim.clashman.relocated
    text: "clashman 后续已从 main workspace 迁移到 `workspace-ops-deck/skills/` 目录，与 cf-docker-registry、ob-man、gh-tracker、openclaw-upgrade-check 等运维技能同址。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-22-0733-11f918d9
        weight: 0.85
  - id: claim.clashman.provider-lookup
    text: "排查 clashman / opencode 模型流量走向时，配置中真正的 provider 对象在 `models.providers.<id>` 下（如 opencode / opencode-go / opencode-go-responses），不是顶层 `providers`——定位模型挂载位置必须看这一层。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1627-c99c35d2
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-06-clashman-test-8c8c3a8c.md
  - sources/bridge-workspace-142ea9a2-memory-2026-08-22-0733-11f918d9.md
  - sources/bridge-workspace-142ea9a2-memory-2026-08-16-1627-c99c35d2.md

---
# clashman 技能

OpenClaw 运维类技能，用于代理/网络流量相关排查。

## 位置变迁

| 阶段 | 位置 |
|------|------|
| 2026-04 创建 | main workspace skills |
| 2026-08 之后 | `workspace-ops-deck/skills/` |

与 `cf-docker-registry`、`ob-man`、`gh-tracker`、`openclaw-upgrade-check` 一起迁到 ops-deck。

## 排查要点

排查 clashman / opencode 模型的流量走向时：

- **真正的 provider 对象在 `models.providers.<id>`**，而非顶层 `providers`
- 已知 provider id：`opencode`、`opencode-go`、`opencode-go-responses`
- 要确认模型挂在哪个 provider、host 指向哪里，从这一层读

## 相关

- [[git-clone-tls-issue]] — 同属 VM 网络/代理排查领域

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
