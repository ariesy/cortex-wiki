---
pageType: entity
entityType: project
id: entity.project.stock-research-engine
updatedAt: "2026-05-29"
claims:
  - id: claim.stock-research-engine.core
    text: "多Agent辩论系统，通过多维度分析生成投资决策"
    status: supported
    confidence: 0.8
    evidence:
      - kind: entity-summary
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-29-memory-sources
        weight: 0.9
relationships:
  - targetId: entity.project.tradingagents
    targetTitle: "tradingagents"
    kind: similar-approach
    weight: 0.8
    note: "同为AI Agent投资分析系统"
  - targetId: entity.project.investsignal
    targetTitle: "InvestSignal"
    kind: related-system
    weight: 0.7
    note: "InvestSignal关注信号，此框架关注分析"
---


# stock-research-engine

> 多维度股票分析框架，通过多Agent辩论生成投资决策

**类型:** Project  
**状态:** active  
**ID:** `project_stock_research_engine`  
**来源:** 多次实际使用

---


## 基本信息

| 项目 | 内容 |
|------|------|
| **名称** | stock-research-engine |
| **类型** | 投资分析框架 |
| **位置** | `~/.openclaw/skills/stock-research-engine` |
| **技术栈** | Python, tushare, agent-framework |
| **状态** | 活跃使用中 |

---

## 核心功能

- 多维度估值分析
- 技术面分析
- 基本面分析
- 市场情绪分析
- 投资决策输出（买入/卖出/持有）

---

## 已分析标的

| 标的 | 代码 | 结论 | 分析日期 |
|------|------|------|----------|
| 京东集团 | 9618.HK | 卖出(Underweight) | 2026-05-06 |
| 中国神华 | 601088 | ⭐⭐⭐⭐强烈推荐 | 2026-04-16 |
| 澜起科技 | 688008.SH | 高弹性预期驱动 | 2026-05-14 |
| 华夏芯片ETF | 159995.SZ | 减持 | 2026-05-06 |
| 恒生科技ETF | 513180 | 低估值+高增长组合 | 2026-05-07 |

---

## 技术架构

通过多Agent团队协作（买方基金经理视角），收集多维度数据后进行辩论评分，最终输出投资建议。

---

*来源: memory/2026-05-06-chip-etf-analysis.md 等*

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
