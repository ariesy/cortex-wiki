---
pageType: entity
id: entity.concept.architecting-with-small-models
title: 中小模型（27B/256k）做系统架构设计的范式
entityType: concept
aliases:
  - small model architecture design
  - 27B 模型架构设计
  - openspec 上层架构层
  - 弱模型架构设计范式
updatedAt: 2026-08-13T13:57:29.052Z
status: active
claims:
  - id: claim.small-model.attention-decay
    text: 27B 级模型配 256k context 时，瓶颈不是 context 窗口不够，而是超长上下文里的注意力衰减（lost in the middle）——256k 名义容量下有效注意力可能只有 10-20k；因此换工具解决不了根本问题，要换的是设计范式：把大问题切成小问题，用结构化产物把「全局一致性」从模型上下文搬进仓库。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1357-3712e0dc
        weight: 0.8
  - id: claim.small-model.openspec-gap
    text: openspec 的 specs/ + changes/ 结构本质是「棕地增量」SDD：默认架构已既定，不主动产出系统级设计；所以要补的是它上面缺的架构层，而不是替换 openspec。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1357-3712e0dc
        weight: 0.8
  - id: claim.small-model.six-practices
    text: 推荐组合六条：①人机分工反转（人当架构师拍板，模型当多方案生成器 + 对抗评审员）；②C4 分层渐进（Context→Container→Component，每层一轮只喂上一层结果 + 本层相关文件）；③契约先行（OpenAPI/JSON Schema/protobuf，人审契约后再作为 openspec spec 输入）；④ADR 决策日志 + 架构测试兜底（ArchUnit / NetArchTest / import-linter 把分层与禁循环依赖写进 CI）；⑤上下文管理抄 Roo Code Memory Bank 模式，opencode 侧用 AGENTS.md 分层；⑥opencode 多 subagent 角色分离（architect 只读出 DSL/契约、reviewer 评审、implementer 按 spec 实现）+ MCP 接代码图谱（Sourcegraph/CodeGraph 类）降低幻觉。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1357-3712e0dc
        weight: 0.8
  - id: claim.small-model.structurizr
    text: 架构中间产物用 Structurizr DSL（架构即代码）落盘：可渲染、可 diff、可评审，模型生成 DSL 比生成大段 prose 可靠得多。
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1357-3712e0dc
        weight: 0.75
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-08-13-1357-3712e0dc.md
---

# 中小模型（27B/256k）做系统架构设计的范式

场景：公司内网 opencode + 内部 LLM，只有 qwen-3.6-27b 可用，context ≈ 256k，已用 openspec 做 delta 式 SDD，但缺系统级架构设计能力。

## 核心判断

**瓶颈不是 context 窗口，而是有效注意力。** 27B 在长上下文里注意力衰减（lost in the middle），256k 名义值实际可用 10-20k。所以策略只有一条：**切小问题 + 结构化落盘**，把全局一致性从模型脑子里搬到仓库里。

## 六条落地做法

| # | 做法 | 要点 |
|---|------|------|
| 1 | 人机分工反转 | 人定边界拍板；模型做局部推理——挑毛病、补细节、给每个决策点 2-3 个方案对比 |
| 2 | C4 分层渐进 | Context → Container → Component，每层一轮，只喂「上一层结果 + 本层相关文件」 |
| 3 | 契约先行 | 模块边界与接口契约（OpenAPI / JSON Schema / protobuf）是最值钱的资产；契约草案模型出、人审 |
| 4 | ADR + 架构测试 | ADR（adr-tools / MADR）防「忘记为什么」；ArchUnit / NetArchTest / import-linter 把分层依赖写进 CI 防悄悄腐化 |
| 5 | 上下文管理 | 抄 Roo Code Memory Bank：核心文件常驻 + 详细文档按需加载；opencode 侧用 AGENTS.md 分层，根级只放稳定事实 |
| 6 | 角色分离 + 代码图谱 | subagent 拆 architect（只读，产 DSL/契约）/ reviewer / implementer；MCP 接 Sourcegraph、CodeGraph 类图谱照真实依赖推理 |

## 工作流

```
人 + 模型画 Container 层 → 人拍板
  → 每个 Container 产 Structurizr DSL + 契约草案 → 人审
    → 契约定稿作为 openspec spec 输入 → 此后 delta 开发在既定边界内填空
```

## 关键洞见

- **Structurizr DSL（架构即代码）比大段 prose 更适合小模型**：可渲染、可 diff、可评审、可校验。
- **架构测试是对模型能力不足的工程化补偿**——模型写飘了，CI 会拦。
- 契约审完再进 openspec，模型就从「自由发挥」变成「边界内填空」。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
