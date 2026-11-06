---
pageType: entity
id: entity.tool.gh-tracker
title: gh-tracker 技能
entityType: tool
aliases:
  - gh-tracker
  - github-pr-issue-tracker
updatedAt: 2026-08-09T15:20:20.174Z
status: active
claims:
  - id: claim.gh-tracker.rename
    text: "GitHub PR/Issue 追踪技能由 `github-pr-issue-tracker` 重命名为 `gh-tracker`（目录 `skills/gh-tracker/`），旧目录删除，targets.json 与 state 基线数据完整迁移，cron 任务名与命令路径同步更新。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-1520-6c990129
        weight: 0.85
  - id: claim.gh-tracker.nl-manage
    text: "gh-tracker 通过 `scripts/manage.sh` 支持自然语言增删查目标：`list` 列出目标、`add --name <名> --repo <owner/repo> [--pr N] [--issue N]` 添加（含重复检测、repo 格式校验、自动备份）、`remove --name <名>` 删除（同步清理 state）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-1520-6c990129
        weight: 0.85
  - id: claim.gh-tracker.targets
    text: "gh-tracker 默认追踪 3 个目标：daily-stock-analysis（ZhuLinsen/daily_stock_analysis，PR #2154 / Issue #2153）、trading-agents（TauricResearch/TradingAgents，PR #1205 / Issue #1204）、serverless-registry（cloudflare/serverless-registry，PR #149 / Issue #148），每天 2:30（东八区）统一检查一次。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-09-1520-6c990129
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-08-09-1520-6c990129.md

---
# gh-tracker 技能

追踪 GitHub 仓库 PR / Issue 更新并通知的技能，支持自然语言增删查追踪目标。

## 命名与位置

| 阶段 | 名称 / 位置 |
|------|-------------|
| 原名 | `github-pr-issue-tracker` |
| 2026-08-09 起 | `gh-tracker`（`skills/gh-tracker/`） |
| 后续 | 迁至 `workspace-ops-deck/skills/`（与 clashman、cf-docker-registry、ob-man、openclaw-upgrade-check 同址） |

## 脚本

- `scripts/manage.sh` — 目标管理（自然语言解析后调用）
  - `list` — 列出所有追踪目标
  - `add --name <名> --repo <owner/repo> [--pr N] [--issue N]` — 添加（重复检测 / repo 格式校验 / 自动备份）
  - `remove --name <名>` — 删除（同时清理 state）
- `scripts/check_updates.sh` — 定时检查更新，无更新时 `NO_REPLY`

## 追踪目标（2026-08-09）

| 名称 | 仓库 | PR | Issue |
|------|------|----|-------|
| daily-stock-analysis | ZhuLinsen/daily_stock_analysis | #2154 | #2153 |
| trading-agents | TauricResearch/TradingAgents | #1205 | #1204 |
| serverless-registry | cloudflare/serverless-registry | #149 | #148 |

每天 02:30（东八区）统一检查一次，有更新私聊通知。

## 相关

- [[daily-stock-analysis-pr-issue-monitor]] — daily_stock_analysis 的监控任务
- [[clashman-skill]] — 同属 ops-deck 运维技能

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
