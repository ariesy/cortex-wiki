---
entity_type: investment_etf
privacyTier: public
ticker: 515080.SS
name: 红利ETF
sector: 高股息/红利策略
last_updated: '2026-05-07'
status: actively_tracking
current_view: '跟踪中证红利指数，股息率约4.9%，PE 8.85倍处于3年历史高位。MACD顶背离风险（+0.008远低于前高+0.0207），1.68元阻力位压制。资金持续流入（近20日净流入11.55亿），攻防兼备属性凸显。

  '
catalysts:
- date: 2026-05
  event: 1.68元阻力位能否有效突破
  type: 验证节点
  direction: 待观察
  status: pending
- date: 2026-05
  event: 银行/能源股财报（分红能力）
  type: 财报
  direction: 待观察
  status: pending
- date: 2026-05
  event: 国债收益率走势（无风险利率）
  type: 政策
  direction: 待观察
  status: pending
tracking:
- indicator: MACD
  latest_value: '+0.008'
  latest_date: '2026-05-07'
  status: worsening
  note: 远低于前高+0.0207，顶背离风险
- indicator: RSI
  latest_value: '64.4'
  latest_date: '2026-05-07'
  status: stable
  note: 中性偏强，距超买70仍有空间
- indicator: ATR
  latest_value: '0.0171'
  latest_date: '2026-05-07'
  status: worsening
  note: 从0.025大幅压缩，波动率极低
- indicator: VWMA
  latest_value: 1.6106元
  latest_date: '2026-05-07'
  status: stable
  note: 价格1.64 > VWMA，有买盘支撑
conclusion: '红利ETF攻防兼备属性凸显（4.9%股息率 vs 1.77%国债），但1.68元阻力位前MACD顶背离风险是核心观察点。建议持有，止损50日均线~1.615元，清仓线200日均线~1.564元。有效突破1.68元+RSI同步新高+放量可上调至增持。

  '
reports:
- path: research/中证红利ETF_515080.SS/2026-05-07_summary.md
  date: '2026-05-07'
  type: ETF
claims:
- id: claim.515080.SS.dividend-yield
  text: 跟踪中证红利指数，股息率约4.9%，显著优于无风险利率
  status: supported
  confidence: 0.9
  evidence:
  - kind: financial-data
    sourceId: source.research.红利ETF
    path: research/红利ETF/
    lines: current_view
    weight: 0.9
- id: claim.515080.SS.macd-divergence
  text: PE 8.85倍处于3年历史高位，MACD顶背离风险，上行空间受限
  status: supported
  confidence: 0.75
  evidence:
  - kind: technical-analysis
    sourceId: source.research.红利ETF
    path: research/红利ETF/
    lines: current_view
    weight: 0.7
- id: claim.515080_SS.bull-case
  text: 跟踪中证红利指数，股息率约4.9%，PE 8.85倍处于3年历史高位。MACD顶背离风险（+0.008远低于前高+0.0207），1.68元阻力位压制。资金持续流入（近20日净流入11.55亿），攻防兼备属性凸显。
  status: supported
  confidence: 0.85
  evidence:
  - kind: entity-summary
    sourceId: source.entities.investments
    path: entities/investments/
    lines: current_view
    weight: 0.9
- id: claim.515080_SS.bear-case
  text: 技术面偏弱，基本面存在不确定性，需等待验证信号
  status: supported
  confidence: 0.8
  evidence:
  - kind: entity-summary
    sourceId: source.entities.investments
    path: entities/investments/
    lines: conclusion/tracking
    weight: 0.8
- id: claim.515080_SS.key-metric
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
- targetId: 招商银行
  targetTitle: 招商银行
  kind: etf-component
  weight: 0.9
  note: 招行是红利ETF核心成分股
- targetId: 中国神华
  targetTitle: 中国神华
  kind: etf-component
  weight: 0.9
  note: 中国神华是红利ETF核心成分股
- targetId: 紫金矿业
  targetTitle: 紫金矿业
  kind: etf-component
  weight: 0.8
  note: 紫金矿业是红利ETF成分股
- targetId: 民生银行_600016
  targetTitle: 民生银行
  kind: etf-component
  weight: 0.7
  note: 民生银行是高股息港股代表
---
# 红利ETF (515080.SS)

## 基础数据

| 指标 | 数据 |
|------|------|
| 基金名称 | 招商中证红利ETF |
| 跟踪指数 | 中证红利指数（000922） |
| 当前价格 | ~1.635-1.645元 |
| 股息率 | ~4.9%（2026-04-27） |
| 指数PE(TTM) | 8.85倍（2026-04-30，历史高位99.72%分位） |
| 股债利差 | 4.9% vs 十年期国债1.77%，息差3.13% |
| 基金规模 | 94.34亿元（创上市新高） |

## 投资逻辑

**核心逻辑：** 低利率环境下高股息资产吸引力凸显，资金持续流入红利ETF寻求"攻守兼备"配置。

**核心看点：**
1. 股息率4.9%显著优于国债，安全边际高
2. 近20日净流入11.55亿，资金持续追捧
3. 规模94亿创上市新高，流动性好

## 风险提示

- MACD顶背离风险（+0.008远低于前高+0.0207）
- 1.68元阻力位压制，突破前不宜追高
- 低利率逻辑已被充分定价，边际效用递减
- 银行/能源股分红若不及预期将压制价格