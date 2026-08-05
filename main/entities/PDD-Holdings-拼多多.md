---
pageType: entity
id: "entity:pdd-holdings"
entityType: investment_stock
entity_type: investment_stock
privacyTier: public
ticker: "PDD.US"
name: "PDD Holdings (拼多多)"
sector: "电商平台/Temu跨境电商"
last_updated: "2026-08-04"
status: actively_tracking
current_view: >-
  全球最大C2M社交电商平台（拼多多主站）+ 全球最大跨境电商（Temu）。TTM收入4424亿（+10%），净利968亿（-13%），利润下滑主因关税+Temu重投入。股价$90.15（2026/8/3），52周区间$71.94-$139.41，YTD -20.8%。PE(TTM) 9.64x，Forward PE 8.10x，FCF Yield 12.18%，净现金占市值48.9%，估值极度压缩（历史底部）。分析师共识Buy（37位，目标价均值$116.10）。AI Berkshire四大师分析（2026-08-04）：中性情景3年+65.7%，悲观情景也不亏钱，属"下有底、上无天花板"的非对称机会。核心风险：Temu盈利假设、de minimis取消、地缘政治。核心机会：估值历史底部、现金流充裕、Temu全球化期权。
catalysts:
  - date: "2026-08-31"
    event: "Q2 2026财报发布"
    type: 财报
    direction: 待观察
    status: pending
  - date: ongoing
    event: "美国de minimis政策变化"
    type: 政策
    direction: 利空
    status: pending
  - date: ongoing
    event: "Temu海外监管进展"
    type: 监管
    direction: 利空
    status: pending
  - date: ongoing
    event: "关税谈判进展"
    type: 贸易政策
    direction: 利空
    status: pending
  - date: ongoing
    event: "Temu盈亏平衡/回购计划信号"
    type: 基本面
    direction: 利好
    status: pending
claims:
  - id: "claim.pdd.q1-2026-profit-decline"
    text: "PDD Q1 2026净利润125亿（-15% YoY），利润下滑主因关税冲击+Temu供应链重投入"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-11-0059-22f6054a
        weight: 0.9
        note: "PDD官方Q1 2026财报数据"
    updatedAt: "2026-06-10"
  - id: "claim.pdd.valuation-extreme"
    text: "PDD当前PE(TTM) 9.64x，Forward PE 8.10x，P/S 2.00x，FCF Yield 12.18%，净现金占市值48.9%，估值处于历史极低水平（5年PE最低9.31x）"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: research-report
        sourceId: "reports/PDD/pdd-investment-research.md"
        weight: 0.9
        note: "AI Berkshire四大师分析（2026-08-04），StockAnalysis+Yahoo交叉验证"
    updatedAt: "2026-08-04"
  - id: "claim.pdd.berkshire-verdict"
    text: "AI Berkshire四大师结论：生意质量★★★★★、护城河★★★★☆、管理层★★★☆☆、估值★★★★★。中性情景3年目标$149.34（+65.7%），悲观情景+2.0%不亏钱。建议空仓者建仓5-10%（止损$65），持仓者<15%可加仓。最大不确定性是地缘政治而非商业竞争"
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: research-report
        sourceId: "reports/PDD/pdd-investment-research.md"
        weight: 0.9
        note: "AI Berkshire四大师分析（2026-08-04）"
    updatedAt: "2026-08-04"
  - id: "claim.pdd.tradingagents-underweight"
    text: "TradingAgents多智能体分析（2026-08-04）最终决策：Underweight减持，建议在$88-92反弹中减持约25%仓位，保留60%核心仓+40%现金，不全部退出。技术面：净利连降三季（¥30.75B→¥12.55B）、净利率从28.6%压缩至11.8%、股价超买（上布林带$89.46上方、偏离10日EMA约3.8%、量能稀薄6.4M vs 崩跌期40.4M）、低于下降的200日均线$103.64约13%。基本面底部：$60B净现金（市值45%）、TTM FCF ~$107B、剔除现金PE ~5x。分层止损：$84警告/$82-83加深削减/$73六月低点最终断路器。加仓触发：Q2利润率企稳（净利率18%+）、实际回购执行、放量收复200日均线"
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: research-report
        sourceId: "reports/PDD_20260804_124200/"
        weight: 0.9
        note: "TradingAgents多智能体分析（2026-08-04），deepseek-v4-flash，12 Agents/7 Reports"
    updatedAt: "2026-08-04"
  - id: "claim.pdd.cash-reserve"
    text: "PDD持有现金+短期投资4361亿人民币（约$60B+），净现金占市值48.9%，为极端估值提供安全垫"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-11-0059-22f6054a
        weight: 0.9
    updatedAt: "2026-06-10"
relationships:
  - targetId: "entity:中概互联网ETF"
    targetTitle: "中概互联网ETF (513050)"
    kind: "constituent"
    weight: 0.7
    note: "PDD是中概互联网ETF的成分股之一"
  - targetId: "entity:黄金ETF"
    targetTitle: "黄金ETF"
    kind: "alternatives"
    weight: 0.3
    note: "同为避险/配置类资产讨论中的标的"
sourceIds:
  - /app/ai-berkshire/reports/PDD/
updatedAt: 2026-08-05T15:11:38.000Z

---

# PDD Holdings (拼多多)

## 基础数据（2026-08-04 更新）

| 指标 | 数值 |
|------|------|
| 最新股价 | $90.15（2026/8/3收盘） |
| 市值 | $128.01B |
| 52周区间 | $71.94 - $139.41 |
| 年初至今 | **-20.8%** |
| PE（TTM） | **9.64x**（5年最低9.31x，中位~17-20x） |
| Forward PE | 8.10x |
| P/S | 2.00x（历史最低） |
| P/B | 2.28x |
| P/FCF | 8.21x |
| EV/EBITDA | 4.53x |
| FCF Yield | **12.18%** |
| 净现金/市值 | **48.9%** |
| 分析师共识 | Buy（18 Strong Buy/4 Buy/14 Hold/1 Sell），目标价均值$116.10 |
| TTM收入（Q1'26） | RMB 4,424亿（+10% YoY） |
| TTM净利 | RMB 968亿（-13% YoY） |
| 现金+短投 | RMB 4,361亿（~$60B+） |
| 下次财报 | 2026/8/31（Q2） |

## AI Berkshire 四大师分析（2026-08-04）

> 报告路径：`/app/ai-berkshire/reports/PDD/pdd-investment-research.md`
> 数据截止：2026-08-03 | 模型：opencode-go/deepseek-v4-pro

### 生意质量（段永平）★★★★★
全球最高效的零售平台：17,000-25,000人创造$64B年收入+$12B+净利润，EBITDA margin超25%。轻资产+高ROIC+强网络效应。收入结构已从广告（49.5%）转向交易佣金（50.5%），货币化模式更稳定。毛利率下降是佣金占比提升的数学结果，经营利润率稳定在21-22%。

### 护城河（巴菲特）★★★★☆
网络效应+规模效应双护城河：拼团飞轮（买家→商家→价格→买家），Temu MAU已超Amazon全球。AI推荐需要海量行为数据训练，数据规模本身是壁垒。护城河整体在变宽但速度放缓。最大外部威胁是地缘政治——护城河无法防御的变量。

### 管理层（段永平+巴菲特）★★★☆☆
陈磊是优秀执行者（CTO背景）但非黄峥式天才战略家。**最大治理缺陷：$62.5B净现金零回购零分红**（占市值48.9%），市场无法定价现金价值。黄峥已完全退出运营但持股~26%。

### 估值（巴菲特+段永平）★★★★★
9.64x P/E + 12.18% FCF Yield + 48.9%净现金占比，市场定价暗含"零增长+盈利持续恶化"假设。反向DCF：市场对Temu几乎没有给价值。

| 情景 | 3年EPS增速 | 目标PE | 3年目标价 | 涨跌幅 |
|------|-----------|--------|----------|--------|
| 🟢乐观 | 18% | 15x | $230.40 | **+155.6%** |
| 🟡中性 | 10% | 12x | $149.34 | **+65.7%** |
| 🔴悲观 | 3% | 9x | $91.98 | **+2.0%** |

**关键发现：即使最悲观假设（3%增长+9x PE），3年也不亏钱。** 内在价值保守区间 $145B-$225B（vs 当前$128B），上行13-76%。

### 风险（芒格逆向思考）
1. Temu被多国禁止/高关税取消成本优势（中25%概率，致命-40%）
2. 国内增长放缓+抖音/快手竞争（中高40%，-20%）
3. 管理层资本配置失误（15%）
4. **最大不确定性是地缘政治，不是商业竞争**

### 操作区间建议

| 区间 | 建议 |
|------|------|
| <$75 | 重仓买入区（PE<8x，FCF Yield>15%） |
| $75-100 | 加仓区（当前$90.15在此区间） |
| $100-130 | 持有区 |
| $130-160 | 减仓观望区 |
| >$160 | 卖出区 |

### 综合决策
- **空仓者**：建议建仓，初始仓位5-10%，止损$65
- **持仓者**：若持仓<15%建议加仓
- **卖出信号**：连续2季度收入增速<5%+FCF大幅负转；Temu退出3个以上主要市场；重大欺诈/丑闻
- **加仓信号**：跌至<$75；Temu宣布盈亏平衡；公司宣布回购

## TradingAgents 多智能体分析（2026-08-04）

> 报告路径：`/app/TradingAgents/reports/PDD_20260804_124200/`
> 配置：Deep模式，4分析师（市场/舆情/新闻/基本面）+ 研究团队 + Trader + 风控 + 组合管理，12 Agents 全完成，耗时38分41秒

### 最终决策：Underweight（减持）

**核心操作：在 $88-92 反弹中减持约25%仓位，保留60%核心仓 + 40%现金，不全部退出**

| 维度 | 结论 |
|------|------|
| Market Analyst | Action: Sell（超买+趋势向下，但建议减持而非清仓） |
| Trader | FINAL PROPOSAL: **HOLD**（技术面：$90.15 确认，无数据异常） |
| 风控团队 | 一致同意部分减持（Aggressive/Conservative/Neutral 三分析师收敛） |
| Portfolio Manager | **Underweight**，减持25%入 $88-92 强势区 |

**空方逻辑（占优）：**
- 净利连降三季：¥30.75B → ¥29.33B → ¥23.02B → ¥12.55B（Q1'26）
- 净利率从 FY24 的 28.6% 压缩至 Q1'26 的 11.8%，经营利润率 27.5%→18.4%
- 技术面超买：上布林带 $89.46 上方、偏离10日EMA约3.8%、量能仅6.4M股（崩跌期40.4M）
- 低于下降中的200日均线 $103.64 约13%——逆势反弹，非趋势反转
- 无回购执行（股本持平/微增）、零分红；股价已高于 Daiwa $80 和 BNP $89 目标价
- Q2 同比基数极高（2025Q2 净利¥30.75B），再降两位数可能回测 $80

**多方底部（阻止清仓）：**
- 净现金 ¥436.1B（占市值45%）、总债务仅 ¥5.1B、TTM FCF ~¥107B
- 剔除现金后 P/E ~5x；ROE 25%——"不断壮大的堡垒，而非恶化的价值陷阱"
- ATR收缩表明恐慌阶段结束；舆情冷淡（5.5/10低信心）无拥挤多头

**风险防护（分层止损）：**
1. 收盘跌破50日均线 ~$84 → 警告，进一步减持
2. 持续收盘跌破 $82-83 支撑区 → 加深削减
3. 跌破 $73（6月低点）→ 最终断路器

**回补/加仓触发（需其一）：**
- Q2 净利润率企稳（≥18%）
- 实际回购导致股本下降
- 放量收复下降中的200日均线 ~$103.64

**时间框架：1-2个季度**（穿越8月底 Q2 财报催化剂）

## 跟踪验证清单
1. Q2 2026财报（8/31）：营收增速能否维持，利润能否企稳
2. Temu各国监管进展与盈亏平衡进度
3. 美国de minimis政策最终落地时间
4. 关税谈判进展
5. 回购/分红计划（$62.5B现金的处置）

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
