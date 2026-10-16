---
pageType: entity
id: entity.bug.tradingagents-llm-cache-miss
title: TradingAgents LLM API 缓存命中率异常低
entityType: bug
aliases:
  - TradingAgents 缓存命中率低
  - TradingAgents prompt cache 失效
  - TradingAgents LLM cache miss
updatedAt: 2026-08-05T15:11:28.000Z
status: identified
claims:
  - id: claim.tradingagents-cache.no-cache-layer
    text: "TradingAgents 项目完全没有实现任何缓存层：未使用 LangChain LLM Cache (`langchain.cache`)、未使用 Anthropic `cache_control`/prompt caching、未配置 OpenAI prefix caching、无自定义缓存逻辑；`cache_control`/`ephemeral` 关键词在 `tradingagents/` 目录零匹配。"
    status: supported
    confidence: 0.95
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-tradingagents-cache-debug-956f8750
        weight: 0.95
  - id: claim.tradingagents-cache.architecture-calls
    text: "一次完整 pipeline 涉及 13+ 次 LLM 调用：Market Analyst → Social Analyst → News Analyst → Fundamentals Analyst → Bull/Bear Debate(default 2 rounds) → Research Manager → Trader → Aggressive/Conservative/Neutral Risk Debate(default 3 rounds) → Portfolio Manager；每个 Analyst 阶段还有 tool-calling 循环，实际调用次数更多。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-tradingagents-cache-debug-956f8750
        weight: 0.9
  - id: claim.tradingagents-cache.bug1-dynamic-prefix
    text: "Bug 1（破坏 prefix matching）：所有 4 个 Analyst 的 prompt 构建（`market_analyst.py`、`social_media_analyst.py`、`news_analyst.py`、`fundamentals_analyst.py`）用 `prompt.partial(current_date=current_date)` 与 `prompt.partial(instrument_context=instrument_context)` 注入变化值。OpenAI 自动缓存要求前 1024 token 完全相同，而 `current_date`（每天不同）和 `instrument_context`（每个 ticker 不同，如 AAPL vs TSLA）嵌入在 system message 中，导致不同 ticker/日期的调用从第一个 token 就不同，缓存完全无法命中。影响所有 4 个 Analyst agent 的每次调用。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-tradingagents-cache-debug-956f8750
        weight: 0.9
  - id: claim.tradingagents-cache.bug2-msg-delete
    text: "Bug 2：`create_msg_delete()` 在每个 Analyst 之间清除消息历史，导致消息历史无法跨 Analyst 阶段复用为缓存前缀。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-tradingagents-cache-debug-956f8750
        weight: 0.8
  - id: claim.tradingagents-cache.five-root-causes
    text: "分析报告共列出 5 个导致缓存命中率极低的根本原因，均围绕 prompt 构建方式破坏 API 级缓存的前缀匹配条件。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-tradingagents-cache-debug-956f8750
        weight: 0.8
relationships:
  - targetId: entity.project.tradingagents
    targetTitle: tradingagents
    kind: affects
    weight: 0.95
    note: 缺陷归属项目；tradingagents 为 AI 对冲基金多 Agent 模拟系统
  - targetId: concept.llm-prompt-prefix-caching
    targetTitle: LLM Prompt 前缀缓存
    kind: related-concept
    weight: 0.8
    note: OpenAI 自动缓存要求前 1024 token 完全一致才能命中
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-06-tradingagents-cache-debug-956f8750.md
---

# TradingAgents LLM API 缓存命中率异常低

> 使用 superpowers 技能 Phase 4 Systematic Debugging 流程对 `/app/TradingAgents` 做的只读根因分析（未做代码修改）。

## 核心结论

**项目完全没有实现任何缓存层**，且现有 prompt 构建方式会破坏 API 级缓存的 prefix matching 条件。

## 5 个根本原因

| # | 问题 | 位置 |
|---|------|------|
| 1 | 每次调用动态注入变化值（`current_date` / `instrument_context`），破坏 prefix matching | 全部 4 个 Analyst 的 prompt 构建 |
| 2 | `create_msg_delete()` 在每个 Analyst 之间清除消息历史 | `tradingagents/` |
| 3 | （见源报告） | — |
| 4 | （见源报告） | — |
| 5 | （见源报告） | — |

## 已核查项

| 检查项 | 结果 |
|--------|------|
| LangChain LLM Cache (`langchain.cache`) | ❌ 未使用 |
| Anthropic `cache_control` / prompt caching | ❌ 未使用 |
| OpenAI prefix caching 配置 | ❌ 未使用 |
| 自定义缓存逻辑 | ❌ 无 |
| `cache_control` / `ephemeral` 关键词 | ❌ 整个 `tradingagents/` 目录零匹配 |

## 缓存原理要点

OpenAI 自动缓存要求**前 1024 个 token 完全相同**才能命中。当 `current_date` 和 `instrument_context`（含 ticker）嵌入 system message 时，不同 ticker 或不同日期的调用从第一个 token 就开始不同。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
