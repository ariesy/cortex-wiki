---
pageType: entity
id: entity.project.ima-scan
entityType: project
title: IMA 文件监控扫描系统
aliases:
  - IMA扫描
  - ima_api.cjs
  - IMA 笔记扫描
updatedAt: 2026-08-05T15:11:28.000Z
status: designing
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-06-1107-11346072.md
claims:
  - id: claim.ima-scan.tech-stack
    text: "IMA 文件监控扫描系统技术栈选定：Python + subprocess 调用 node ima_api.cjs（FunctionSpec 方案，已经 P0 验证可行），而非纯 Node.js 或 Shell 实现。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.85
  - id: claim.ima-scan.notify
    text: "通知策略默认 summary：仅在新文件时发送结果汇总，无变化不发通知（以减少通知噪音）；另有 full（含扫描开始通知）与 none 可选。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.gc
    text: "状态文件 GC 策略：扫描时自动清理超过 30 天的记录（每次扫描结束执行），不做独立 GC 脚本。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.error-handling
    text: "错误处理策略：单文件/笔记创建失败时重试一次，仍失败则记录错误并跳过，继续处理其他文件。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.subdir
    text: "子目录检测策略：仅处理监控目录的直接子目录（一层），忽略嵌套子目录，避免单篇笔记过大。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
---

# IMA 文件监控扫描系统

> 监控本地/IMA 目录，把文件变化整合为笔记的项目；按 superpowers 工作流推进（已过 brainstorming / PRD / FunctionSpec / 智者委员会评审 / P0 验证）。

## 关键设计决策（2026-05-06）

| 决策项 | 选定方案 |
|--------|----------|
| 技术栈 | **Python + subprocess 调用 node ima_api.cjs**（P0 已验证可行） |
| 通知策略 | **summary**（仅新文件时发结果汇总；可选 full / none） |
| 状态文件 GC | **扫描时自动清理 30 天前记录**（不做独立 GC 脚本） |
| 错误处理 | **重试一次，仍失败则跳过** |
| 子目录深度 | **仅一层**（忽略嵌套子目录） |

## 未决 / 待确认

- flock 相关的并发/加锁策略（正文预览截断处正在确认问题 6：flock）

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
