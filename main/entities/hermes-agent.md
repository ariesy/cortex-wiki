---
pageType: entity
id: entity.tool.hermes-agent
entityType: tool
name: "Hermes Agent"
sourceIds:
  - agent-bottleneck-zhihu
relationships:
  - targetId: concept.clean-world-dirty-world
    targetTitle: "Agent 干净世界 vs 脏世界"
    kind: representative-of
    weight: 0.9
---

# Hermes Agent

开源的自进化 Agent 框架，具备 skill discovery 能力。被文章用于论证"干净世界"假设——Hermes 的 skill discovery 依赖结构化 markdown，而企业 Agent 面对的行业规范是 PDF/扫描件/Word 嵌图，无法直接利用。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agent 干净世界 vs 脏世界](../concepts/clean-world-dirty-world.md)
- [Claude Code](claude-code.md)
- [Enterprise Agent: Clean World vs Dirty World](../syntheses/enterprise-agent-clean-world-vs-dirty-world.md)
- [企业Agent五堵墙](../concepts/five-walls-enterprise-agent.md)
- [企业Agent五层解法](../concepts/five-layer-solution.md)
- [相对改进评估](../concepts/relative-improvement-evaluation.md)
<!-- openclaw:wiki:related:end -->
