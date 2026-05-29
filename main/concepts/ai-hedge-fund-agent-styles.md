# AI对冲基金多Agent风格分类

> tradingagents项目中14种投资大师Agent的风格分类

**类型:** Concept  
**ID:** `concept_ai_hedge_fund_agent_styles`  
**来源:** tradingagents项目解析

---

## 14种Agent风格

| Agent | 投资风格 | 特点 |
|-------|---------|------|
| Warren Buffett | 价值投资 | 以合理价格买入优质公司 |
| Ben Graham | 价值投资鼻祖 | 强调安全边际，只买隐藏的宝石 |
| Charlie Munger | 逆向价值投资 | 好公司+好价格才买 |
| Peter Lynch | 成长投资 | 寻找"十倍股" |
| Cathie Wood | 激进成长投资 | 相信创新和颠覆 |
| Michael Burry | 逆向交易 | 深度价值狩猎，"大空头" |
| Bill Ackman | 激进维权投资 | 大胆持仓，推动变革 |
| Nassim Taleb | 风险分析 | 关注尾部风险，反脆弱性 |
| Mohnish Pabrai | Dhandho投资 | 低风险高胜率的机会 |
| Phil Fisher | 成长研究 | 深入"scuttlebutt"调研 |
| Stanley Druckenmiller | 宏观对冲 | 成长+不对称机会 |
| Rakesh Jhunjhunwala | 成长趋势 | 印度"大牛" |
| Aswath Damodaran | 估值专家 | 专注于股票估值 |

---

## 分析功能Agent

- **Valuation Agent** — 计算内在价值，生成交易信号
- **Sentiment Agent** — 分析市场情绪，生成交易信号
- **Fundamentals Agent** — 分析基本面数据，生成交易信号
- **Technical Agent** — 分析技术指标，生成交易信号

---

## 风控层

- **Risk Manager** — 计算风险指标，设定持仓限额
- **Portfolio Manager** — 最终交易决策，生成订单

---

*来源: memory/2026-05-13-ai-hedge-fund-research.md*