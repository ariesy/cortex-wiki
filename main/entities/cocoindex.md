---
pageType: entity
id: entity.tool.cocoindex
title: CocoIndex
entityType: tool
aliases:
  - cocoindex
  - CocoIndex 增量数据框架
updatedAt: 2026-08-05T15:11:28.000Z
status: active
claims:
  - id: claim.cocoindex.positioning
    text: "CocoIndex 是面向 AI Agent 的增量数据框架，Python 编写、核心引擎用 Rust 实现，核心理念是 \"React — for data engineering\"：开发者声明目标状态，引擎自动计算最小增量工作保持同步。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-cocoindex-summary-1e6c3af9
        weight: 0.85
  - id: claim.cocoindex.incremental
    text: "CocoIndex 的核心能力是增量处理：源数据变化只 re-index 变化部分（1 个文件编辑 → 1 行重新同步）；代码逻辑变更时仅受影响的行 re-run，缓存命中率 94%+。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-cocoindex-summary-1e6c3af9
        weight: 0.8
  - id: claim.cocoindex.features
    text: "CocoIndex 主要功能：语义搜索与 Index（支持呼叫图 call graphs 与影响范围 blast radius 分析）、跨源数据整合（localfs/PDF/Postgres/视频/Slack/Meeting notes → 向量数据库/Kafka）、声明式编程模型（F(Source) 变换 + @coco.fn(memo=True) 输入 hash 缓存）、CocoInsight 实时可观测性。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-cocoindex-summary-1e6c3af9
        weight: 0.8
  - id: claim.cocoindex.users
    text: "CocoIndex 面向 AI Coding Agent 开发者、RAG 应用开发者、数据工程师、安全/Code Review Agent 以及企业数据团队，解决数据陈旧、全量重建成本高、Agent 推理质量差、Schema 迁移麻烦、调试不透明等痛点。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-cocoindex-summary-1e6c3af9
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-06-cocoindex-summary-1e6c3af9.md
---
# CocoIndex

面向 AI Agent 的**增量数据框架**，Python 编写、核心引擎用 Rust 实现。核心理念：**"React — for data engineering"** —— 开发者声明目标状态，引擎自动计算最小增量工作来保持同步。仓库：github.com/cocoindex-io/cocoindex

## 解决的问题

| 痛点 | CocoIndex 的解法 |
|------|-----------------|
| 数据陈旧（批处理 pipeline 有 context gap） | 增量引擎，源数据变化后**亚秒级**感知，只重新处理变化部分 |
| 全量重建成本高 | **Δ-only**：变化的文件才 re-embed，其他缓存复用 |
| AI Agent 推理质量差 | 端到端 lineage，每条数据可溯源到源文件 |
| Schema 迁移麻烦 | 代码变更时**仅影响到的行重新运行** |
| 调试不透明 | **CocoInsight** 实时可视化每个 step、每条记录 |

## 核心功能

1. **增量处理** — 1 个文件编辑 → 1 行重新同步；代码逻辑变化仅受影响行列 re-run，缓存命中率 94%+
2. **语义搜索 & Index** — 非 grep 式字符串匹配，按语义/意图搜索（函数、模式、代码意图）；支持呼叫图（call graphs）与影响范围分析（blast radius）
3. **跨源数据整合** — 代码库（localfs）、PDF、数据库（Postgres）、视频、Slack、Meeting notes → 向量数据库 embedding、Kafka
4. **声明式编程模型** — 开发者写 `F(Source)` 变换，引擎自动推导 DAG 并增量执行；`@coco.fn(memo=True)` 做输入 hash 缓存
5. **CocoInsight 可观测性** — 实时渲染 pipeline 状态，每条向量可追溯到原始段落

## 面向用户

| 用户类型 | 使用场景 |
|---------|---------|
| AI Coding Agent 开发者 | 让 agent 在最新代码库上工作（生成/重构/审查） |
| RAG 应用开发者 | 将代码、文档、PDF 实时同步到向量数据库 |
| 数据工程师 | 构建增量 ETL pipeline，避免全量重建 |
| 安全 / Code Review Agent | 代码变更影响分析、漏洞扫描 |
| 企业数据团队 | 跨 PB 级数据源保持 AI 应用的数据一致性 |

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
