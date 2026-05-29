---
pageType: entity
entityType: project
id: entity.project.superresearch
updatedAt: "2026-05-29"
claims:
  - id: claim.superresearch.process
    text: "强制5阶段Phase流程，HARD GATE确保设计先行"
    status: supported
    confidence: 0.8
    evidence:
      - kind: entity-summary
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-29-memory-sources
        weight: 0.9
---


# superresearch

> 强制Phase流程的深度研究框架，适用于投资研究、深度调研

**类型:** Skill  
**状态:** active  
**ID:** `skill_superresearch`  
**来源:** TOOLS.md

---


## 强制Phase流程

| Phase | 名称 | 说明 |
|-------|------|------|
| **Phase 1** | Brainstorming | 需求澄清、方案设计、**用户确认** |
| **Phase 2** | Writing Plans | 编写详细实现计划 |
| **Phase 3** | Subagent-Driven Development | TDD循环执行 |
| **Phase 4** | Systematic Debugging | Bug修复（如需要） |
| **Phase 5** | Finishing a Branch | 分支完成、PR |

---

## ⚠️ 强制约束

- **不跳过任何Phase** — 即使觉得简单也必须完成 brainstorming 和 planning
- **用户确认设计之前，不写任何代码**（HARD GATE）
- 问题/报错**立即报告**，不自行绕过

---

## 应用场景

- 投资研究（首选）
- 深度调研
- 任何需要系统化分析的任务

---

*来源: TOOLS.md superpowers技能说明*