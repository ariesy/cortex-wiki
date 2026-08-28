---
pageType: entity
entityType: project
id: entity.project.investsignal-sprint8-sentiment-signal
updatedAt: "2026-08-28"
relationships:
  - targetId: entity.project.investsignal-sprint8-etf-signal
    targetTitle: "InvestSignal Sprint 8：ETF 基本面信号与规模追踪"
    kind: related
    weight: 0.7
  - targetId: entity.project.investsignal-architecture-v1-1
    targetTitle: "InvestSignal 架构设计 v1.1"
    kind: belongs-to
    weight: 0.8
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-03-22-sentiment-signals-64c692b3
---

# InvestSignal Sprint 8：情绪面信号计算（S8-T12）

> entity_type: project

InvestSignal 项目 Sprint 8 的 S8-T12 任务（2026-03-22）：建立新闻情绪面信号计算链路，补齐五维分析框架中的情绪面维度。

---

## 交付成果

新增模块 `src/analyzer/indicators/sentiment/`：

| 模块 | 说明 |
|------|------|
| `models.py` | `SentimentSignal`, `NewsSentiment`, `CredibilityWeight` |
| `collector.py` | 从 MXNewsCollector 收集新闻 |
| `analyzer.py` | 使用 OpenClaw LLM 分析情绪（带 fallback） |
| `calculator.py` | 情绪信号计算（可信度加权） |
| `heat_detector.py` | 讨论热度检测 |
| `dao.py` | 数据库持久化 |

---

## 任务与测试

| T# | 任务 | 文件 | 测试 |
|----|------|------|------|
| T1 | 数据模型 | `models.py` | 13 passed |
| T2 | 情绪数据收集器 | `collector.py` | 10 passed |
| T3 | 情绪分析器 | `analyzer.py` | 41 passed |
| T4 | 情绪信号计算器 | `calculator.py` | 27 passed |
| T5 | 讨论热度检测器 | `heat_detector.py` | 15 passed |
| T6 | 情绪数据 DAO | `dao.py` | 9 passed |
| T7 | 集成测试 | `tests/` | 23 passed |

**总测试：138+ passed**

---

## Sprint 8 状态（截至 2026-03-22）

| 任务 | 状态 | 故事点 |
|------|------|--------|
| S8-T8: 基金基本面信号研究 | ✅ Done | 2 |
| S8-T9: 观察列表变动触发收集 | ✅ Done | 3 |
| S8-T11: 宏观面信号计算 | ✅ Done | 4 |
| S8-T12: 情绪面信号计算 | ✅ Done | 4 |

---

*来源: memory/2026-03-22-sentiment-signals.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-03-22-sentiment-signals](../sources/bridge-workspace-142ea9a2-memory-2026-03-22-sentiment-signals-64c692b3.md)
<!-- openclaw:wiki:related:end -->
