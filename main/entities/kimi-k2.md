---
pageType: entity
id: entity.model.kimi-k2
title: Kimi K2（Moonshot AI）
entityType: concept
aliases:
  - Kimi K2.5
  - Kimi K2.6
  - MoonshotAI Kimi
updatedAt: 2026-08-28T16:05:00.000Z
status: active
claims:
  - id: claim.kimi-k2.layer-distinction
    text: "对比 Kimi K2 与 Claude Code 必须分两层看：Kimi 是基础模型（可接 Cursor / Windsurf / Trae / Cline），Claude Code 是「Claude 模型 + 专用 agentic harness」，把模型分数和工具体验混谈是常见误判。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-kimi-k2-vs-claude-code-compari-619dd649
        weight: 0.9
  - id: claim.kimi-k2.benchmark
    text: "Kimi K2.6 官方 benchmark：SWE-Bench Verified 80.2（Opus 4.6 为 80.8，基本持平）、SWE-Bench Pro 58.6 反超 Opus 的 53.4、Terminal-Bench 2.0 66.7 领先；但 Claw Eval (pass^3) 62.3 明显落后于 Claude 的 70.4。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-kimi-k2-vs-claude-code-compari-619dd649
        weight: 0.8
  - id: claim.kimi-k2.reliability-gap
    text: "Claude Code 的护城河在 harness 而非模型：plan mode、CLAUDE.md 上下文管理、工具调用优化、权限控制构成工程壁垒；Claw Eval 上的领先说明「连续多次正确执行」的可靠性更好，对 production coding agent 比单峰 benchmark 更重要。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-kimi-k2-vs-claude-code-compari-619dd649
        weight: 0.8
  - id: claim.kimi-k2.instruction-following
    text: "「Kimi K2 中文指令遵循差」需按版本区分：K2 初版（2025-07）确有 QAT 优化方向与用户需求脱节、heavy 模式不稳定等反馈；K2.5 起被 Cursor 选作 Composer 2 基座，指令遵循已达生产级；K2.6 进一步提升。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-kimi-k2-vs-claude-code-compari-619dd649
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-30-kimi-k2-vs-claude-code-compari-619dd649.md
relationships:
  - targetId: entity.tool.claude-code
    targetTitle: "Claude Code"
    kind: compared-with
    weight: 0.9

---
# Kimi K2（Moonshot AI）

MoonshotAI 的基础模型系列，作为 Claude Code 的主要对标/替代被反复评估。

## Benchmark（K2.6，官方 Tech Blog）

| Benchmark | Kimi K2.6 | Claude Opus 4.6 | GPT-5.4 | Kimi K2.5 |
|-----------|-----------|-----------------|---------|-----------|
| SWE-Bench Verified | 80.2 | **80.8** | — | 76.8 |
| SWE-Bench Pro | **58.6** | 53.4 | 57.7 | 50.7 |
| SWE-Bench Multilingual | 76.7 | **77.8** | — | 73.0 |
| Terminal-Bench 2.0 | **66.7** | 65.4 | 65.4 | 50.8 |
| LiveCodeBench v6 | **89.6** | 88.8 | — | 85.0 |
| Claw Eval (pass^3) | 62.3 | **70.4** | 60.3 | 52.3 |

**读法**：峰值能力已追平甚至局部反超，但 agentic 工具调用的**可靠性**仍落后。

## 选型判断

- 单次/高难度工程任务 → Kimi K2.6 不输甚至更优（SWE-Bench Pro、Terminal-Bench）
- 长链路、需连续正确执行的 production agent → Claude Code 更稳（Claw Eval 差距明显）
- 生态层面：Claude Code 有 skill system、memory management 与成熟社区；Kimi 作为独立 agent harness 的生态仍在建设，目前主要靠 Cursor / Windsurf / Trae / Cline 接入

## 版本演进

| 版本 | 指令遵循 |
|------|---------|
| K2（2025-07） | 差，heavy 模式不稳定，QAT 优化方向与市场宣传脱节 |
| K2.5 | 明显改善，成为 Cursor Composer 2 基座 |
| K2.6 | 进一步提升（Factory.ai 评价 better instruction following） |

## Related
- [Claude Code](claude-code.md)

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Claude Code](claude-code.md)
<!-- openclaw:wiki:related:end -->
