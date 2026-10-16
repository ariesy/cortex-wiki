---
pageType: entity
id: entity.bug.ima-scan-node-path-cron
entityType: bug
title: ima-sync cron 环境下 node 路径缺失导致上传静默失败
aliases:
  - ima-sync node PATH bug
  - ima_sync processed 误标记 bug
updatedAt: 2026-08-05T15:11:28.000Z
status: fixed
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-07-ima-sync-debug-fix-0a6e63bb.md
claims:
  - id: claim.ima-scan-bug.node-path
    text: "Bug 1（根因）：cron 默认 PATH 为 /usr/bin:/bin，找不到 node，subprocess.run(['node', ...]) 抛 FileNotFoundError 被 except OSError 吞掉，导致返回 success:false 但不给出错误信息。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.9
  - id: claim.ima-scan-bug.node-path-fix
    text: "Bug 1 修复：note_creator.py 中自动检测 _NODE_BIN 绝对路径（/home/linuxbrew/.linuxbrew/bin/node），使 cron 环境下也能找到 node。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.9
  - id: claim.ima-scan-bug.false-processed
    text: "Bug 2（严重）：子目录内不管文件上传是否成功都被标记为 processed，导致失败文件永不重试。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.9
  - id: claim.ima-scan-bug.false-processed-fix
    text: "Bug 2 修复：ima_sync.py 添加 dir_file_failures 计数器，仅当目录内所有文件都成功后才标记 processed；另手动从 state 清除了被误标记的 35 个目录记录。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.9
  - id: claim.ima-scan-bug.healthcheck-logging
    text: "优化：health check 失败日志现在会输出具体错误原因，不再静默。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.8
  - id: claim.ima-scan-bug.recovery
    text: "清理误标记记录后，妈妈/姚文海/朱琨 目录由后续 cron 自动重扫；朱琨 因文件量大先从配置中移除以避免限流。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb
        weight: 0.8
---

# ima-sync cron 环境下 node 路径缺失导致上传静默失败

> 影响 [IMA 文件监控扫描系统](ima-scan-system.md) 的一次生产事故与修复记录（2026-05-07）。

## 两个 Bug

| Bug | 根因 | 修复 |
|-----|------|------|
| Bug 1（根因） | cron 默认 PATH `/usr/bin:/bin` 找不到 `node`，`subprocess.run(['node', ...])` 抛 `FileNotFoundError`，被 `except OSError` 吞掉 → 返回 `success: false` 但不给错误信息 | `note_creator.py` 自动检测 `_NODE_BIN` 绝对路径（`/home/linuxbrew/.linuxbrew/bin/node`） |
| Bug 2（严重） | 子目录内不管文件上传是否成功都标记 `processed` → 失败文件永不重试 | `ima_sync.py` 增加 `dir_file_failures` 计数器，仅目录内全部成功才标记 `processed` |

## 修复后处置

- 手动从 state 清除被误标记的 **35 个目录**记录（妈妈 / 姚文海 / 朱琨）。
- `朱琨` 因文件量大先从扫描配置中移除，避免再次触发限流。
- health check 失败日志改为输出具体错误原因。

## 验证结果

| 目录 | 结果 |
|------|------|
| 朱凌霄 | 21 子目录 + 2 根文件全部成功，两次扫描 35 + 129 = 164 个文件 0 失败 |
| 爸爸 | 1 子目录全部上传成功 |
| 妈妈 / 姚文海 / 朱琨 | state 已清空，后续 cron 自动重扫 |

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
