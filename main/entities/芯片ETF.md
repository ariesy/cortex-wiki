---


pageType: entity

entityType: investment_stock
entity_type: investment_etf

privacyTier: public
ticker: 159995.SZ

name: 芯片ETF
sector: 半导体/芯片

last_updated: '2026-05-06'
status: actively_tracking

current_view: '跟踪国证芯片产业指数，RSI 71.88接近超买、量价背离（上涨缩量）显示短期回调风险高。逼近2.12元强阻力位。建议减持60%锁定利润，等待回撤至1.82元（50日均线）附近再分批建仓。

  '
catalysts:
- date: 2026-05

  event: 关注2.12元阻力位能否突破
  type: 验证节点

  direction: 待观察
  status: pending
- date: 2026-05

  event: 地缘政治风险（出口管制）
  type: 政策

  direction: 利空
  status: pending
- date: 2026-05

  event: 国产替代政策力度
  type: 政策

  direction: 利多
  status: pending
tracking:
- indicator: RSI

  latest_value: '71.88'
  latest_date: '2026-05-06'

  status: worsening
  note: 接近超买区域
- indicator: 成交量

  latest_value: 萎缩
  latest_date: '2026-05-06'

  status: worsening
  note: 价格上涨但量能萎缩，需求衰竭信号
- indicator: 布林带上轨阻力

  latest_value: 2.12元
  latest_date: '2026-05-06'

  status: pending
  note: 当前价格~2.07元，逼近强阻力
- indicator: 50日均线支撑

  latest_value: 1.82元
  latest_date: '2026-05-06'

  status: stable
  note: 回撤买入目标位

conclusion: '芯片ETF短期技术面风险高：RSI超买+量价背离+逼近强阻力位2.12元。建议立即减持60%仓位锁定利润，止损设于1.98元。若周线收盘站稳2.12元且放量可买回至满仓；主要买入目标在1.82元（50日均线），止损200日均线1.69元。

  '
claims:
  - id: claim.159995.SZ.bull-case

    text: "国产替代逻辑强劲，受益于政策支持半导体自主可控，AI算力需求持续爆发"
    status: supported

    confidence: 0.85
    evidence:
      - kind: entity-summary

        sourceId: source.entities.investments
        path: entities/investments/

        lines: current_view
        weight: 0.9
  - id: claim.159995.SZ.bear-case

    text: "RSI 71.88接近超买，量价背离（上涨缩量）显示短期回调风险高，逼近2.12元强阻力位"
    status: supported

    confidence: 0.8
    evidence:
      - kind: entity-summary

        sourceId: source.entities.investments
        path: entities/investments/

        lines: conclusion/tracking
        weight: 0.8
  - id: claim.159995.SZ.key-metric

    text: "RSI 71.88接近超买，50日均线1.82元是回撤买入目标位"
    status: supported

    confidence: 0.85
    evidence:
      - kind: entity-summary

        sourceId: source.entities.investments
        path: entities/investments/

        lines: tracking indicators
        weight: 0.85

reports:
- path: research/华夏芯片ETF_159995.SZ/2026-05-06_summary.md

  date: '2026-05-06'
  type: ETF
- id: claim.159995.SZ.localization

  text: 国产替代逻辑强劲，受益于政策支持半导体自主可控
  status: supported

  confidence: 0.85
  evidence:
  - kind: industry-data

    sourceId: source.research.芯片ETF
    path: research/芯片ETF/

    lines: current_view
    weight: 0.8
- id: claim.159995.SZ.rsi-overbought

  text: RSI 71.88接近超买，短期回调风险高，建议减持锁定利润
  status: supported

  confidence: 0.8
  evidence:
  - kind: technical-analysis

    sourceId: source.research.芯片ETF
    path: research/芯片ETF/

    lines: current_view
    weight: 0.7
relationships:
- targetId: 兆易创新

  targetTitle: 兆易创新
  kind: etf-component

  weight: 0.9
  note: 兆易是芯片ETF核心成分股
- targetId: 深南电路

  targetTitle: 深南电路
  kind: etf-component

  weight: 0.8
  note: 深南是芯片ETF成分股
- targetId: 兴森科技

  targetTitle: 兴森科技
  kind: etf-component

  weight: 0.8
  note: 兴森是芯片ETF成分股
- targetId: 中际旭创

  targetTitle: 中际旭创
  kind: etf-component

  weight: 0.7
  note: 光模块与芯片产业链高度相关
- targetId: 中际旭创

  targetTitle: 中际旭创
  kind: etf-holds-components

  confidence: 0.85
  evidence:
    - kind: sector-analysis

      sourceId: source.entities.investments
      note: "芯片ETF持有中际旭创等光模块/算力芯片标的"

updatedAt: "2026-05-29"


---


# 芯片ETF (159995.SZ)

## 基础数据

| 指标 | 数据 |
|------|------|
| 基金名称 | 华夏国证芯片产业ETF |
| 跟踪指数 | 国证芯片产业指数 |
| 当前价格 | ~2.07元 |
| 52周高/低 | 约2.4元/1.2元 |
| 50日均线 | 1.82元 |
| 200日均线 | 1.75元 |
| 强阻力位 | 2.12元 |

## 投资逻辑

**核心逻辑：** AI算力需求爆发+国产替代是国家战略，长期结构性牛市逻辑成立。

**核心看点：**
1. AI需求和国产替代是长期结构性利好
2. 国产替代政策持续支持
3. 成分股估值已计入乐观预期但长期成长性强

## 风险提示

- RSI 71.88接近超买，短期回调概率高
- 量价背离：价格上涨但成交量萎缩
- 成分股PE 40-60x，估值已高度定价
- 地缘政治风险（出口管制）可能冲击盈利预期

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
