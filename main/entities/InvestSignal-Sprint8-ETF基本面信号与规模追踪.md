---
pageType: entity
entityType: project
id: entity.project.investsignal-sprint8-etf-signal
updatedAt: "2026-08-28"
relationships:
  - targetId: entity.project.investsignal-sprint4-hk-etf
    targetTitle: "InvestSignal Sprint 4：港股与 ETF 数据支持"
    kind: related
    weight: 0.8
  - targetId: entity.project.investsignal-architecture-v1-1
    targetTitle: "InvestSignal 架构设计 v1.1"
    kind: belongs-to
    weight: 0.8
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-03-21-2e8a5338
---

# InvestSignal Sprint 8：ETF 基本面信号与规模追踪

> entity_type: project

InvestSignal 项目 Sprint 8（2026-03-21）建立 ETF 专属基本面信号体系，并落地 ETF 规模每日追踪。

---

## S8-T8 基金基本面信号计算方法

- 新建模块 `src/analyzer/indicators/etf/`，实现 ETFCollector、ETFCalculator、ETFSignalGenerator
- 三维度指标：
  - **B1 估值**：溢价率 / 净值分位数
  - **B2 持仓**：集中度
  - **B3 流动性**：规模变化 / 换手率
- 22 个单元测试全部通过

## ETF 报告集成

- `SingleStockAnalysis` 新增 `etf_analysis` 字段
- WatchListAnalyzer 集成 ETFSignalGenerator
- ETFCache 缓存，TTL = 6 小时
- 报告模板添加 ETF 专属指标表格（多时间段规模变化）
- 49 个测试全部通过

## ETF 规模每日记录

- 新建数据库表 `etf_scale`
- `ETFScaleDAO`：`save_batch` / `get_latest` / `get_scale_change` / `cleanup_old_data`
- 收集脚本 `scripts/etf_scale_daily.py`
- 定时任务 `0 16 * * *`（每天 16:00 UTC）已注册

| Commit | 描述 |
|--------|------|
| bca9b32 | 添加 etf_scale 表 |
| 7f332f3 | 添加 ETFScaleDAO |
| c4e96c6 | 添加规模收集脚本 |
| 2d2f253 | 添加多时间段展示方法 |
| a84cf03 | 集成到报告生成 |
| 6b000af | 修复短横线显示 |

---

## 待解决问题

### 换手率数据源
- 东方财富 API 不稳定
- 已调研天天基金 / 新浪但覆盖有限
- 暂时移除换手率指标，只保留规模变化
- 回滚 commit：`6bde2be`

### ETF 规模变化展示
- 日变化 / 周变化 / 月变化
- 无数据显示短横线 `-`

---

## Sprint 8 剩余任务（7 个，共 22 故事点）

| 任务 | 描述 | 故事点 |
|------|------|--------|
| S8-T1 | 中文资讯爬虫 | 5 |
| S8-T2 | 英文资讯爬虫 | 5 |
| S8-T3 | 周报格式优化 | 4 |
| S8-T4 | Bug 修复 | 3 |
| S8-T5 | 性能优化 | 3 |
| S8-T6 | MVP 演示验收 | 2 |
| S8-T7 | 股票名称模糊查询 | 3 |

## 定时任务状态

| 脚本 | 状态 |
|------|------|
| `etf_scale_daily.sh` | ✅ 已注册（每天 16:00 UTC） |
| `capital_flow_daily.sh` | ❌ 未注册（API 不稳定） |
| `weekly_report.sh` | ❌ 未注册 |
| `financial_report_collect.sh` | ❌ 未注册 |

---

## 其他

### S8-T1 中文资讯爬虫
T1-T4 全部完成，但因 mx-search API 限流问题回退，commit `55b57a1`。

### mx-data vs AkShare EM API 调研
- 结论：mx-data API 可替代 AkShare `*_em` 接口
- 端点：`https://mkapi2.dfcfs.com/finskillshub/api/claw/query`
- 验证：招商银行收盘价返回正常

### Phase 2 PRD + FunctionSpec
- 项目：InvestSignal Phase 2 - 东财数据接口增强
- 提交：`ee6ae9c`

---

*来源: memory/2026-03-21-2e8a5338.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-03-21](../sources/bridge-workspace-142ea9a2-memory-2026-03-21-2e8a5338.md)
<!-- openclaw:wiki:related:end -->
