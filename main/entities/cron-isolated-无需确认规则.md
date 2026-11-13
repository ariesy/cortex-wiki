---
pageType: entity
id: entity.concept.cron-isolated-no-confirm
title: cron 调度环境无需人工确认（wiki weekly 整理流程修正）
entityType: concept
aliases:
  - cron 不请求确认
  - wiki-source-entity-extract 确认规则
  - 调度环境无法确认
updatedAt: 2026-11-13T13:04:38.336Z
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-14-1416-5d935581
  - source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
claims:
  - id: claim.cron-no-confirm.2026-08-14.rule
    text: 2026-08-14 确立行为规范：weekly wiki 整理任务（wiki-source-entity-extract）在 cron
      调度环境中运行，属于 isolated 调度环境，发送确认消息无人能回复、会导致流程卡死；因此必须"无需确认、直接处理"，该规则已固化到 cron
      任务说明与 TOOLS.md。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-1416-5d935581
        weight: 1
  - id: claim.cron-no-confirm.2026-08-14.pipeline
    text: wiki weekly 整理流程：周五 21:00 cron 触发 → wiki-weekly-scan.py 扫描增量（本周 555 条）→ 识别
      4 个高优先级 → LLM 拟方案（历史版本会先发群确认）→ 核对去重 → 更新/新建实体并补 claims → 标记已处理 → finish
      收尾（lint 0 errors）。wiki-weekly-mark.py 规则为"只跳过 low，high/medium 必须人工判断"。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-1416-5d935581
        weight: 1
  - id: claim.cron-no-confirm.2026-08-14.dedup-lesson
    text: 该批次方案原本建议"创建 4 个新实体"，执行前核对发现其中 3 个已存在（中国神华、医疗ETF、贵州茅台）、1 个内容已被 concepts
      覆盖（Agent 工程化挑战），若盲从方案会创建重复实体污染 wiki；结论是落盘前必须做实体去重核对。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-1416-5d935581
        weight: 1
  - id: claim.cron-no-confirm.2026-08-14.first-round-wrap
    text: 2026-08-14 wiki 周度整理完成首轮收尾：4 个高优先级条目已处理（中国神华补 kronos 微调 claim、医疗ETF 补
      TradingAgents 减持 claim、贵州茅台/Agent 工程化确认已覆盖），标记 4 个 source，finish 脚本 lint 0
      errors / compile OK 且报告已发。教训：cron 调度环境是 isolated
      session，不能中途发"请确认"消息，否则无人回应会卡流程，应自主处理完只发完成报告；修复方式为在 cron payload
      增加"全程不要发消息请求用户确认"，并在 TOOLS.md 新增「调度任务不得请求确认 ⚠️」规范。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-4613d029
        weight: 0.95
---

# cron 调度环境无需人工确认

## 规则

- 调度环境（cron / isolated session）不发起确认请求，直接执行。
- 人工确认仅适用于交互 session。
- 已固化位置：cron 任务说明（wiki-source-entity-extract）、TOOLS.md、当日 memory。

## 流程

周五 21:00 触发 → 扫描增量 → 过滤 → 实体查重 → 写 entity / claims → mark → finish → lint。

## 相关

- [[wiki-lint-batch-fix-2026-08-05]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-14-1416](../sources/bridge-workspace-142ea9a2-memory-2026-08-14-1416-5d935581.md)
- [Memory Bridge (main): 2026-08-14](../sources/bridge-workspace-142ea9a2-memory-2026-08-14-4613d029.md)

### Related Pages

- [cron-notify.sh 定时任务通知包装机制](cron-notify-通知包装机制.md)
<!-- openclaw:wiki:related:end -->
