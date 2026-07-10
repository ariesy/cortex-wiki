---
pageType: entity
id: entity.tdx-chronos
title: tdx-chronos
entityType: project
aliases:
  - tdx-chronos 通达信数据平台
updatedAt: 2026-07-08T14:54:13.000Z
status: active
claims:
  - id: claim.tdx-chronos.v1.4.0-release
    text: "Sprint 10 收官，v1.4.0 发布：9 public method 的 Query Facade 层，55/55 测试 PASS，tag v1.4.0"
    status: supported
    confidence: 0.95
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-08-62bf2505
        weight: 0.95
  - id: claim.tdx-chronos.cron-bug-fixes
    text: "Sprint 9 完整闭环：daily_incr.sh 和 weekly_sync.sh 共修复 6 处沉默 bug（bash heredoc f-string NameError + API typo），3 个 cron job 全部首次真跑通"
    status: supported
    confidence: 0.95
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-06-3bcca33e
        weight: 0.95
  - id: claim.tdx-chronos.sprint5-9-fin-domain
    text: "Sprint 5-9 完成财务领域补全：585 字段语义映射、三表勾稽、财务报表分类、10 项 doctor 健康检查、v1.1.0-v1.2.0 双 tag 发布"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-05-46b1d5ff
        weight: 0.9
---
# tdx-chronos

tdx-chronos 是通达信金融数据全量解析与增量同步平台，基于 mootdx 做数据源，用 Parquet 做存储层，提供 K 线、财务、股本、股东等数据的本地化查询 API。

## 技术栈
- 数据源：mootdx（通达信私有协议）
- 存储：Apache Parquet (PyArrow)
- 元数据：SQLite (meta.db)
- 调度：OpenClaw cron jobs
- 部署：Docker 容器，路径 `/app/tdx-chronos`

## 版本里程碑
- **v1.0**: Sprint 0-4，全量解析 + Parquet 优化
- **v1.1.0**: Sprint 5-7 (2026-07-05)，cron 接入 + 股本 type 1-48 语义映射 + 229 PASSED
- **v1.2.0**: Sprint 8 (2026-07-05)，财务领域补全 + 三表勾稽 + 243 PASSED
- **v1.4.0**: Sprint 10 (2026-07-08)，Query Facade + 9 public method + 55/55 PASS

## 9 个 Public Method (v1.4.0)
1. `TdxChronos(data_dir, readonly=True)` — 入口
2. `symbol_info(symbol)` — 标的元数据
3. `list_symbols(market=None)` — 列表
4. `kline(symbol, start, end)` — K 线
5. `list_quarters()` — 财报季度列表
6. `finance(quarter, ratios_only=False)` — 财务数据
7. `shareholders(symbol)` — 股东数据
8. `index_klines(index_code, start, end)` — 指数 K 线
9. `doctor()` — 健康检查报告

## 10 项 Doctor 检查
kline_symbols / financial_quarters / gp_records / index_records / download_log_7d_success_rate / kline_parquet_size_mb / index_freshness_days / error_rate / reconciliation (三表勾稽) / quarter_metadata

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
