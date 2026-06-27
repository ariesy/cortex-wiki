---
pageType: entity
id: entity:红利ETF

entityType: investment_stock
entity_type: investment_etf

privacyTier: public
ticker: 515080.SS

name: 红利ETF
sector: 高股息/红利策略

last_updated: '2026-06-25'
status: actively_tracking

current_view: '跟踪中证红利指数(000922)，股息率4.9%、PE 8.85倍处于3年历史高位(99.72%分位)。2026-06-25群聊因子对比研究：相对300价值核心差异是"选样范围"(300价值限沪深300选100只；中证红利全A选100只)，所以中证红利行业更分散（含煤炭、公路、港口、运营商等中盘红利股），银行权重约25-30%(低于300价值的45-55%)。估值水平接近，但"现金流"色彩更纯——本质是买"稳定收租的物业"，而非"打折的优质店铺"。当前风险：估值已不便宜+机构拥挤度创历史新高+2025-2026若风险偏好回升可能阶段性跑输。攻防兼备但需控仓。

  '
catalysts:
- date: 2026-06-25

  event: 2026-06-25群聊因子ETF对比：与沪深300/300价值/红利低波100/50AH 5个产品维度对比
  type: 群聊讨论

  direction: 中性
  status: completed
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
- indicator: 指数PE-TTM

  latest_value: '8.85倍（99.72%分位）'
  latest_date: '2026-04-30'

  status: worsening
  note: 处于3年历史高位
- indicator: 股息率

  latest_value: '4.9%'
  latest_date: '2026-04-27'

  status: stable
  note: 仍优于10年国债1.77%，息差3.13%
- indicator: 基金规模

  latest_value: '94.34亿元'
  latest_date: '2026-05-07'

  status: improving
  note: 创上市新高
- indicator: MACD

  latest_value: '+0.008'
  latest_date: '2026-05-07'

  status: worsening
  note: 远低于前高+0.0207，顶背离风险

conclusion: '攻防兼备但需控仓(≤A股权益20%)。2026-06-25群聊因子对比研究新增定位：与300价值相比是"现金流型"而非"估值修复型"，与红利低波100相比波动更大(无低波过滤)。当前估值分位99.72%已透支两年涨幅，建议持有但不加仓；如2025-2026市场风险偏好大幅回升需考虑切换至300价值或红利低波100。

  '
reports:
- path: research/中证红利ETF_515080.SS/2026-05-07_summary.md

  date: '2026-05-07'
  type: ETF
- path: syntheses/a股因子etf对比研究-2026-06-25.md

  date: '2026-06-25'
  type: 因子对比
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

  text: PE 8.85倍处于3年历史高位(99.72%分位)，MACD顶背离风险，上行空间受限
  status: supported

  confidence: 0.85
  evidence:
  - kind: technical-analysis

    sourceId: source.research.红利ETF
    path: research/红利ETF/

    lines: current_view
    weight: 0.85
- id: claim.515080.SS.factor-positioning-2026-06-25

  text: 2026-06-25因子对比研究定位：选样范围全A(非限沪深300)，行业更分散(含中盘红利股)；本质是"现金流型"价值(非"估值修复型")
  status: supported

  confidence: 0.85
  evidence:
  - kind: synthesis-summary

    sourceId: source.syntheses.factor-etf-comparison-2026-06-25
    path: syntheses/a股因子etf对比研究-2026-06-25.md

    lines: 300价值vs红利ETF对比
    weight: 0.85
- id: claim.515080.SS.peer-comparison

  text: 与300价值相比银行权重低(25-30% vs 45-55%)，行业含煤炭/公路/港口/运营商等中盘红利股；与红利低波100相比无低波过滤
  status: supported

  confidence: 0.85
  evidence:
  - kind: synthesis-summary

    sourceId: source.syntheses.factor-etf-comparison-2026-06-25
    path: syntheses/a股因子etf对比研究-2026-06-25.md

    lines: 因子对比矩阵
    weight: 0.85
relationships:
- targetId: entity:300价值ETF

  targetTitle: 300价值ETF (512370)
  kind: peer-comparison

  weight: 0.9
  note: 同样是价值风格，但选样范围不同(全A vs 沪深300)，银行权重差异大
- targetId: entity:红利低波100

  targetTitle: 红利低波100 (930955)
  kind: peer-comparison

  weight: 0.9
  note: 中证红利基础上叠加"低波动"过滤，波动率显著更低
- targetId: entity:沪深300ETF

  targetTitle: 沪深300ETF (510300)
  kind: peer-comparison

  weight: 0.85
  note: 大盘底仓基准，估值水平对比参考
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
updatedAt: "2026-06-25"
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

## 2026-06-25 群聊因子对比研究更新

**与 300价值ETF 的核心差异**：
- **选样范围**：300价值只能在沪深300的300只大盘股里选；中证红利是全A选股，因此纳入中盘红利股（煤炭、公路、港口、区域银行、运营商等）
- **行业分布**：300价值银行独大（45-55%），中证红利银行仅25-30%，行业更分散（含煤炭、电信运营商、公路、铁路、传统化工等高分红）
- **风格本质**：300价值 = "估值修复型价值"（买打折店铺盼回升）；中证红利 = "现金流收入型价值"（买收租物业拿分红）
- **数据印证**：中证红利 PE 11-13 倍（2026 区间），股息率 5-6%，比 300 价值（PE 7-9）估值略贵但更分散

**与 沪深300ETF 的核心差异**：
- 沪深300 = 宽基大盘（PE 12-13，股息率 2%）
- 中证红利 = 因子策略（PE 8-9，股息率 5%）
- 中证红利明显跑赢沪深300（2023-2024 年累计 +42.61% vs 沪深300震荡）

**与 红利低波100 的核心差异**：
- 红利低波100 = 中证红利 + 过去一年日波动率过滤（取波动率最低的100只）
- 红利低波100 持有体验更好（2022-2024 三年正收益，2024 仅跌2.3%）
- 但当前 PE 分位60-70% 也已经不便宜

**2026年配置建议**（结合用户投资风格）：
- 进攻型仓位（看中弹性）→ 沪深300
- 估值修复+价值型 → 300价值
- 现金流收入型（看重股息）→ 中证红利（515080）
- 防御+稳定+更高股息 → 红利低波100

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
