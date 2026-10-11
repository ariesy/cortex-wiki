---
pageType: entity
id: entity.project.tradingagents-tauric
entityType: project
title: TradingAgents (Tauric Research)
aliases:
  - TradingAgents
  - TauricResearch/TradingAgents
updatedAt: 2026-08-05T15:11:28.000Z
status: active
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-trading-agents-framework-69da0319.md
claims:
  - id: claim.tradingagents-tauric.arch
    text: "TradingAgents(来自 Tauric Research / UCLA)是基于 LangGraph 的多代理 LLM 金融交易框架，模拟真实量化交易公司运作：5 层架构、约 12 个 Agent（分析师团队 → 研究员团队 → 交易员 → 风险管理 → 投资组合经理）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-trading-agents-framework-69da0319
        weight: 0.85
  - id: claim.tradingagents-tauric.agents
    text: "核心 Agent 职责：基本面/情感/新闻/技术分析师（各维度分析）、多空研究员（辩论分析师报告）、交易员（决定时机与仓位）、风险管理团队（评估波动性/流动性）、投资组合经理（最终批准或否决交易提案）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-trading-agents-framework-69da0319
        weight: 0.8
  - id: claim.tradingagents-tauric.install
    text: "安装：git clone github.com/TauricResearch/TradingAgents，conda 环境 python=3.13 后 pip install .；支持 Docker（docker compose run --rm tradingagents）；CLI 入口 tradingagents / python -m cli.main；Python 调用 TradingAgentsGraph.propagate(ticker, date)。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-trading-agents-framework-69da0319
        weight: 0.8
  - id: claim.tradingagents-tauric.datasources
    text: "外接数据源默认 yfinance，可切换 Alpha Vantage；涉股票行情/技术指标/基本面/新闻，舆情为内置情感分析。切换方式：config['data_vendors']['core_stock_apis'] 及 config['tool_vendors'][<tool>] 覆盖，并设置 ALPHA_VANTAGE_API_KEY。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-trading-agents-framework-69da0319
        weight: 0.8
---

# TradingAgents (Tauric Research)

> 基于 LangGraph 的多代理 LLM 金融交易框架（Tauric Research / UCLA），模拟真实量化交易公司的分工。

⚠️ 注意与另一同名项目 [`tradingagents.md`](tradingagents.md)（virattt/ai-hedge-fund，14 种投资大师风格 Agent）区分——两者命名相同但架构、来源、数据源完全不同。

## 架构：5 层 × ~12 个 Agent

分析师团队 → 研究员团队 → 交易员 → 风险管理 → 投资组合经理

| Agent | 职责 |
|-------|------|
| 基本面分析师 | 评估公司财报、业绩指标、intrinsic value |
| 情感分析师 | 分析社媒/舆情情感评分 |
| 新闻分析师 | 监控全球新闻、宏观经济指标 |
| 技术分析师 | MACD、RSI 等技术指标识别交易模式 |
| 多空研究员 | 辩论分析师报告，平衡风险收益 |
| 交易员 | 综合所有报告，决定交易时机和仓位 |
| 风险管理团队 | 评估波动性、流动性等风险因素 |
| 投资组合经理 | 最终批准/否决交易提案 |

## 安装

```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
conda create -n tradingagents python=3.13
conda activate tradingagents
pip install .
# 或 Docker
cp .env.example .env   # 填入 API keys
docker compose run --rm tradingagents
```

CLI：`tradingagents` 或 `python -m cli.main`

Python 调用：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

## 外接数据源

| 类别 | 数据源 | 说明 |
|------|--------|------|
| 股票数据 | `yfinance`（默认）/ Alpha Vantage | 每日 OHLCV、财务数据 |
| 技术指标 | `yfinance`（默认）/ Alpha Vantage | MACD、RSI 等 |
| 基本面数据 | `yfinance`（默认）/ Alpha Vantage | 财报、营收、利润 |
| 新闻数据 | `yfinance`（默认）/ Alpha Vantage | 新闻、宏观事件 |
| 舆情 | 内置情感分析 | 社媒情感评分 |

切换数据源：

```python
config = DEFAULT_CONFIG.copy()
config["data_vendors"]["core_stock_apis"] = "alpha_vantage"   # 替换 yfinance
config["tool_vendors"]["get_stock_data"] = "alpha_vantage"    # 单工具覆盖
```

同时需设置 `ALPHA_VANTAGE_API_KEY`。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
