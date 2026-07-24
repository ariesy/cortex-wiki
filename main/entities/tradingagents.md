---
pageType: entity
entityType: project
id: entity.project.tradingagents
updatedAt: 2026-07-17T13:12:12.861Z
claims:
  - id: claim.tradingagents.2026-07-17.688248-sell
    text: 2026-07-17 TradingAgents 多智能体分析：688248.SS（南网科技）—— SELL 评级。33次LLM调用全部200
      OK。投资组合经理终裁清仓，等估值回归。详见 entities/688248.SH_南网科技.md
    status: active
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-17-1256-78a022e4
        weight: 0.9
    updatedAt: 2026-07-17T12:56:09.722Z
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
