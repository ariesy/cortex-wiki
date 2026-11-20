---
pageType: entity
id: entity.concept.deepseek-harness
title: "DeepSeek Harness（dsh）"
entityType: concept
aliases:
  - dsh
  - DeepSeek Harness
  - deepseek-harness
  - dsh-plugin
tags: [deepseek, agent-framework, cordis, plugin, dsh]
updatedAt: "2026-08-15"
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-15-1412-9e518dbc
claims:
  - id: claim.dsh.overview
    text: "DeepSeek Harness（dsh）是 DeepSeek AI 于 2026 年 8 月发布的开源 agent 框架，MIT 协议，核心设计是「一切皆插件」：模型、工具、skills、session、沙箱、agent loop 均为插件，用 Cordis 框架组合成 profile。发布数日 GitHub stars 达 3.3 万+，仍是 developer preview，官方明说会有破坏性变更。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-15-1412-9e518dbc
        weight: 0.85
  - id: claim.dsh.plugin-discovery
    text: "dsh 生态暂无官方集中式插件 hub（类比 ClawHub）。官方唯一发现机制是 GitHub topic `dsh-plugin`（github.com/topics/dsh-plugin），交流走 GitHub Discussions + Discord，插件以 npm 包分发、用 `dsh plugin install` 安装（底层 pnpm）。第三方 registry 已在填空：dshplugin.world（自称 DeepSeek Harness Plugin Registry，爬 topic 去噪后生成静态页与安装命令）与 dshpluginstore.com（人工策划的插件商店，带 star 与评价）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-15-1412-9e518dbc
        weight: 0.8
  - id: claim.dsh.ecosystem-judgement
    text: "dsh 插件生态仍处早期：官方 API 未稳定、破坏性变更随时可能发生，第三方 registry 数量与质量不足，GitHub topic 水分大（topic 页显示 3355 个仓库，实际核查 411 个中仅 29 个被确认）。当前最可靠路径是 GitHub topic 交叉验证 + 两个第三方目录参考，安装前确认维护活跃度与版本适配。"
    status: observed
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-15-1412-9e518dbc
        weight: 0.75
---

# DeepSeek Harness（dsh）

## 概述

- 2026 年 8 月由 DeepSeek AI 开源，MIT 协议，GitHub stars 3.3 万+（发布数日）
- 设计哲学：**一切皆插件**（模型 / 工具 / skills / session / 沙箱 / agent loop）
- 组合方式：Cordis 框架 + profile
- 状态：developer preview，官方明言会有破坏性变更

## 插件生态（2026-08 快照）

| 渠道 | 说明 |
|---|---|
| 官方 | 无 registry；用 GitHub topic `dsh-plugin` 做发现；Discussions + Discord 交流 |
| 安装 | npm 包 + `dsh plugin install`（底层 pnpm） |
| 第三方 | dshplugin.world（可爬取目录）、dshpluginstore.com（人工策划商店） |

水分提示：GitHub topic 页 3355 个仓库匹配，快照核查的 411 个中仅 29 个确认。

## 判断

生态太早期，官方 registry 大概率会补上；现阶段靠 topic 交叉验证 + 关注维护活跃度与版本适配。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-15-1412](../sources/bridge-workspace-142ea9a2-memory-2026-08-15-1412-9e518dbc.md)
<!-- openclaw:wiki:related:end -->
