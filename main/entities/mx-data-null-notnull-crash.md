---
pageType: entity
id: entity.bug.mx-data-null-notnull-crash
title: "mx-data 空数据 None 写入 NOT NULL 崩溃"
entityType: concept
aliases:
  - mx_data_IntegrityError
  - batch 7 失败
  - .get 默认值陷阱
tags: [bug, python, sqlite, cron, mx-data, 防御性编程]
updatedAt: "2026-08-15"
status: resolved
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-15-0319-76c42cf2
claims:
  - id: claim.mxdata-notnull.symptom
    text: "症状：定时任务「mx-data 异步数据获取」整天崩溃（exit=1），日志反复出现「资金流响应数据为空」「股票价格响应数据为空: 510500/512600」；问题自 2026-06 起就存在，只是 cron-notify 8/14 上线后才暴露。"
    status: supported
    confidence: 0.9
  - id: claim.mxdata-notnull.rootcause
    text: "根因链：mx-data API 对部分查询返回空 → Provider 返回空字典（trade_date=None、close=None）→ DAO 用 data.get('trade_date', 默认值)，但 key 存在且值为 None 时 .get 默认值不生效 → None 写入 NOT NULL 字段报 sqlite3.IntegrityError（fund_flow_cache、index_data、northbound_cache 三表）→ _handle_success 未捕获保存异常，单个标的拖垮整个批次。"
    status: supported
    confidence: 0.95
  - id: claim.mxdata-notnull.fix
    text: "修复（commit 28ff630，2 个文件，最小防御性修改）：mx_data_dao.py 中 fund_flow/northbound/etf_info 的 trade_date 改为 data.get('trade_date') or 今天；save_market_index 在 close 为 None 时跳过保存并记 warning；_save_stock_price 跳过缺 trade_date 的行；mx_job_scheduler.py 中单个标的保存失败不再中断批次，计入失败并进重试队列。"
    status: supported
    confidence: 0.95
  - id: claim.mxdata-notnull.verify
    text: "验证：语法检查通过后手动重跑失败批次 --batch=7 → 「批次 7 完成: 成功 6, 失败 0」，exit=0，无异常。"
    status: supported
    confidence: 0.95
---

# mx-data 空数据 None 写入 NOT NULL 崩溃

## 症状

`mx-data 异步数据获取` 定时任务每天崩溃（exit=1），上游 API 对部分标的返回空数据。

## 根因

1. Provider 对空响应返回空字典：`trade_date=None`、`close=None`
2. DAO 用 `data.get('trade_date', 默认值)` —— **key 存在但值为 None 时默认值不生效**，None 直接入 `NOT NULL` 字段
3. `sqlite3.IntegrityError: NOT NULL constraint failed`（fund_flow_cache / index_data / northbound_cache）
4. `_handle_success` 不捕获保存异常 → 单标的失败拖垮整批

## 修复（commit 28ff630）

- `mx_data_dao.py`
  - trade_date：`data.get('trade_date') or 今天`
  - `save_market_index`：close 为 None 跳过保存（warning）
  - `_save_stock_price`：跳过缺 trade_date 的行
- `mx_job_scheduler.py`：单标的保存失败计入失败并进重试队列，不中断批次

## 验证

`--batch=7` 重跑：成功 6，失败 0，exit=0。

## 教训

- `dict.get(key, default)` 对显式 None 无效，空值回退应写 `or` 或显式判 None。
- 批处理必须有 per-item 异常边界，避免单点失败放大为整批失败。
- 静默 cron 会让遗留故障潜伏数月，通知覆盖是排障前提。

## 相关

- [[cron-notify-通知包装机制]]
- [[cron-isolated-无需确认规则]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-15-0319](../sources/bridge-workspace-142ea9a2-memory-2026-08-15-0319-76c42cf2.md)
<!-- openclaw:wiki:related:end -->
