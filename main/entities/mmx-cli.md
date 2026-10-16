---
pageType: entity
entityType: project
id: entity.project.mmx-cli
updatedAt: 2026-10-16T13:17:17.660Z
claims:
  - id: claim.mmx-cli.tool
    text: MiniMax Token Plan额度查询命令行工具，5h/24h窗口差异
    status: supported
    confidence: 0.8
    evidence:
      - kind: entity-summary
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-29-memory-sources
        weight: 0.9
  - id: claim.mmx-cli.use-script
    text: 查询 mmx 额度必须走 mmx 技能的脚本（quota.sh），直接跑原始命令不会按指定格式返回 5 小时用量与多媒体模型用量信息。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-mmx-quota-script-fix-49acac04
        weight: 0.85
  - id: claim.mmx-cli.quota-panel
    text: MiniMax Token Plan 额度面板结构：M2.7 文本模型 5h 窗口上限 600（03:00 后刷新）、周额度 6000（周六
      23:59 重置）；Coding Plan VLM 与搜索 5h 上限 60；音乐生成 v2.6 / 音乐封面 / 歌词生成 5h 上限
      100、周额度 700（12:00 刷新）；语音/视频/图片无限制。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-mmx-quota-script-fix-49acac04
        weight: 0.8
  - id: claim.mmx-cli.tools-md-no-entry
    text: TOOLS.md 中没有 mmx 的单独条目，该技能走 workspace skill 的 SKILL.md。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-mmx-quota-script-fix-49acac04
        weight: 0.8
relationships:
  - targetId: concept.minimax-quota-window
    targetTitle: MiniMaxQuota窗口时间不一致
    kind: documents
    weight: 0.8
sourceIds:
  - memory/2026-04-29-mmx-quota-windows.md
  - source.bridge.workspace-142ea9a2.memory-2026-05-07-mmx-quota-script-fix-49acac04
---

# mmx-cli

> entity_type: skill

**类型:** Project/Skill  
**ID:** `skill_mmx_cli`  
**位置:** `~/.agents/skills/mmx-cli`  
**来源:** mmx quota bug修复

---


## 基本信息

| 项目 | 内容 |
|------|------|
| **名称** | mmx-cli |
| **位置** | `~/.agents/skills/mmx-cli` |
| **用途** | MiniMax Token Plan命令行工具 |

---

## 功能

| 命令 | 说明 |
|------|------|
| `mmx quota` | 查询各模型额度使用情况 |

---

## 窗口时间说明

| 模型类型 | 窗口时间 |
|----------|----------|
| 文本/编码模型 | **5小时**窗口 |
| 媒体生成模型 | **24小时**窗口 |

API对不同模型返回不同时间窗口（文本5h/媒体24h），脚本直接透传。

---

## 相关Pattern

- `pattern_minimax_quota_window` — MiniMaxQuota窗口时间不一致

---

*来源: memory/2026-04-29-mmx-quota-windows.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-05-07-mmx-quota-script-fix](../sources/bridge-workspace-142ea9a2-memory-2026-05-07-mmx-quota-script-fix-49acac04.md)
<!-- openclaw:wiki:related:end -->
