---
pageType: entity
id: entity.project.clawflows
entityType: project
title: Clawflows 工作流引擎
aliases:
  - clawflows
  - check-email workflow
  - CLAWFLOWS_OPENCLAW_AGENT
updatedAt: 2026-08-05T15:11:28.000Z
status: active
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-07-clawflows-scheduler-cron-type-f5bb1936.md
claims:
  - id: claim.clawflows.scheduler-mechanism
    text: "clawflows 的 schedule 使用 OpenClaw 内置的 cron 机制，与系统 crontab 无关（系统 crontab 中没有 clawflows 条目）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-clawflows-scheduler-cron-type-f5bb1936
        weight: 0.85
  - id: claim.clawflows.agent-routing
    text: "clawflows cmd_run 通过环境变量 CLAWFLOWS_OPENCLAW_AGENT 指定执行 agent，默认 main；核心逻辑为 cf_agent=\"${CLAWFLOWS_OPENCLAW_AGENT:-main}\" 后调用 openclaw agent --agent \"$cf_agent\"。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-clawflows-scheduler-cron-type-f5bb1936
        weight: 0.85
  - id: claim.clawflows.scheduler-runs-as-main
    text: "clawflows 的 scheduler cron job 运行在主 agent 下，若要让定时调度也走指定 agent，需要在 cron 环境变量中同样设置 CLAWFLOWS_OPENCLAW_AGENT。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-clawflows-scheduler-cron-type-f5bb1936
        weight: 0.8
  - id: claim.clawflows.workflow-is-prompt
    text: "clawflows workflow 的内容只是 prompt 指令（如 check-email 写的是 Using your email skill），运行时会话自动选择可用 skill 执行，无需额外配置。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-clawflows-scheduler-cron-type-f5bb1936
        weight: 0.8
  - id: claim.clawflows.gog-email-skill
    text: "gog 是 OpenClaw 内置的 Google Workspace 邮件技能（技能列表显示 ready），check-email workflow 可直接用它查 Gmail；inbox-zero agent 已存在（Workspace ~/.openclaw/workspace-inbox-zero）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-clawflows-scheduler-cron-type-f5bb1936
        weight: 0.8
---

# Clawflows 工作流引擎

> 以 prompt 指令形式定义 workflow、由 OpenClaw cron 调度执行的工作流引擎；支持通过环境变量把 workflow 路由到指定 agent。

## 调度机制

| 问题 | 结论 |
|------|------|
| 用 OpenClaw cron 还是系统 crontab？ | **OpenClaw 自己的 cron 机制**，与系统 crontab 无关 |
| 定时任务跑在哪个 agent？ | **主 agent（main）** |
| 如何路由到其他 agent？ | 设置 `CLAWFLOWS_OPENCLAW_AGENT=<agent>` |

## 用法

```bash
# 一次性使用
CLAWFLOWS_OPENCLAW_AGENT=inbox-zero clawflows run check-email

# 定时任务层生效需在 cron 环境变量中同样设置
export CLAWFLOWS_OPENCLAW_AGENT=inbox-zero
```

## 已确认细节

- workflow 内容只是 prompt 指令，运行时由当前 agent 自动选择可用 skill（例如 `gog` 查 Gmail）。
- `gog`：OpenClaw 内置 Google Workspace 邮件技能，技能列表显示 `✓ ready`。
- `inbox-zero` agent 已存在：Workspace `~/.openclaw/workspace-inbox-zero`，Agent dir `~/.openclaw/agents/inbox-zero/agent`。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
