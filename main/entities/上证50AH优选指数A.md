---
pageType: entity
id: entity:上证50AH优选指数A
entityType: investment_stock
entity_type: investment_etf
privacyTier: public
ticker: 501050.SS
name: 上证50AH优选指数A
sector: 大盘蓝筹/AH轮动
last_updated: 2026-08-03
status: actively_tracking
current_view: |
  2026-08-03 同日两份独立分析：①AI Berkshire四大师（长周期基本面）：指数PE 10.14（分位66.9%）、PB 1.20、股息率2.98%、ROE 11.83%；AH溢价已从2024年160+收敛至~122-123；7年跑赢上证50约12.6pct但跑输沪深300；0.60%综合费率偏高；15亿规模Q2净赎回约10%；结论：空仓观望/小额定投，持仓者可继续持有，加仓信号PE<8或AH溢价重回140+。②TradingAgents多智能体（短中期+风控）：因数据商覆盖残缺（仅1条K线、无新闻、无净值/持仓数据）陷入信息盲区，判决UNDERWEIGHT——现有持仓降至组合2%以内观察仓，分2-3笔在1.70-1.73减持，硬止损1.62，场外资金严禁建仓，待至少3项关键数据（净值序列/跟踪误差/折溢价/持仓）补齐后重审，时间维度1-3个月。两份报告核心趋同：当前均不建议加仓；差异在存量仓位处理力度（伯克希尔"可持有" vs TradingAgents"降至2%"），且TradingAgents明确标注Underweight源于数据缺失而非基本面恶化，不代表对底层策略否定。
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
  - indicator: 单位净值(A类)
    latest_value: 1.740元
    latest_date: 2026-07-31
    status: stable
    note: 2026-08-03报告日
  - indicator: 基金规模
    latest_value: ~15.02亿元
    latest_date: 2026-06-30
    status: worsening
    note: Q2单季净赎回约10%（A类8.33亿份，C类0.16亿份）
  - indicator: 指数PE
    latest_value: "10.14（分位66.9%）"
    latest_date: 2026-07-31
    status: neutral
    note: 绝对便宜，相对自身历史中高位；PB 1.20分位75.5%
  - indicator: 股息率
    latest_value: 2.98%
    latest_date: 2026-07-31
    status: stable
    note: 高于10年国债约1pp，有债底；注意H股股息税20%侵蚀
  - indicator: AH溢价(HSAHP)
    latest_value: "~122-123"
    latest_date: 2026-08-03
    status: neutral
    note: 从2024年160+大幅收敛，溢价收敛alpha基本吃尽
  - indicator: 近7年超额(指数)
    latest_value: "+12.6pct vs 上证50"
    latest_date: 2026-08-03
    status: stable
    note: 50AH优选+14.63% vs 上证50+2.01%；但跑输沪深300(+30.16%)
  - indicator: 场内价格(2026-08-03)
    latest_value: "1.71（开1.73/高1.73/低1.70）"
    latest_date: 2026-08-03
    status: stable
    note: 成交量仅86,100股，流动性极低；数据商对该基金K线覆盖残缺（仅1条记录）
  - indicator: 跟踪偏离度
    latest_value: "A类+0.62%"
    latest_date: 2026-Q2
    status: stable
    note: 季报披露，符合LOF常态
conclusion: |
  2026-08-03 双框架交叉结论：①AI Berkshire四大师：机制聪明（AH择优规则制度化，7年跑赢上证50约12.6pct），但0.60%综合费率+15亿小规模让"买便宜"收益每年先被吞0.4pct，且AH溢价收敛至~123后超额红利衰减。空仓者观望/小额定投（若追求AH弹性用低费率港股通ETF，追求大盘价值用上证50ETF费率0.2%）；持仓者可继续持有（3%股息+AH价差有债底，接受低弹性）；加仓信号PE<8（分位<30%）或AH溢价重回140+；减仓信号AH溢价<110长期化+成长持续跑赢。②TradingAgents多智能体（同日）：因数据商覆盖残缺陷入信息盲区，判决UNDERWEIGHT——持仓降至2%观察仓、分2-3笔1.70-1.73减持、止损1.62、场外不建仓，数据补齐后重审（1-3个月）。两框架均不建议当前加仓；TradingAgents的Underweight归因于数据缺失而非基本面恶化，不否定底层策略。最大风险：AH溢价收敛+大盘价值跑输成长+高费率侵蚀+场内流动性极低。
reports:
  - path: /app/TradingAgents/reports/501050.SS_20260803_045847/complete_report.md
    date: 2026-08-03
    type: TradingAgents多智能体分析
  - path: /home/ariesy/.openclaw/workspace/research/上证50AH优选_501050.SS/2026-08-03_tradingagents_summary.md
    date: 2026-08-03
    type: TradingAgents中文综述
  - path: /app/ai-berkshire/reports/上证50AH/上证50AH-投资研究.md
    date: 2026-08-03
    type: AI Berkshire四大师投资研究
  - path: research/上证50AH优选指数A_501050.SS/2026-06-25_summary.md
    date: 2026-06-25
    type: 因子对比
  - path: syntheses/a股因子etf对比研究-2026-06-25.md
    date: 2026-06-25
    type: 因子对比
claims:
  - id: claim.501050.tradingagents-20260803
    text: >
      2026-08-03 TradingAgents多智能体分析（3轮辩论）：上证50AH优选(501050)—UNDERWEIGHT。
      技术分析师：HOLD（数据商仅1条K线，无统计意义），情绪分析师：Neutral 5.0/10（全源沉默），
      新闻分析师：偏中性略正面（价值轮动利好），基本面分析师：数据不可用（指数基金无报表），
      多空辩论：多头宏观顺风论证 vs 空头数据完整性硬约束（空方胜），研究经理：Underweight，
      交易员：SELL，风控三方分歧后组合经理终裁：持仓降至2%观察仓、分2-3笔1.70-1.73减持、
      硬止损1.62、场外资金严禁建仓、数据补齐后重审（1-3个月）。
      Underweight源于数据商覆盖残缺（信息盲区）而非基本面恶化，不否定底层策略。
      详见 /app/TradingAgents/reports/501050.SS_20260803_045847/complete_report.md
    status: supported
    confidence: 0.8
    evidence:
      - kind: report
        sourceId: /app/TradingAgents/reports/501050.SS_20260803_045847/complete_report.md
        weight: 0.9
    updatedAt: 2026-08-03T05:20:00.000Z
  - text: 2026-08-03四大师研究：指数PE 10.14（分位66.9%）、PB 1.20（分位75.5%）、股息率2.98%、ROE 11.83%；AH溢价收敛至~122-123；7年跑赢上证50约12.6pct但跑输沪深300；0.60%综合费率偏高；15亿规模Q2净赎回约10%
    status: supported
    confidence: 0.9
    evidence:
      - kind: ai-berkshire-report
        sourceId: /app/ai-berkshire/reports/上证50AH/上证50AH-投资研究.md
        path: /app/ai-berkshire/reports/上证50AH/上证50AH-投资研究.md
        weight: 0.95
        note: 蛋卷估值+中证指数官方编制方案+恒生HSAHP+华夏2026Q2季报交叉验证
  - text: 2026年6月分析报告：501050规模15.43亿元，A类净值1.698(2026-06-08)，前十大含贵州茅台(9.76%)、中国平安H(6.80%)、紫金矿业H(5.80%)等，H股占比约40%，跟踪误差优秀(0.01%/月)
    status: supported
    confidence: 0.8
    evidence: 
      - kind: report
        sourceId: /app/ai-berkshire/reports/上证50AH/上证50AH-投资研究.md
        weight: 0.8
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
updatedAt: 2026-08-03T04:00:00.000Z
sourceIds:
  - /app/TradingAgents/reports/501050.SS_20260803_045847/complete_report.md
  - /home/ariesy/.openclaw/workspace/research/上证50AH优选_501050.SS/2026-08-03_tradingagents_summary.md
  - /app/ai-berkshire/reports/上证50AH/上证50AH-投资研究.md
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
| 基金规模 | 15.02亿元（2026Q2，A类14.74亿+C类0.27亿） |
| 股票仓位 | A股58.69% + 港股通34.92%（2026Q2） |
| 最新净值（A类）| **1.740（2026-07-31）** |
| 成立来收益 | +74.50% |
| 管理费+托管费 | 0.60%/年（管理0.50%+托管0.10%） |

## 业绩表现（指数层面，截止2026-07-31，新浪日线计算）

| 区间 | 50AH优选(000170) | 上证50 | 沪深300 |
|------|:----------:|:--------:|:----:|
| 近 1 年 | +15.00% | +10.23% | +26.51% |
| 近 3 年 | +29.73% | +19.96% | +29.59% |
| 近 5 年 | -4.42% | -14.56% | -4.68% |
| 近 7 年 | +14.63% | +2.01% | +30.16% |
| 2016-12以来 | +40.5% | +32.4% | +48.4% |

**关键判断**（2026-08-03四大师框架更新）：
- **AH择优确有超额**：7年跑赢上证50约12.6pct（近1年超额4.8pp、近3年9.8pp），规则红利真实存在
- **但跑输沪深300**：近7年+14.63% vs +30.16%，底层是上证50"大盘价值"基因，成长/科技牛市中弹性不足
- **5年维度为负**：中间经历过大回撤，并非"低波动稳健"资产
- 指数自行计算与基金季报基准交叉验证偏差<0.6pp，数据可信

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

## 持仓结构（2026Q2前十大）

| 标的 | 市场 | 持仓占比 | 行业 |
|------|------|:--------:|------|
| 贵州茅台 | A | 7.25% | 消费 |
| 兆易创新 | A | 5.33% | 半导体 |
| 寒武纪 | A | 4.91% | AI芯片 |
| 中国平安 | H（02318）| 4.86% | 保险 |
| 招商银行 | A | 4.30% | 银行 |
| 紫金矿业 | H（02899）| 4.00% | 有色 |
| 澜起科技 | A | 3.48% | 半导体 |
| 中微公司 | A | 3.44% | 半导体设备 |
| 海光信息 | A | 3.37% | AI算力 |
| 长江电力 | A | 3.17% | 电力 |

**持仓特征**（2026Q2，前十大合计44.11%）：
- **半导体/AI芯片权重显著**（兆易、寒武纪、澜起、中微、海光合计约20%）——上证50已从"银行+白酒"演变为"金融+半导体+消费"新大盘
- **金融**（A股7.05%+港股18.83%≈26%）与**制造业**（A股37.52%）为两大支柱
- **港股通仓位34.92%**：两地上市的公司大多选持更便宜的H股（如平安H、紫金H），"买便宜"规则的实际体现

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

## 估值水平（2026-07-31，蛋卷）

| 维度 | 50AH优选(000170) | 上证50 | 沪深300 | 标普500 |
|------|------|------|------|------|
| PE | 10.14（分位66.9%）| 11.69（分位84.3%）| 14.38（分位86.7%）| 25.49 |
| PB | 1.20（分位75.5%）| 1.27（分位65.1%）| 1.47（分位52.8%）| 5.49 |
| 股息率 | 2.98% | 3.12% | 2.56% | 1.03% |
| ROE | 11.83% | 10.85% | 10.19% | 21.56% |

**估值解读**（2026-08-03更新）：
- **绝对估值很低**（PE 10.1、PB 1.2、股息2.98%），但**相对自身历史并不便宜**（PE分位66.9%、PB分位75.5%），处于"绝对便宜+相对中高位"的中间地带
- 低PE主要来自金融权重（PE 5-7x），剔除金融后非金融PE约15-20x，"10倍PE"有误导性
- AH溢价已从2024年160+收敛至~122-123（HSAHP 52周区间113.6-127.9），"溢价收敛alpha"基本吃尽，未来超额依赖波动
- 注意：港股通H股股息税20%（内地投资者）会侵蚀2.98%股息的实得收益

## 投资结论

**核心观点**（2026-08-03 AI Berkshire 四大师框架更新）：
- ✅ **机制聪明**：AH择优规则制度化（7年跑赢上证50约12.6pct），"买便宜"写进指数编制
- ⚠️ **0.60%综合费率偏高**：比上证50ETF（0.20%）每年多付约0.4pct，需靠AH规则alpha覆盖
- ⚠️ **超额红利衰减**：AH溢价收敛至~123，未来超额依赖波动而非单边收敛
- ⚠️ **15亿小规模**：Q2单季净赎回约10%，流动性弱于头部ETF
- 📊 **空仓者**：观望/小额定投；若追求AH弹性用低费率港股通ETF，追求大盘价值用上证50ETF
- 📊 **持仓者**：可继续持有（3%股息+AH价差有债底），接受低弹性
- 📈 **加仓信号**：PE<8（分位<30%）或AH溢价重回140+
- 📉 **减仓/换仓信号**：AH溢价<110长期化+成长持续跑赢，策略超额消失时0.60%费率不再值得

**关键跟踪指标**：
1. 恒生AH溢价指数（HSAHP）——核心指标，当前~122-123
2. 指数PE分位（当前66.9%）与股息率
3. 基金规模变化（警惕持续缩水）
4. 上证50中半导体/AI权重（兆易、寒武纪、澜起、中微、海光）合计占比趋势

**最大风险**：AH溢价收敛+大盘价值跑输成长+高费率侵蚀收益

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-06-10-1237](../sources/bridge-workspace-142ea9a2-memory-2026-06-10-1237-65cf7423.md)

### Related Pages

- [华龙](华龙-华夏基金.md)
- [实体提取汇总 2026-06-12](../syntheses/entity-extract-2026-06-12.md)
<!-- openclaw:wiki:related:end -->
