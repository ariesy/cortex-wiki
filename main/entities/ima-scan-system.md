---
pageType: entity
id: entity.project.ima-scan
entityType: project
title: IMA 文件监控扫描系统
aliases:
  - IMA扫描
  - ima_api.cjs
  - IMA 笔记扫描
updatedAt: 2026-10-16T13:18:51.436Z
status: designing
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-06-1107-11346072.md
  - source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
  - source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
claims:
  - id: claim.ima-scan.tech-stack
    text: IMA 文件监控扫描系统技术栈选定：Python + subprocess 调用 node ima_api.cjs（FunctionSpec
      方案，已经 P0 验证可行），而非纯 Node.js 或 Shell 实现。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.85
  - id: claim.ima-scan.notify
    text: 通知策略默认 summary：仅在新文件时发送结果汇总，无变化不发通知（以减少通知噪音）；另有 full（含扫描开始通知）与 none 可选。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.gc
    text: 状态文件 GC 策略：扫描时自动清理超过 30 天的记录（每次扫描结束执行），不做独立 GC 脚本。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.error-handling
    text: 错误处理策略：单文件/笔记创建失败时重试一次，仍失败则记录错误并跳过，继续处理其他文件。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.subdir
    text: 子目录检测策略：仅处理监控目录的直接子目录（一层），忽略嵌套子目录，避免单篇笔记过大。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-1107-11346072
        weight: 0.8
  - id: claim.ima-scan.processed-gate
    text: 已修复缺陷：子目录必须等目录内所有文件都上传成功后才标记 processed（dir_file_failures 计数器），避免失败文件永不重试。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.9
  - id: claim.ima-scan.node-bin-abs
    text: 已修复缺陷：note_creator.py 自动检测 _NODE_BIN
      绝对路径（/home/linuxbrew/.linuxbrew/bin/node），使 cron 默认 PATH /usr/bin:/bin
      下也能调用 node。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.9
  - id: claim.ima-scan.kb-title-file-name
    text: IMA 知识库条目标题来自 create_media 的 file_name（而非 add_knowledge 的
      title），因此按「文件夹名_序号.扩展名」命名 file_name 才能得到自定义标题。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.9
  - id: claim.ima-scan.dir-note-rule
    text: 目录笔记创建条件为「有图片或非图片文件」即创建（if non_image_files or
      image_files），纯图片目录也会生成含媒体索引表的笔记。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.9
  - id: claim.ima-scan.pdf-same-as-image
    text: PDF 文件后续同样直接上传知识库并按「文件夹名 + 序号」命名，与图片处理方式一致。
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.75
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
### Sources

- [Memory Bridge (main): 2026-05-07-ima-sync-debug-fix](../sources/bridge-workspace-142ea9a2-memory-2026-05-07-ima-sync-debug-fix-0a6e63bb.md)
- [Memory Bridge (main): 2026-05-07-pdf-knowledge-base-fix](../sources/bridge-workspace-142ea9a2-memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4.md)

### Referenced By

- [IMA 知识库标题使用 create_media.file_name 而非 add_knowledge.title](ima-kb-title-file-name-bug.md)
- [ima-sync cron 环境下 node 路径缺失导致上传静默失败](ima-sync-cron-node-path-bug.md)
<!-- openclaw:wiki:related:end -->
