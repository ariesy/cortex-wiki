---
pageType: entity
id: "entity:pdd-holdings"
entityType: investment_stock
entity_type: investment_stock
privacyTier: public
ticker: "PDD.US"
name: "PDD Holdings (拼多多)"
sector: "电商平台/Temu跨境电商"
last_updated: "2026-06-10"
status: actively_tracking
current_view: >-
  中国第三大电商平台（拼多多主站）+ 全球最大跨境电商平台（Temu）。Q1 2026营收1062亿（+11%），净利润125亿（-15%），利润下滑主因关税冲击+Temu重投入。股价$81.80，距52周高点-41.3%，PE 8.5-10.7x，Forward PE 7.06x，估值极度压缩。现金+短投4361亿（~$600亿），43位分析师一致目标价$145.65（+78%上行空间）。核心风险：de minimis取消、Temu海外监管、关税冲击。核心机会：估值极低、现金流充裕、Temu全球化长期逻辑。
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
    text: "PDD当前PE 8.5-10.7x，Forward PE 7.06x，估值处于历史极低水平，43位分析师一致目标价$145.65"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-11-0059-22f6054a
        weight: 0.85
        note: "stock-research-engine分析"
    updatedAt: "2026-06-10"
  - id: "claim.pdd.cash-reserve"
    text: "PDD持有现金+短期投资4361亿人民币（约$600亿），为极端估值提供安全垫"
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
---

# PDD Holdings (拼多多)

## 基础数据（2026-06-10）

| 指标 | 数值 |
|------|------|
| 最新股价 | ~$81.80（2026/6/9收盘） |
| 52周区间 | $81.01 - $139.41 |
| 距52周高点 | **-41.3%** |
| PE（TTM） | 8.5x - 10.7x |
| Forward PE | 7.06x |
| PB | 1.89x |
| Q1 2026营收 | RMB 1,062亿（+11% YoY） |
| Q1 2026净利润 | RMB 125亿（**-15% YoY**） |
| Non-GAAP净利润 | RMB 141亿（-17% YoY） |
| Non-GAAP利润率 | ~20% |
| 现金+短投 | RMB 4,361亿（~$600亿） |
| FY2025全年营收 | RMB 4,318亿（+10% YoY） |
| Q2 2026 EPS预期 | $21.12 |
| FY2026 EPS预期 | $82.80 |
| 下次财报 | 2026/8/31（Q2） |

## stock-research-engine 分析（2026-06-10）

### 一句话本质
> 买PDD，本质上是在买"中国电商基本盘+Temu全球化期权"的组合，当前处于**极端悲观定价**区间。

### 核心逻辑

**三重增长引擎：**
1. **拼多多主站**：国内电商基本盘，用户规模9亿+，C2M模式持续渗透下沉市场
2. **Temu全球化**：跨境电商第二曲线，已进入70+国家，但处于重投入期
3. **现金储备**：$600亿现金为战略转型提供充足弹药

**核心风险：**
- 美国de minimis政策取消 → Temu直邮模式成本飙升
- 关税冲击 → Q1利润已下滑15%
- 海外监管风险 → 多国对Temu发起调查
- 利润换增长 → 短期盈利承压

**估值分析：**
- Forward PE 7.06x，在中概互联网板块中属于极低水平
- $600亿现金占市值比例极高，提供强安全垫
- 43位分析师一致目标价$145.65，较当前有78%上行空间
- 但Barclays下调至$89（Equal-weight），反映部分机构极度悲观

### 机构评级

| 机构 | 目标价 | 评级 |
|------|--------|------|
| Benchmark | $127（↓from $160） | Buy |
| Citi | $123（↓from $142） | Buy |
| Morgan Stanley | $129（↓from $148） | Overweight |
| Bernstein | $110（↓from $132） | Market Perform |
| Barclays | $89（↓from $165） | **Equal-weight** |

### 跟踪验证清单
1. Q2 2026财报（8/31）：营收增速能否维持，利润能否企稳
2. Temu各国监管进展
3. 美国de minimis政策最终落地时间
4. 关税谈判进展
5. 回购/分红计划

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
