---
pageType: entity
id: entity.tool.claude-code
entityType: tool
name: "Claude Code"
sourceIds:
  - agent-bottleneck-zhihu
relationships:
  - targetId: concept.clean-world-dirty-world
    targetTitle: "Agent 干净世界 vs 脏世界"
    kind: representative-of
    weight: 1.0
---

# Claude Code

Anthropic 开发的 Coding Agent，是"干净世界" Agent 的典型代表。被文章引用为对比标杆——Claude Code 能做的事（自动写代码、reflection、工具调用），企业级 Agent 抄不动，因为两者的前提假设完全不同。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agent 干净世界 vs 脏世界](concepts/clean-world-dirty-world.md)
- [Enterprise Agent: Clean World vs Dirty World](syntheses/enterprise-agent-clean-world-vs-dirty-world.md)
- [Hermes Agent](entities/hermes-agent.md)
- [企业Agent五堵墙](concepts/five-walls-enterprise-agent.md)
- [企业Agent五层解法](concepts/five-layer-solution.md)
- [相对改进评估](concepts/relative-improvement-evaluation.md)
<!-- openclaw:wiki:related:end -->
