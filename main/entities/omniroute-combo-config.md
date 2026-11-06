---
pageType: entity
id: entity:omniroute-combo
entityType: concept
entity_type: tool_config
privacyTier: public
name: OmniRoute Combo（多模型路由配置）
aliases:
  - omniroute combo
  - OmniRoute handoffThreshold
  - OmniRoute context-relay
category: AI 基础设施 / LLM 路由
last_updated: 2026-08-11
updatedAt: 2026-08-11T00:21:53.714Z
status: verified
summary: |
  本机 OmniRoute（v3.8.49）的 combo 是「一组模型 + 策略 + 升级/兜底参数」的路由单元；增强智能的可用手段包括 handoff（context-relay）、fusion 多模型投票、auto/smart 模式、context-relay 交接摘要，以及 comboAutoPromoteEnabled 等全局开关。实测结论：handoffThreshold/handoffModel 按「上游配额消耗百分比」触发，不是回答质量评分。
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-11-0021-e73dd80b
claims:
  - id: claim.entity.omniroute-combo.enhance-intelligence-20260811
    text: OmniRoute v3.8.49 中与"增强模型智能"相关的 combo 配置：①handoffThreshold/handoffModel（弱模型兜底、强模型升级，本机 freetier/freetierv/freetier-pro 的 handoffModel 均为空，未启用）；②fusion 策略（多模型并行 + judge 模型综合），以及 pipeline，这两者在 v3.8.49 的 OpenAPI 枚举里尚不存在（仅有 14 种策略），需升级版本；③auto/smart 模式（质量优先 + 10% 探索，另有 auto/LKGP 最近成功路径、auto/coding 代码质量优先）；④context-relay 策略（长对话跨模型接力时生成结构化交接摘要）；⑤全局开关 comboAutoPromoteEnabled（默认 false，开启后按 /api/combos/metrics 自动提升最佳模型为主模型）与 reasoningTokenBufferEnabled（默认 true）。
    status: supported
    confidence: 0.8
    evidence:
      - kind: source-code
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-11-0021-e73dd80b
        weight: 0.85
    updatedAt: 2026-08-11T00:21:53.714Z
  - id: claim.entity.omniroute-combo.handoff-threshold-semantics-20260811
    text: 纠正认知：handoffThreshold/handoffModel 不是"回答质量评分"，而是 context-relay 功能的一部分，评分标准为上游配额消耗百分比。源码 contextHandoff.ts + combo.ts 显示生成 handoff 需同时满足：①strategy 为 context-relay（或通用 handoff 开启且发生模型切换）；②provider 命中 handoffProviders（默认仅 codex）；③percentUsed ≥ handoffThreshold。配置可通过 PATCH /api/combos/{id} 修改。
    status: supported
    confidence: 0.8
    evidence:
      - kind: source-code
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-11-0021-e73dd80b
        weight: 0.85
    updatedAt: 2026-08-11T00:21:53.714Z
---

# OmniRoute Combo（多模型路由配置）

## 背景

OmniRoute（本机 v3.8.49）的 combo = 模型组 + 策略 + 升级/兜底参数。目标：在不换模型的情况下"增强智能"。

## 五种手段

| 手段 | 机制 | 本机状态 |
|------|------|----------|
| handoffThreshold / handoffModel | 触发条件满足时切换到 `handoffModel` | freetier / freetierv / freetier-pro 的 `handoffModel` 均为空 → 未启用 |
| fusion 策略 | 一组模型并行请求 + judge 模型综合出最佳答案 | v3.8.49 枚举里没有（需升级） |
| auto / smart 模式 | 质量优先 + 10% 探索；另有 `auto`（LKGP）、`auto/coding` | 可用 |
| context-relay 策略 | 跨模型接力时生成结构化交接摘要，保持会话连续性 | 可用 |
| 全局开关 | `comboAutoPromoteEnabled`（默认 false，配合 `/api/combos/metrics` 自动提升最佳模型）、`reasoningTokenBufferEnabled`（默认 true） | 前者未开 |

## ⚠️ 关键纠错：handoffThreshold 的语义

不是「模型回答质量评分」，而是 **context-relay 的上游配额消耗百分比**。源码 `contextHandoff.ts` + `combo.ts`：

1. `strategy` 为 `context-relay`（或通用 handoff 开启且发生模型切换）；
2. provider 命中 `handoffProviders`（默认只有 `codex`）；
3. `percentUsed ≥ handoffThreshold`。

三条同时满足才生成 handoff。配置方式：`PATCH /api/combos/{id}`。

## 最低成本建议

先把 `freetier` 或 `freetier-pro` 的 `handoffModel` 配成强模型（如 deepseek-v4-pro），即可获得"弱模型兜底、强模型升级"；fusion 需先升级 OmniRoute。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-11-0021](../sources/bridge-workspace-142ea9a2-memory-2026-08-11-0021-e73dd80b.md)
<!-- openclaw:wiki:related:end -->
