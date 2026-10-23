---
pageType: entity
id: entity:alphasift-screen-result-not-persisted-bug
entityType: bug
privacyTier: public
name: AlphaSift 选股结果不落盘 Bug
title: AlphaSift 选股结果不落盘 Bug
status: open
severity: medium
first_seen: '2026-08-02'
last_updated: '2026-08-02'
updatedAt: '2026-10-23T13:00:00.000Z'
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-02-1237-787acbad
claims:
  - id: claim.alphasift.results-memory-only-bug
    text: >-
      2026-08-02 排查 alphasift screen 任务"执行成功但结果找不回"问题，结论为 Bug 而非任务失败：
      POST /api/v1/alphasift/screen/tasks 提交的后台任务（task_id 67ca6733e31b4de5a6806977f5764501）
      时间线完整走通——05:38:12 创建 202、05:38:24 全市场快照获取成功（em_datacenter 5197 行）、
      05:39:19 发出 LLM 排序请求（deepseek-v4-flash）、05:40:11 LLM 返回 200、05:40:20
      [TaskQueue] 自定义任务完成。根因：API 侧 submit_background_task 只把结果放在内存 task_queue 的
      _tasks dict 中，未像 CLI 的 --save-run 那样调用 save_screen_result 落盘；data/alphasift/ 目录不存在、
      数据库无 alphasift 表；且日志系统只记录 LLM 请求体、不记录响应体，导致页面丢失 task_id 后结果不可恢复。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-02-1237-787acbad
        weight: 0.85
  - id: claim.alphasift.hardfilter-pool-recovered
    text: >-
      该次 alphasift 选股中能从日志恢复的仅为硬筛候选池 6 只（评分/现价/涨跌幅/PE）：
      601211 国泰海通 89.5 分 18.36 元 -3.52% PE 14.7（反转 99.7 领先）、002142 宁波银行 87.9 分 31.88 元
      -3.10% PE 7.0、601328 交通银行 83.3 分 7.18 元 -1.91% PE 6.6（价值 90.1 领先）、
      600309 万华化学 81.9 分 74.51 元 -2.68% PE 17.7、000425 徐工机械 80.8 分 8.96 元 -2.50% PE 15.9、
      002508 老板电器 80.0 分 15.94 元 -3.63% PE 12.3；LLM 排序结果（market_view / ranked JSON、理由、
      风险标签）无法恢复。
    status: supported
    confidence: 0.80
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-02-1237-787acbad
        weight: 0.80
  - id: claim.alphasift.fix-proposal
    text: >-
      修复建议（尚未实施）：API 保存 run 到 data/alphasift/runs/（复用 CLI 的 save_screen_result），
      并在日志中记录 LLM 响应体；按开发规范先写设计文档再动手。临时绕过方式：浏览器页面未关闭时可直接
      重查 task_id 取回，否则重跑（硬筛数秒、LLM 排序约 1 分钟）。
    status: proposed
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-02-1237-787acbad
        weight: 0.75
---

# AlphaSift 选股结果不落盘 Bug

> 任务执行成功、LLM 也正常返回，但结果只活在内存里 —— 页面一刷新就永久丢失。

## 现象

| 项 | 内容 |
|----|------|
| 触发 | `POST /api/v1/alphasift/screen/tasks` 提交后台选股任务 |
| 症状 | 页面刷新/丢失 `task_id` 后，前端再也取不到 LLM 排序结果 |
| 误导性 | 日志显示任务**完全成功**（`[TaskQueue] 自定义任务完成`），容易误判为"任务没跑" |

## 时间线（2026-08-02 UTC，task_id `67ca6733e31b4de5a6806977f5764501`）

| 时间 | 事件 |
|------|------|
| 05:38:12 | 创建任务，返回 202 |
| 05:38:24 | 全市场快照获取成功（em_datacenter，5197 行） |
| 05:39:19 | 发出 LLM 排序请求（deepseek-v4-flash） |
| 05:40:11 | LLM 返回 200 OK |
| 05:40:20 | `[TaskQueue] 自定义任务完成` |

## 根因

1. **结果只存内存**：API 流程 `submit_background_task` 把结果塞进内存 `task_queue._tasks` dict，
   没有像 CLI（`--save-run`）一样调用 `save_screen_result` 落盘。
2. **无处可查**：`data/alphasift/` 目录不存在，数据库中也没有 alphasift 表。
3. **日志缺响应体**：只记录 LLM 请求体（含候选池），不记录响应体，排序结论/理由/风险标签全部丢失。

## 可恢复 / 不可恢复

**可恢复 —— 硬筛候选池（6 只）**

| 代码 | 名称 | 评分 | 现价 | 涨跌幅 | PE | 领先维度 |
|------|------|------|------|--------|-----|----------|
| 601211 | 国泰海通 | 89.5 | 18.36 | -3.52% | 14.7 | 反转 99.7 |
| 002142 | 宁波银行 | 87.9 | 31.88 | -3.10% | 7.0 | — |
| 601328 | 交通银行 | 83.3 | 7.18 | -1.91% | 6.6 | 价值 90.1 |
| 600309 | 万华化学 | 81.9 | 74.51 | -2.68% | 17.7 | — |
| 000425 | 徐工机械 | 80.8 | 8.96 | -2.50% | 15.9 | — |
| 002508 | 老板电器 | 80.0 | 15.94 | -3.63% | 12.3 | — |

**不可恢复** —— LLM 排序结果（`market_view` / `ranked` JSON、理由、风险标签）

## 修复方案（待实施）

- API 侧增加落盘：保存 run 到 `data/alphasift/runs/`（复用 `save_screen_result`）。
- 日志系统记录 LLM 响应体，便于事后审计与恢复。
- 按开发规范：先写设计文档，再动代码。

## 相关

- 临时绕过：浏览器页面若未关闭，可凭原 `task_id` 重查；否则重跑（硬筛数秒，LLM 排序约 1 分钟）。
- 涉及工具链：`alphasift`（选股）、`em_datacenter`（全市场快照）。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-02-1237](../sources/bridge-workspace-142ea9a2-memory-2026-08-02-1237-787acbad.md)
<!-- openclaw:wiki:related:end -->
