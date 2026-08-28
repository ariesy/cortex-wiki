---
pageType: entity
id: entity.concept.skills-dual-directory-discovery
title: workspace skills 与 external skills 双目录发现机制
entityType: concept
aliases:
  - skill symlink 被阻止
  - external skills 目录
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.skills-dual-directory.independent
    text: "OpenClaw 中 `~/.openclaw/workspace/skills/`（workspace skills）与 `~/.openclaw/skills/`（external skills）是两套独立的发现系统，各自维护自己的技能列表，不共享。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-30-skill-sync-4f642b06
        weight: 0.9
  - id: claim.skills-dual-directory.symlink-blocked
    text: "用 symlink 打通两个 skills 目录的方案会被安全机制阻止，不可用。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-30-skill-sync-4f642b06
        weight: 0.9
  - id: claim.skills-dual-directory.copy-solution
    text: "可行方案是把 skill 复制到 external 目录（`~/.openclaw/skills/<name>/`，subagent 可访问），workspace 原版保持不变（main session 使用）。代价是两份副本需要手动同步。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-30-skill-sync-4f642b06
        weight: 0.9
  - id: claim.skills-dual-directory.subagent-visibility
    text: "subagent 只能发现 external skills 目录下的技能，这是「subagent 报找不到某个 skill」类故障的首要排查点。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-30-skill-sync-4f642b06
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-03-30-skill-sync-4f642b06.md

---
# workspace skills 与 external skills 双目录发现机制

一个会反复踩的部署陷阱：技能改好了，但调用方根本看不见。

## 两套目录

| 目录 | 谁在用 | 说明 |
|------|--------|------|
| `~/.openclaw/workspace/skills/` | main session | workspace skills |
| `~/.openclaw/skills/` | subagent | external skills |

两者**独立发现、不共享**。

## symlink 方案不可行

用软链接让一个目录指向另一个会被安全机制阻止。

## 正确做法

复制到 external 目录，两边各自保留一份完整 skill：

```
~/.openclaw/skills/<name>/          # subagent 用
~/.openclaw/workspace/skills/<name>/ # main session 用
```

**代价**：改了 workspace 版之后必须手动同步到 external 版，否则两边行为漂移。

## 排障

subagent 报「找不到 skill X」→ 先检查 `~/.openclaw/skills/X/` 是否存在，而不是去改 skill 本身。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [DeerFlow与OpenClaw集成分析](deerflow-integration.md)
<!-- openclaw:wiki:related:end -->
