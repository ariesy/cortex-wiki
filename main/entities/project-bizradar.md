---
pageType: entity
id: entity.project.bizradar
title: BizRadar
entityType: project
aliases:
  - bizradar
  - BizRadar 痛点挖掘
updatedAt: 2026-08-05T15:11:28.000Z
status: active
claims:
  - id: claim.bizradar.positioning
    text: "BizRadar 是 AI 用户痛点发现工具，扫描社交媒体（V2EX/HN/Reddit/微博/Twitter/AppStore）挖掘真实用户抱怨，通过 5 个 Agent（E/PM/Critic/TL/Planner）流水线输出完整 PRD + 分享卡片，MIT 开源。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-0047-25a55ec3
        weight: 0.85
  - id: claim.bizradar.differentiator
    text: "BizRadar 的差异点是 Critic Agent 量化打分，用于过滤伪需求；5 Agent 流水线设计比大多数竞品更系统化，PRD 输出 + 分享卡片解决了「输出后怎么用」的问题。在该细分领域属于功能最完整的开源方案之一。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-0047-25a55ec3
        weight: 0.8
  - id: claim.bizradar.limitations
    text: "BizRadar 的局限：数据源依赖爬虫/API、长期维护成本高；评分体系封闭、未经过市场验证；实际商业价值取决于 LLM 的指令遵循质量。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-0047-25a55ec3
        weight: 0.8
  - id: claim.bizradar.competitors
    text: "同类竞品：海外有 IdeaPicker（Reddit 痛点挖掘）、Pain Point Discovery Tools 系列、PrometAI（商业计划生成）、Discovery Agent/BusinessOptix（企业内部流程发现）；国内有 DeepPoint（智谱 AI，社交媒体聚类 + PRD 生成）、墨刀 AI Agent（全链路产品调研）、Signlz AI（PRD 拆解）、火山引擎 ADG（Agent 竞品分析 + 原型）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-0047-25a55ec3
        weight: 0.85
  - id: claim.bizradar.api-dependency
    text: "源码分析确认 BizRadar 的必填 API Key 包括 LLM_API_KEY（LLM 调用，支持 DeepSeek / 云雾API / Kimi 等）。"
    status: supported
    confidence: 0.7
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-0047-25a55ec3
        weight: 0.7
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-07-0047-25a55ec3.md
---

# BizRadar

> AI 用户痛点发现 + PRD 生成工具，5 Agent 流水线，MIT 开源。

## 定位

| 维度 | 说明 |
|------|------|
| **定位** | AI 用户痛点发现器，从社交媒体真实抱怨中提炼创业机会 |
| **数据源** | V2EX / HN / Reddit / 微博 / Twitter / AppStore |
| **Agent 数量** | 5 个（E / PM / Critic / TL / Planner） |
| **输出** | 完整 PRD + 分享卡片 |
| **评分机制** | Critic Agent 量化打分 |
| **Web UI** | 可视化大盘 |
| **开源** | MIT |

## 差异点

1. **5 Agent 流水线设计** — 比大多数竞品更系统化
2. **Critic Agent 量化打分** — 帮用户过滤伪需求
3. **PRD 输出 + 分享卡片** — 解决「输出后怎么用」

## 竞品格局

| 竞品 | 定位 |
|------|------|
| IdeaPicker | AI 创业点子发现器（专注 Reddit，仅出点子） |
| PrometAI | AI 商业计划生成器 |
| DeepPoint | AI 用户痛点发现器（智谱 AI） |
| 墨刀 AI Agent | 全链路产品调研 |
| Signlz AI | PRD 辅助生成 |
| 火山引擎 ADG | AI 竞品分析 + 原型 |

## 局限

- 数据源依赖爬虫/API，长期维护成本高
- 评分体系封闭，未经过市场验证
- 实际商业价值取决于 LLM 的指令遵循质量

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
