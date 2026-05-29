---
pageType: entity

entityType: investment_stock
entity_type: investment_etf

privacyTier: public
ticker: 516500.SS

name: 生物科技ETF
sector: 生物科技

last_updated: '2026-05-06'
status: actively_tracking

current_view: '跟踪中证生物科技主题指数，处于历史低位区域，长线吸引力显现。但MACD柱状图转负、价格受压中轨下方，短期技术面空方占优。美国生物安全法案是悬而未决的灰犀牛。

  '
catalysts:
- date: 待定

  event: 美国生物安全法案进展
  type: 政策

  direction: 利空
  status: pending
- date: 2026-05

  event: Sell in May季节性压制
  type: 政策

  direction: 利空
  status: pending
- date: 待定

  event: 美联储政策转向确认
  type: 政策

  direction: 待观察
  status: pending
tracking:
- indicator: MACD柱状图

  latest_value: '-0.0007'
  latest_date: '2026-05-06'

  status: worsening
  note: 刚转负，短期动量警示
- indicator: 价格vs布林带中轨

  latest_value: 0.6184元（低于0.6226）
  latest_date: '2026-05-06'

  status: worsening
  note: 空方略占优势
- indicator: 200日SMA阻力

  latest_value: 0.6620元
  latest_date: '2026-05-06'

  status: pending
  note: 需涨约8%才能触及
- indicator: 布林带宽度

  latest_value: 压缩至62%
  latest_date: '2026-05-06'

  status: stable
  note: 方向不明

conclusion: '生物科技ETF处于历史估值低位，长线配置价值显现，但短期技术面偏空。美国生物安全法案是可能直接击穿支撑的"灰犀牛"。建议持有当前仓位，等待放量突破0.6620（200日均线）的右侧确认信号后再加仓。

  '
reports:
- path: research/华夏中证生物科技ETF_516500.SS/2026-05-06_summary.md

  date: '2026-05-06'
  type: ETF
claims:
- id: claim.516500.SS.valuation-low

  text: 跟踪中证生物科技主题指数，处于历史低位区域，长线吸引力显现
  status: supported

  confidence: 0.8
  evidence:
  - kind: financial-data

    sourceId: source.research.生物科技ETF
    path: research/生物科技ETF/

    lines: current_view
    weight: 0.8
- id: claim.516500.SS.us-biotech-risk

  text: 美国生物安全法案是悬而未决的灰犀牛，对CXO/生物科技出口有潜在冲击
  status: supported

  confidence: 0.7
  evidence:
  - kind: industry-data

    sourceId: source.research.生物科技ETF
    path: research/生物科技ETF/

    lines: current_view
    weight: 0.7
- id: claim.516500_SS.bull-case

  text: 跟踪中证生物科技主题指数，处于历史低位区域，长线吸引力显现。但MACD柱状图转负、价格受压中轨下方，短期技术面空方占优。美国生物安全法案是悬而未决的灰犀牛。
  status: supported

  confidence: 0.85
  evidence:
  - kind: entity-summary

    sourceId: source.entities.investments
    path: entities/investments/

    lines: current_view
    weight: 0.9
- id: claim.516500_SS.bear-case

  text: 技术面偏弱，基本面存在不确定性，需等待验证信号
  status: supported

  confidence: 0.8
  evidence:
  - kind: entity-summary

    sourceId: source.entities.investments
    path: entities/investments/

    lines: conclusion/tracking
    weight: 0.8
- id: claim.516500_SS.key-metric

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
- targetId: 医疗ETF

  targetTitle: 医疗ETF
  kind: same-sector

  weight: 0.7
  note: 生物科技与医疗健康主题高度重叠
updatedAt: "2026-05-29"
---
# 生物科技ETF (516500.SS)

## 基础数据

| 指标 | 数据 |
|------|------|
| 基金名称 | 华夏中证生物科技主题ETF |
| 跟踪指数 | 中证生物科技主题指数（930625） |
| 管理人 | 华夏基金管理有限公司 |
| 成立日期 | 2021-03-04 |
| 当前价格 | ~0.61-0.63元 |
| 200日SMA | 0.6620元 |

## 投资逻辑

**核心逻辑：** 老龄化社会带来的生物科技长期需求 + AI驱动药物研发的降本增效逻辑（外溢效应）+ 全球生物科技风险偏好回升预期。

**核心看点：**
1. 估值处于历史低位，多年低点区域
2. AI+医疗应用长期逻辑清晰
3. 长线吸引力显现

## 风险提示

- 美国生物安全法案威胁（直接冲击供应链）
- MACD柱状图转负，短期动量恶化
- 成交量低迷，缺乏方向性资金确认
- 港/A股生物科技板块持续面临抛压

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
