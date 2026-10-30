---
pageType: entity
id: daily-incr-dual-scheduler-conflict
title: "daily_incr 双调度器并发冲突（tdx 数据快照损坏）"
tags: [bug, tdx, cron, 数据管道, 并发冲突, flock, daily_incr]
updatedAt: "2026-08-05"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-05-1457-83f98de1
claims:
  - id: claim.daily-incr.symptom
    text: "daily 增量报错表现为 tdxgp `[Errno 2] No such file`、`Size mismatch` 交错写入损坏、tdxfin.zip 多出 2752512 bytes 导致 unzip 失败；后果为股本 records=0、财务 parsed=0。"
    status: supported
    confidence: 0.85
  - id: claim.daily-incr.rootcause
    text: "根因是双调度器并发冲突：系统 crontab 中 daily_incr（`30 9 * * 1-5` UTC = 17:30 CST）与 OpenClaw cron 的 tdx-daily-incr（`30 17 * * 1-5` Asia/Shanghai）在同一时刻触发，两个进程并发写同一 snapshot 目录。"
    status: supported
    confidence: 0.9
  - id: claim.daily-incr.fix
    text: "修复措施：禁用系统 crontab 中重复的 daily_incr 行（保留带状态追踪和飞书 delivery 的 OpenClaw cron）；daily_incr.sh 增加 flock 互斥锁作为双保险；重新下载 tdxgp.zip（739MB）与 tdxfin.zip（537MB）并重跑解析。"
    status: supported
    confidence: 0.9
  - id: claim.daily-incr.result
    text: "修复后数据恢复：股本 ok=8,534、records=134,838,102；财务 skipped=242 parsed=18；K线 12,324 与指数 28,119 未受影响；download_log 当天 6 行全部修正为 success。"
    status: supported
    confidence: 0.8
  - id: claim.daily-incr.weekly-dedup
    text: "weekly_sync / weekly_doctor 同样存在双调度：系统 crontab 周六 18:00/19:00 UTC（= 周日 02:00/03:00 CST），OpenClaw cron 周日 18:00/19:00 UTC（= 周一 02:00/03:00 CST），两者错一天导致每周各跑两次（时间错开不会写坏数据）；用户确认后按同样方式去重：保留 OpenClaw cron 并把时间修正为脚本注释声明的周日 02:00/03:00 CST，注释掉系统 crontab 行。"
    status: supported
    confidence: 0.8
---

# daily_incr 双调度器并发冲突

## 症状（2026-08-05）

- 一个进程报 tdxgp `[Errno 2] No such file`（文件被对方删除/覆盖）
- 另一个进程报 `Size mismatch`（交错写入损坏）
- tdxfin.zip 被写坏（多出 2752512 bytes，unzip 失败）
- 后果：股本 records=0（tdxgp 缺失）、财务 parsed=0（tdxfin 损坏）

## 根因：双调度器并发

| 调度器 | 任务 | 时间 |
|--------|------|------|
| 系统 crontab | daily_incr | `30 9 * * 1-5` UTC = 17:30 CST |
| OpenClaw cron | tdx-daily-incr | `30 17 * * 1-5` Asia/Shanghai |

同一时刻触发，两个进程并发写同一个 snapshot 目录。

## 修复

1. 禁用系统 crontab 中重复的 daily_incr 行（保留 OpenClaw cron —— 它有状态追踪 + 飞书 delivery 到本群）
2. `daily_incr.sh` 加 `flock` 互斥锁 —— 双保险，后到者直接跳过
3. 补数据：重新下载 tdxgp.zip（739MB）+ tdxfin.zip（537MB），单进程下载成功并重跑解析

## 修复结果

- 股本：ok=8,534 → records=**134,838,102**
- 财务：skipped=242 parsed=18（恢复正常）
- K线（12,324）、指数（28,119）未动，本就正常
- download_log 当天 6 行全部修正为 success

## 同类问题：weekly 双调度（已处理）

| 调度器 | 时间 | 说明 |
|--------|------|------|
| 系统 crontab | 周六 18:00/19:00 UTC = 周日 02:00/03:00 CST | 符合脚本注释 |
| OpenClaw cron | 周日 18:00/19:00 UTC = 周一 02:00/03:00 CST | 错了一天 |

两者错开一天不会并发写坏数据，但实际每周跑了两次。处理方式：保留 OpenClaw cron（有飞书 delivery），把时间修正为脚本注释声明的**周日 02:00/03:00 CST**，并注释掉系统 crontab 行。

## 相关实体

- [[mootdx]]（tdx 数据源）
- [[tdx-chronos]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-05-1457](../sources/bridge-workspace-142ea9a2-memory-2026-08-05-1457-83f98de1.md)
<!-- openclaw:wiki:related:end -->
