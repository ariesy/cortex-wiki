---
pageType: entity
id: entity.bug.feishu-plugin-bundle-conflict
title: 飞书插件冲突：全局插件覆盖捆绑插件且版本更旧
entityType: bug
aliases:
  - 飞书插件版本冲突
  - bundled plugin conflict
  - feishu extension override
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.feishu-bundle-conflict.symptom
    text: "OpenClaw 更新后会报飞书插件冲突警告：全局插件 `~/.openclaw/extensions/feishu/`（版本 2026.3.13）覆盖了 OpenClaw 2026.4.2 内置的捆绑插件，但全局插件版本反而更旧，形成「新版被旧版遮蔽」。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-feishu-bundle-check-04250497
        weight: 0.9
  - id: claim.feishu-bundle-conflict.resolution
    text: "处理方式：删除全局插件让捆绑插件接管，即可用上 OpenClaw 内置的更新飞书支持。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-feishu-bundle-check-04250497
        weight: 0.9
  - id: claim.feishu-bundle-conflict.predelete-check
    text: "删除全局插件前必须检查其 `skills/` 目录——其中含 4 个飞书技能（feishu-doc, feishu-drive, feishu-perm 等），这些不会随捆绑插件自动回来，需单独迁移/备份。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-feishu-bundle-check-04250497
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-07-feishu-bundle-check-04250497.md

---
# 飞书插件冲突：全局插件覆盖捆绑插件且版本更旧

OpenClaw 升级后出现的插件遮蔽问题。

## 现象

升级后报飞书插件冲突警告：

| 插件 | 路径 | 版本 |
|------|------|------|
| 全局插件 | `~/.openclaw/extensions/feishu/` | 2026.3.13（**旧**） |
| 捆绑插件 | OpenClaw 2026.4.2 内置 | 更新 |

全局插件优先级更高 → 实际生效的是**更旧**的那份。

## 处理

删除全局插件，让捆绑插件接管。

## ⚠️ 删除前必查

`~/.openclaw/extensions/feishu/skills/` 下有 **4 个飞书技能**：

- `feishu-doc`
- `feishu-drive`
- `feishu-perm`
- （第 4 个）

这些**不会**随捆绑插件回来。删之前先备份/迁移，否则技能直接消失。

## 通用教训

任何「删除全局插件让内置接管」的操作，都要先枚举全局插件里夹带的 skills 和资源，再动手。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
