---
pageType: entity
id: entity:上证50AH优选指数A
entityType: investment_stock
entity_type: investment_etf
privacyTier: public
ticker: 501050.SS
name: 上证50AH优选指数A
sector: 大盘蓝筹/AH轮动
last_updated: 2026-06-25
status: actively_tracking
current_view: |
  跟踪上证50AH优选指数(950090)，2026-06-24单位净值1.7450，2026-06-25群聊因子对比研究：核心定位是"上证50增强+AH自动套利"二合一。对于同时有A+H的成分股，每月比较汇率调整后价比选便宜持有。反身性陷阱明显——A股越涨→AH价差越大→50AH越被迫买H股→越跑输A股牛市。近1年+15.72%跑输沪深300达10.89pct（受2024-2025 A股强、港股弱压制），近3年+36.12%仍跑赢沪深300 8.20pct（长期策略未失效）。当前H股持仓约40%（含中国平安H、紫金矿业H、招行H、工行H、兴业H、中信H等），H股部分PE 5-9倍+股息率5-8%估值极便宜，但A/H价差收窄预期+港股估值修复需要时间。适合"上证50替代+长期持有"，但短期会因A/H方向出现明显跑输。
catalysts:
  - date: 2026-06-25
    event: 2026-06-25群聊因子ETF对比：与沪深300/300价值/红利/红利低波100 5个产品维度对比
    type: 群聊讨论
    direction: 中性
    status: completed
  - date: 2026-06-25
    event: A/H折溢价水平及方向（恒生AH溢价指数HSAHP）
    type: 关键观察
    direction: 待观察
    status: pending
  - date: 2026-Q3
    event: 港股估值修复进度（恒生指数走势）
    type: 验证节点
    direction: 待观察
    status: pending
tracking:
  - indicator: 单位净值
    latest_value: 1.7450元
    latest_date: 2026-06-24
    status: stable
    note: 当日+0.75%
  - indicator: 近1年收益
    latest_value: +15.72%
    latest_date: 2026-06-24
    status: stable
    note: 跑输沪深300 10.89pct
  - indicator: 近3年收益
    latest_value: +36.12%
    latest_date: 2026-06-24
    status: improving
    note: 跑赢沪深300 8.20pct，长期策略有效
  - indicator: 前10大持仓集中度
    latest_value: 45.39%
    latest_date: 2026-Q1
    status: stable
    note: 高于沪深300(30%)+上证50(38%)
  - indicator: H股配置比例
    latest_value: ~40%
    latest_date: 2026-Q1
    status: worsening
    note: 受2024-2025 A/H价差扩大影响
conclusion: |
  适合"上证50替代+长期持有"的差异化配置，建议仓位A股权益10-20%。不适合短期弹性期望或A股主升浪期间加仓。最大风险是反身性陷阱——A股越涨→50AH越被动→资金流出。当前不强制调仓，但若A股持续走强应考虑切换至纯沪深300或300价值。AH折溢价水平（恒生AH溢价指数HSAHP）是核心跟踪指标，突破130则需警惕。
reports:
  - path: research/上证50AH优选指数A_501050.SS/2026-06-25_summary.md
    date: 2026-06-25
    type: 因子对比
  - path: syntheses/a股因子etf对比研究-2026-06-25.md
    date: 2026-06-25
    type: 因子对比
claims:
  - text: 2026年6月分析报告：501050规模15.43亿元，A类净值1.698(2026-06-08)，前十大含贵州茅台(9.76%)、中国平安H(6.80%)、紫金矿业H(5.80%)等，H股占比约40%，跟踪误差优秀(0.01%/月)
    status: supported
    confidence: 0.8
    evidence: []
relationships:
  - targetId: entity:沪深300ETF
    targetTitle: 沪深300ETF (510300)
    kind: peer-comparison
    weight: 0.85
    note: 大盘底仓对比基准
  - targetId: entity:300价值ETF
    targetTitle: 300价值ETF (512370)
    kind: peer-comparison
    weight: 0.8
    note: 价值风格，但50AH含H股
  - targetId: entity:红利低波100
    targetTitle: 红利低波100 (930955)
    kind: peer-comparison
    weight: 0.75
    note: 都是"防守型"，但50AH是大盘+套利，红利低波100是行业均衡+因子
  - targetId: 贵州茅台_600519
    targetTitle: 贵州茅台
    kind: etf-component
    weight: 0.95
    note: 50AH优选第一大重仓（9.76%）
  - targetId: 601318.SH_中国平安
    targetTitle: 中国平安
    kind: etf-component
    weight: 0.9
    note: 第二大重仓（6.80%，H股02318）
  - targetId: 招商银行
    targetTitle: 招商银行
    kind: etf-component
    weight: 0.9
    note: 第四大重仓（5.23%，当前配A股）
  - targetId: 紫金矿业
    targetTitle: 紫金矿业
    kind: etf-component
    weight: 0.85
    note: 第三大重仓（5.80%，H股02899）
  - targetId: 长江电力_600900
    targetTitle: 长江电力
    kind: etf-component
    weight: 0.7
    note: 第五大重仓（3.56%，纯A股）
  - targetId: 兴业银行
    targetTitle: 兴业银行
    kind: etf-component
    weight: 0.7
    note: 第六大重仓（3.43%，A股）
  - targetId: 恒瑞医药_600276
    targetTitle: 恒瑞医药
    kind: etf-component
    weight: 0.6
    note: 第八大重仓（2.65%，纯A股）
updatedAt: 2026-06-27T10:55:13.226Z
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-06-10-1237-65cf7423
---

# 上证50AH优选指数A (501050.SS)

## 基础数据

| 指标 | 数据 |
|------|------|
| 基金全称 | 华夏沪港通上证50AH优选指数证券投资基金（LOF） |
| 基金代码 | 501050（A类）/ 006395（C类） |
| 跟踪指数 | 上证50AH优选指数（950090.SH） |
| 管理人 | 华夏基金 |
| 基金经理 | 华龙（2022年8月22日任职） |
| 成立日期 | 2016-10-27 |
| 基金规模 | 15.43亿元（2026Q1） |
| 股票仓位 | 88.82%（2026Q1） |
| 最新净值（A类）| **1.7450（2026-06-24）** |
| 成立来收益 | +74.50% |
| 管理费+托管费 | 约0.6%/年 |

## 业绩表现（截止2026-06-24）

| 区间 | A类净值增长率 | 沪深300 | 跑赢/输 |
|------|:----------:|:--------:|:----:|
| 近 1 月 | -1.02% | +2.02% | -3.04pct |
| 近 3 月 | +4.30% | +10.47% | -6.17pct |
| 近 6 月 | -0.85% | +6.67% | -7.52pct |
| **近 1 年** | **+15.72%** | **+26.61%** | **-10.89pct** |
| **近 2 年** | **+40.05%** | **+42.17%** | **-2.12pct** |
| **近 3 年** | **+36.12%** | **+27.92%** | **+8.20pct** |
| 成立来 | +74.50% | — | — |

**关键判断**：
- **短期（1年）明显跑输沪深300**：2024-2025 A股政策刺激反弹，AH价差扩大，被动配H股
- **长期（3年）仍跑赢沪深300 8.2pct**：策略长期有效
- **跟踪误差2-3pct/年**：管理费+换手摩擦

## 核心策略：AH自动轮动

**机制**（基于2026-06-25群聊因子研究）：

上证 50 的 50 只成分股中，约 23 只同时有 A+H 上市。对于这些双重上市股：
- 每月轮动一次
- 比较 A 股价格 ×(汇率) vs H 股价格
- **持有便宜的那一边**

**实际效果**（2024-2025 期间）：
- A 股相对 H 股溢价 20-30%
- 50AH 优选被迫大量配置 H 股
- H 股表现弱于 A 股 → 50AH 跑输沪深 300

## 持仓结构（2026Q1前十大）

| 标的 | 市场 | 持仓占比 | 行业 |
|------|------|:--------:|------|
| 贵州茅台 | A | 9.76% | 消费 |
| 中国平安 | H（02318）| 6.80% | 保险 |
| 紫金矿业 | H（02899）| 5.80% | 有色 |
| 招商银行 | A | 5.23% | 银行 |
| 长江电力 | A | 3.56% | 电力 |
| 兴业银行 | A | 3.43% | 银行 |
| 工商银行 | H（01398）| 3.03% | 银行 |
| 恒瑞医药 | A | 2.65% | 医药 |
| 药明康德 | A | 2.61% | 医药 |
| 中信证券 | H（06030）| 2.52% | 券商 |

**持仓特征**：
- **H股占比约40%**（策略倾向配H股）
- **银行保险合计约40-50%** 为绝对主力
- **前 10 大集中度 45.39%** 高于沪深 300（30%）

## 2026-06-25 群聊因子对比研究

**在5个ETF中的独特定位**：
- **沪深300**：宽基大盘，无AH套利
- **300价值**：限沪深300选100只价值股，无AH套利
- **中证红利（515080）**：全A选100只高股息股，无AH套利
- **红利低波100（930955）**：中证红利+低波过滤，无AH套利
- **50AH优选**：上证50+AH自动套利 → **唯一一个"跨市场"产品**

**核心优势**：
- A股贵时自动买H股，等待价差回归
- A股折价时自动买A股，享受估值修复
- 长期（3年+）大概率跑赢上证50和沪深300

**核心劣势（反身性陷阱）**：
- A股越涨 → AH价差越大 → 50AH越被迫买H股
- 越跑输A股牛市 → 资金流出 → 越被动
- 2024-2025年正是这种"聪明指数吃暗亏"的阶段

## 估值水平（按持仓分拆）

| 维度 | A股部分（茅台、长江电力等）| H股部分（平安、招行H等）|
|------|------|------|
| PE 区间 | 12-25 倍 | 5-9 倍 |
| PB 区间 | 2-5 倍 | 0.5-0.8 倍 |
| 股息率 | 1-3% | 5-8% |
| 估值水平 | 合理偏低 | 极便宜 |

**整体加权 PE 估算 10-13 倍**。

## 投资结论

**核心观点**（2026-06-25更新）：
- ✅ **适合做"上证 50 替代 + 长期持有"**，不期望短期跑赢
- ✅ **适合"A/H 双账户"投资者**（用沪市买茅台、深市买H股自己复刻）
- ⚠️ **不适合**期望短期弹性、或在 A 股主升浪期间加仓
- 📊 **建议仓位**：A 股权益的 10-20%，作为大盘底仓的差异化配置

**关键跟踪指标**：
1. 恒生AH溢价指数（HSAHP）当前水平
2. 港股恒生指数走势
3. 茅台/平安/招行三巨头的业绩

**最大风险**：A 股进入新一轮主升浪 → H 股持续跑输 → 50AH 优选被反复"过山车"

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-06-10-1237](../sources/bridge-workspace-142ea9a2-memory-2026-06-10-1237-65cf7423.md)

### Related Pages

- [华龙](华龙-华夏基金.md)
- [实体提取汇总 2026-06-12](../syntheses/entity-extract-2026-06-12.md)
<!-- openclaw:wiki:related:end -->
