---
pageType: entity
id: entity.bug.screening-history-restore
title: Screening 历史 Run 恢复缺陷（策略上下文丢失 + 过期响应竞态）
entityType: bug
aliases:
  - screening-history-restore
  - 历史 run 恢复策略上下文丢失
  - Ignore stale history-detail responses
updatedAt: "2026-08-16T01:55:04.359Z"
status: resolved
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-16-0155-5aba2907
claims:
  - id: claim.screening-history.restore-strategy-context
    text: "历史 run 恢复时（handleHistoryRunSelect 及挂载时 runId 恢复分支）未同步策略/市场上下文，导致结果区文案与后续深度分析的 analysisSkills 使用的是当前页面策略而非历史 run 的策略。修复：两处恢复路径均从 ScreeningRunDetail 同步 strategy/market 到页面 state。对应 Codex P2「Restore strategy with result」与 ZhuLinsen blocker OR-COR-6c1e5d27。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0155-5aba2907
        weight: 0.9
  - id: claim.screening-history.stale-response-race
    text: "快速切换历史条目时，过期详情响应会覆盖最新结果（响应竞态）。修复：参照现有 hotspot 的 requestIdRef 模式，新增 historyRunRequestIdRef 跟踪最新请求序号，响应返回时校验是否仍是最新请求，过期响应直接忽略；并补回归测试覆盖快速切换场景。对应 Codex P2「Ignore stale history-detail responses」。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0155-5aba2907
        weight: 0.9
  - id: claim.screening-history.changelog-and-verification
    text: "同轮修复中 CHANGELOG 条目从已发布的 [3.30.0] 移到 [Unreleased]（Codex P2「Keep changelog under Unreleased」）。修复提交 063ed75b（策略上下文同步 + CHANGELOG）与 886b73b9（竞态防护），位于分支 bugfix/screening-history-restore，30 个测试全部通过。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0155-5aba2907
        weight: 0.85
---

# Screening 历史 Run 恢复缺陷

## 概述

选股（screening）页面「历史 run 恢复」功能存在两个问题，在 2026-08-15 一轮 code review（Codex P2 × 3 + ZhuLinsen blocker）后修复，分支 `bugfix/screening-history-restore`。

## 修复清单

| 提交 | 内容 | 对应意见 |
|------|------|---------|
| `063ed75b` | 历史 run 恢复时同步策略/市场上下文（两处恢复路径） | Codex P2「Restore strategy with result」+ blocker `OR-COR-6c1e5d27` |
| `063ed75b` | CHANGELOG 条目从 `[3.30.0]` 移到 `[Unreleased]` | Codex P2「Keep changelog under Unreleased」 |
| `886b73b9` | 忽略过期历史详情响应（`historyRunRequestIdRef` 竞态防护） | Codex P2「Ignore stale history-detail responses」 |

## 技术细节

- 策略上下文：`handleHistoryRunSelect` 与挂载时 runId 恢复分支均从 `ScreeningRunDetail` 同步 `strategy`/`market` 到页面 state。
- 竞态防护：沿用现有 hotspot 的 `requestIdRef` 模式；测试定位时需用 `role=button` 而非 `getByText('Dual Low')`（策略下拉 option 与历史条目 span 文本重复）。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-16-0155](../sources/bridge-workspace-142ea9a2-memory-2026-08-16-0155-5aba2907.md)
<!-- openclaw:wiki:related:end -->
