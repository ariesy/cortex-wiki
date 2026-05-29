---
pageType: entity
entityType: project
id: entity.project.mmx-cli
updatedAt: "2026-05-29"
claims:
  - id: claim.mmx-cli.tool
    text: "MiniMax Token Plan额度查询命令行工具，5h/24h窗口差异"
    status: supported
    confidence: 0.8
    evidence:
      - kind: entity-summary
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-29-memory-sources
        weight: 0.9
relationships:
  - targetId: concept.minimax-quota-window
    targetTitle: "MiniMaxQuota窗口时间不一致"
    kind: documents
    weight: 0.8---


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