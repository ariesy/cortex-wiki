---
pageType: entity
id: entity.concept.cron-notify-wrapper
title: "cron-notify.sh 定时任务通知包装机制"
entityType: concept
aliases:
  - cron 通知包装
  - crontab 静默失败
  - --fail-only 冷却
tags: [cron, 通知, crontab, openclaw-cron, 飞书]
updatedAt: "2026-08-15"
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
  - source.bridge.workspace-142ea9a2.memory-2026-08-15-0007-8ea6e54e
claims:
  - id: claim.cron-notify.inventory
    text: "2026-08-14 盘点通知覆盖情况：OpenClaw cron 11 个 + 系统 crontab 17 个活跃任务；系统 crontab 中 8 个原本无通知的静默任务已用 scripts/cron-notify.sh 包装，成功/失败结果发到群 oc_812b4a80dbf93832f71b6135ef6cb25a。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
        weight: 0.9
  - id: claim.cron-notify.modes
    text: "cron-notify.sh 支持 --fail-only（仅失败通知）与 --cooldown（冷却去重），退出码正确透传。已包装任务：ETF规模每日监控、港股成交量预测、资金流数据抓取、财报数据收集、clashman 流量清理、Bitwarden 每日备份（成功+失败都通知）；mx-data 异步数据获取（--fail-only，冷却 6h）、clashman 流量轮询（--fail-only，冷却 30m）避免刷屏。改动前备份 crontab-20260814-160902.bak。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
        weight: 0.9
  - id: claim.cron-notify.delivery-fix
    text: "OpenClaw cron「Memory Dreaming Promotion」原 delivery=none，改为 announce → 本群（oc_812b4a80dbf93832f71b6135ef6cb25a）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
        weight: 0.85
  - id: claim.cron-notify.announce-pitfall
    text: "OpenClaw cron delivery 配置陷阱：`edit --announce` 可能只设置 fallback 标志，list 显示 mode=none 但 to 已设置，get 确认实际仍为 none；managed 任务 edit 后 delivery 可能被重置——需用 get 验证实际状态而非依赖 list 缓存（缓存文件也可能是编辑前旧数据，需重新拉取）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-15-0007-8ea6e54e
        weight: 0.8
  - id: claim.cron-notify.value
    text: "静默 cron 的价值在于尽早暴露故障：mx-data 批次崩溃从 6 月就反复出现，但直到 8/14 cron-notify 上线才被发现。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
        weight: 0.8
---

# cron-notify.sh 定时任务通知包装机制

## 背景

定时任务失败长期静默，直到人工查日志才发现。2026-08-14 对全部定时任务做通知覆盖盘点并补全。

## 结构

- 系统 crontab：`scripts/cron-notify.sh <cmd>` 包装，通过退出码判定成功/失败
  - `--fail-only`：仅失败通知，避免高频任务刷屏
  - `--cooldown`：冷却窗口去重（mx-data 6h、clashman 轮询 30m）
- OpenClaw cron：通过 delivery（announce）配置投递，部分任务 delivery=none 需手工改为 announce

## 覆盖清单

| 任务 | 通知策略 |
|---|---|
| ETF规模每日监控 / 港股成交量预测 / 资金流抓取 / 财报数据收集 | 成功+失败 |
| clashman 流量清理 / Bitwarden 每日备份 | 成功+失败 |
| mx-data 异步数据获取 | --fail-only，冷却 6h |
| clashman 流量轮询 | --fail-only，冷却 30m |
| OpenClaw cron Memory Dreaming Promotion | delivery none → announce |

## 注意事项

- OpenClaw cron `edit --announce` 不一定生效：用 `get` 验证 delivery 实际状态，list 可能读到缓存旧值，managed 任务 edit 后可能被重置。
- 通知上线后立刻暴露出历史故障（mx-data),说明"能看见失败"比"能重试失败"更优先。

## 相关

- [[cron-isolated-无需确认规则]]
- [[mx-data-null-notnull-crash]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-14](../sources/bridge-workspace-142ea9a2-memory-2026-08-14-4613d029.md)
- [Memory Bridge (main): 2026-08-15-0007](../sources/bridge-workspace-142ea9a2-memory-2026-08-15-0007-8ea6e54e.md)

### Related Pages

- [cron 调度环境无需人工确认（wiki weekly 整理流程修正）](cron-isolated-无需确认规则.md)
<!-- openclaw:wiki:related:end -->
