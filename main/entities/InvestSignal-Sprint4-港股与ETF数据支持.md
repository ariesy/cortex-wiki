---
pageType: entity
entityType: project
id: entity.project.investsignal-sprint4-hk-etf
updatedAt: "2026-08-28"
relationships:
  - targetId: entity.project.investsignal-architecture-v1-1
    targetTitle: "InvestSignal 架构设计 v1.1"
    kind: belongs-to
    weight: 0.9
  - targetId: entity.project.investsignal-sprint3-capital-signal
    targetTitle: "InvestSignal Sprint 3：融资融券与资金面信号模块"
    kind: related
    weight: 0.6
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-03-17-bb7cf45c
---

# InvestSignal Sprint 4：港股与 ETF 数据支持

> entity_type: project

InvestSignal 项目 Sprint 4（2026-03-17）打通港股与 ETF 数据采集，期间发现并绕过东方财富 API 封禁。

---

## S4-T9 港股数据支持

- 完成港股数据收集器 `hkstock_collector.py`
- 完成 WatchListAnalyzer 集成
- 腾讯控股 (0700.HK) 加入观察列表
- 通过智者委员会 Tech Spec 审核并采纳改进建议
- 修复代码格式转换逻辑：5 位 → 4 位（港股代码）
- 测试：港股收集器 14 个单测通过

## S4-T10 InvestSignal Skill

- 已完成

## S4-T11 ETF 数据支持

- 发现问题：东方财富 API 被封禁
- 解决方案：改用新浪财经接口 `akshare.fund_etf_hist_sina`
- 完成 ETF 收集器 `etf_collector.py` 与 WatchListAnalyzer 集成
- 沪深300ETF (510300.SH) 加入观察列表
- 测试：ETF 收集器 11 个单测通过

---

## 重要发现：数据源可用性

- **东方财富 API 被封**：所有 A 股 / ETF 数据获取失败
- **新浪财经可用**：
  - `akshare.fund_etf_hist_sina` — ETF 历史数据 ✅
  - `akshare.stock_zh_index_spot_sina` — 指数实时行情 ✅
- **港股可用**：`yfinance` 可正常获取港股数据

---

## 观察列表

| 代码 | 名称 | 市场 |
|------|------|------|
| 510300.SH | 沪深300ETF | ETF |
| 0700.HK | 腾讯控股 | 港股 |
| 600036.SH | 招商银行 | A股 |

---

*来源: memory/2026-03-17-bb7cf45c.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-03-17](../sources/bridge-workspace-142ea9a2-memory-2026-03-17-bb7cf45c.md)
<!-- openclaw:wiki:related:end -->
