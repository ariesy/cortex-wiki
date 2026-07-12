---
pageType: entity
entityType: project
id: entity.project.tradingagents
updatedAt: 2026-07-12T08:27:42.451Z
claims:
  - id: claim.tradingagents.2026-07-10.159828
    text: 2026-07-12 TradingAgents 多智能体分析：159828.SZ（国泰中证医疗ETF）—— Hold 评级，目标价 0.43
      元，时间窗口 3-6 个月，硬止损 0.358。详见 [[中证医疗etf-159828-sz-2026-07-12-双框架对比分析]] 和
      [[159828.SZ_国泰中证医疗ETF]]
    status: active
    confidence: 0.85
    evidence:
      - kind: research-report
        path: research/国泰中证医疗ETF_159828.SZ/2026-07-10/tradingagents_raw.log
        weight: 0.9
        confidence: 0.9
        note: TradingAgents 多智能体分析，minimax-cn (Minimax-M3 deep + MiniMax-M2.7-highspeed
          quick)，depth=3
    updatedAt: 2026-07-12T08:22:00+08:00
relationships:
  - targetId: concept.ai-hedge-fund-agent-styles
    targetTitle: AI对冲基金多Agent风格分类
    kind: describes
    weight: 0.9
    note: 14种Agent风格的详细说明
  - targetId: entity.document.autonomous-research-agents-survey-2026
    targetTitle: From Copilots to Colleagues
    kind: related-research
    weight: 0.6
---

# tradingagents

> AI对冲基金模拟系统，通过14种投资大师Agent协作进行股票分析决策

**类型:** Project  
**状态:** research  
**ID:** `project_tradingagents`  
**来源:** 2026-05-13深度研究

---


## 基本信息

| 项目 | 内容 |
|------|------|
| **GitHub** | virattt/ai-hedge-fund |
| **定位** | AI对冲基金**模拟**系统，仅用于教育目的 |
| **不支持** | 实盘交易 |

---

## 14种投资风格Agent

| Agent | 投资风格 |
|-------|---------|
| Warren Buffett | 价值投资 |
| Ben Graham | 价值投资鼻祖，强调安全边际 |
| Charlie Munger | 逆向价值投资 |
| Peter Lynch | 成长投资，寻找"十倍股" |
| Cathie Wood | 激进成长投资 |
| Michael Burry | 逆向交易，"大空头" |
| Bill Ackman | 激进维权投资 |
| Nassim Taleb | 风险分析，反脆弱性 |
| Mohnish Pabrai | Dhandho投资，低风险高胜率 |
| Phil Fisher | 成长研究，深入调研 |
| Stanley Druckenmiller | 宏观对冲 |
| Rakesh Jhunjhunwala | 成长趋势，印度"大牛" |
| Aswath Damodaran | 估值专家 |

---

## 市场支持

| 市场 | 状态 | 数据源 |
|------|------|--------|
| 美股 | ✅ 明确支持 | financialdatasets.ai |
| 港股 | ⚠️ 架构可扩展，数据不支持 | — |
| A股 | ❌ 不支持 | — |

---

## 核心局限

1. **仅模拟，不执行实盘** — 只是模拟，不会真的下单
2. **数据源单一** — 依赖付费 financialdatasets.ai
3. **美股专用** — 港股/A股需要数据层改造

---

## 适合场景

| 场景 | 适用度 |
|------|--------|
| 初步筛选股票（从100支选到10支） | ⭐⭐⭐⭐⭐ |
| 验证自己的投资观点 | ⭐⭐⭐⭐ |
| 学习不同投资大师思维框架 | ⭐⭐⭐⭐⭐ |
| 构建投资决策检查清单 | ⭐⭐⭐⭐ |
| 实盘跟单 | ❌ 不支持 |

---

*来源: memory/2026-05-13-ai-hedge-fund-research.md*

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
