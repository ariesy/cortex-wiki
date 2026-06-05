---
pageType: entity
id: entity:中概互联网ETF

entityType: investment_stock
entity_type: investment_etf

privacyTier: public
ticker: 513050.SS

name: 中概互联网ETF
sector: 中概互联网

last_updated: '2026-05-08'
status: actively_tracking

current_view: '跟踪中证海外中国互联网50指数，持仓腾讯(~30%)、阿里(~25%)等龙头。当前处于历史估值中低水位（较52周高点回撤30%），MACD底背离+MACD柱转正，技术面底部构建初现。阿里巴巴AI重估+腾讯DeepSeek投资+京东技术面改善形成合力。

  '
catalysts:
- date: '2026-05-19'

  event: 拼多多2026财年Q1财报发布
  type: 财报

  direction: 待观察
  status: pending
- date: 2026-05

  event: DeepSeek融资进展（腾讯投资）
  type: 政策

  direction: 利多
  status: pending
- date: 2026-05

  event: 阿里巴巴财报/AI业务
  type: 验证节点

  direction: 利多
  status: pending
tracking:
- indicator: MACD柱状图

  latest_value: '+0.00249'
  latest_date: '2026-05-07'

  status: improving
  note: 由负转正，2026年以来首次
- indicator: RSI

  latest_value: '52.65'
  latest_date: '2026-05-07'

  status: stable
  note: 站上50中轴，不超买
- indicator: 布林带宽

  latest_value: '0.112'
  latest_date: '2026-05-07'

  status: stable
  note: 极度收缩，酝酿突破
- indicator: 价格vs200日均线

  latest_value: 1.24 vs 1.4604
  latest_date: '2026-05-07'

  status: worsening
  note: 价格远低于200 SMA，长期空头

conclusion: '中概互联网ETF处于底部构建阶段，MACD底背离+柱转正是2026年以来首次的看涨信号，RSI站上50中轴但未超买。短期阻力50日均线1.239元，长期压力200日均线1.460元。建议持有观望，空仓者可在1.20-1.25区间轻仓试探，止损1.19元。关键催化剂：拼多多5/19财报、DeepSeek融资进展、阿里AI业务验证。

  '
reports:
- path: research/中概互联网ETF易方达_513050.SS/complete_report.md

  date: '2026-05-08'
  type: ETF
claims:
- id: claim.513050.SS.ai-infrastructure

  text: 中概互联网ETF持仓腾讯阿里等AI基础设施龙头，受益于中国AI重估
  status: supported

  confidence: 0.85
  evidence:
  - kind: research-report

    sourceId: source.research.中概互联网ETF
    path: research/中概互联网ETF/

    lines: current_view
    weight: 0.8
- id: claim.513050.SS.valuation-low

  text: 当前较52周高点回撤30%，估值处于历史中低水位
  status: supported

  confidence: 0.8
  evidence:
  - kind: technical-analysis

    sourceId: source.research.中概互联网ETF
    path: research/中概互联网ETF/

    lines: current_view
    weight: 0.7
- id: claim.513050_SS.bull-case

  text: 跟踪中证海外中国互联网50指数，持仓腾讯(~30%)、阿里(~25%)等龙头。当前处于历史估值中低水位（较52周高点回撤30%），MACD底背离+MACD柱转正，技术面底部构建初现。阿里巴巴AI重估+腾讯DeepSeek投资+京东技术面改善
  status: supported

  confidence: 0.85
  evidence:
  - kind: entity-summary

    sourceId: source.entities.investments
    path: entities/investments/

    lines: current_view
    weight: 0.9
- id: claim.513050_SS.bear-case

  text: 技术面偏弱，基本面存在不确定性，需等待验证信号
  status: supported

  confidence: 0.8
  evidence:
  - kind: entity-summary

    sourceId: source.entities.investments
    path: entities/investments/

    lines: conclusion/tracking
    weight: 0.8
- id: claim.513050_SS.key-metric

  text: 关键监控指标详见tracking字段，定期跟踪验证
  status: supported

  confidence: 0.85
  evidence:
  - kind: entity-summary

    sourceId: source.entities.investments
    path: entities/investments/

    lines: tracking indicators
    weight: 0.85
relationships:
- targetId: 1810.HK_小米集团

  targetTitle: 小米集团
  kind: etf-component

  weight: 0.9
  note: 小米是港股中概互联网ETF成分股
- targetId: 京东集团

  targetTitle: 京东集团
  kind: etf-component

  weight: 0.9
  note: 京东是港股中概互联网ETF核心成分股
updatedAt: "2026-05-29"
---
# 中概互联网ETF (513050.SS)

## 基础数据

| 指标 | 数据 |
|------|------|
| 基金名称 | 易方达中证海外中国互联网50ETF |
| 跟踪指数 | 中证海外中国互联网50指数 |
| 52周高/低 | 1.768元 / 1.164元 |
| 当前价格 | 1.24元 |
| 50日均线 | 1.239元 |
| 200日均线 | 1.460元 |

## 持仓结构（估算）

| 成分股 | 权重约 | 近期催化剂 |
|--------|:------:|-----------|
| 腾讯控股 | ~30% | DeepSeek投资 |
| 阿里巴巴 | ~25% | AI云扩张，BNP目标价$209 |
| 美团 | ~8% | 到店业务改善 |
| 拼多多 | ~6% | 5/19财报 |
| 京东 | ~5% | 金叉信号 |

## 投资逻辑

**核心逻辑：** 中国AI龙头企业的一揽子配置工具，阿里AI重估+腾讯DeepSeek投资+整体估值处于历史低位构成三重支撑。

**核心看点：**
1. 当前价格较52周高点回撤约30%
2. MACD底背离+柱转正，技术面拐点初现
3. 阿里BNP目标价$209（+58%），腾讯DeepSeek期权

## 风险提示

- 长期趋势仍为空头（200日均线压制）
- 地缘政治风险持续
- 拼多多财报前不确定性
- 百度盈利预期下调拖累

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
