---
pageType: entity
id: entity.concept.etf-technical-signal-scoring
title: ETF 技术面信号评分体系
entityType: concept
aliases:
  - 卖出信号评分
  - InvestSignal 技术面
  - KDJ RSI 共振
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.etf-scoring.formula
    text: "技术面综合得分由四个指标累加：MA（均线）、MACD、KDJ、RSI。每个指标给出持有(0)、买入(+1)或卖出(-1)，综合得分决定信号方向。以 2026-04-23 沪深300ETF(510300)为例：MA 持有0、MACD 持有0、KDJ 超买(J值>80) -1、RSI>70 -1，综合 -2 触发卖出信号。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-27-sell-signal-analysis-d61636b6
        weight: 0.8
  - id: claim.etf-scoring.confidence-formula
    text: "信号置信度计算公式：confidence = 30（基准）+ |score| × 20（方向加成）+ count × 10（一致性加成）。其中 count 为方向一致的指标数量。上例中 30 + 2×20 + 2×10 = 90%。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-27-sell-signal-analysis-d61636b6
        weight: 0.8
  - id: claim.etf-scoring.resonance-limitation
    text: "宽基 ETF 之间（如沪深300ETF 510300 与中证500ETF 510500）出现同向信号属于常态而非独立印证——两者走势高度相关，信号自然一致，不能简单当作'两个标的互相验证'来提升结论强度。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-27-sell-signal-analysis-d61636b6
        weight: 0.8
  - id: claim.etf-scoring.signal-nature
    text: "该体系产生的是纯技术面的短期风险信号，不代表中长期方向；KDJ 超买与 RSI>70 在强势行情中可能高位钝化（持续超买），需结合资金面（北向资金流向、ETF 份额变化）综合判断。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-27-sell-signal-analysis-d61636b6
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-27-sell-signal-analysis-d61636b6.md

---
# ETF 技术面信号评分体系

InvestSignal 的技术面打分逻辑，用于观察列表中 ETF 的每日自动分析。

## 指标与打分

| 指标 | 卖出条件 | 得分 |
|------|---------|------|
| MA（均线） | 跌破均线 | -1 |
| MACD | 死叉 | -1 |
| KDJ | 超买（J值 > 80） | -1 |
| RSI | > 70 | -1 |

各指标取 持有(0) / 买入(+1) / 卖出(-1)，累加得**综合得分**，得分符号决定信号方向。

**实例（2026-04-23 沪深300ETF 510300）**

| 指标 | 信号 | 得分 |
|------|------|------|
| MA | 持有 | 0 |
| MACD | 持有 | 0 |
| KDJ | 超买（J>80） | -1 |
| RSI | >70 | -1 |
| **综合** | **卖出** | **-2** |

## 置信度公式

```
confidence = 30（基准）
           + |score| × 20（方向加成）
           + count × 10（一致性加成）
```

`count` = 方向一致的指标数量。

上例：30 + 2×20 + 2×10 = **90%**。高置信度来自 KDJ 与 RSI 两个指标同时指向超买、方向一致互相印证。

## 仓位建议映射

综合得分 -2 时建议仓位 **0-10%**（空仓/极低仓位）。风险提示为短期回调风险，但也承认可能高位钝化。

## ⚠️ 两个容易误读的地方

**1. 宽基 ETF 同向信号不是独立印证。**

沪深300ETF 与中证500ETF 同日出现相同卖出信号、指标状态完全一致——这不构成"两个标的互相验证"。两者同涨同跌、走势高度相关，信号自然一致。它只能说明**整体大盘短期处于 KDJ 超买 + RSI 偏高状态**，不能靠"共振"来拔高结论强度。

**2. 这是短期风险信号，不是趋势反转确认。**

纯技术面，不代表中长期方向。KDJ/RSI 在强势行情中会高位钝化。应结合：
- 一季报披露情况（4月底密集期）是否超预期
- 北向资金流向是否持续
- ETF 份额变化

## 相关

- [[InvestSignal架构设计v1.1]]
- [[InvestSignal-Sprint3-资金面信号模块]]
- [[投资信息推送渠道]]

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
