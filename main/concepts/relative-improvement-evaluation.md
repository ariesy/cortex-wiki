---
pageType: concept
id: concept.relative-improvement-evaluation
title: "相对改进评估"
updatedAt: "2026-06-02"
sourceIds:
  - agent-bottleneck-zhihu
relationships:
  - targetId: concept.five-layer-solution
    targetTitle: "企业Agent五层解法"
    kind: evaluation-framework
    weight: 0.8
---

# 相对改进评估

企业 Agent 的评估哲学：不追求绝对准确，追求相对改进。

## 四条原则

1. **和基线比**：不需要 100% 准确，只需要比没有 Agent 的时候好
2. **量置信度**：好的 Agent 能诚实地说"我不知道"
3. **做盲测**：用人工审查过的历史案例做双盲对比
4. **监控漂移**：法规/业务规则/数据分布变化 → 能力漂移 → 持续评估

## 核心哲学

> "在脏世界里，相对改进就是一切。"

Coding Agent 有 SWE-Bench，企业 Agent 没有标准答案。承认这一点，才能做有意义的评估。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agent 干净世界 vs 脏世界](concepts/clean-world-dirty-world.md)
- [Claude Code](entities/claude-code.md)
- [Enterprise Agent: Clean World vs Dirty World](syntheses/enterprise-agent-clean-world-vs-dirty-world.md)
- [Hermes Agent](entities/hermes-agent.md)
- [企业Agent五堵墙](concepts/five-walls-enterprise-agent.md)
- [企业Agent五层解法](concepts/five-layer-solution.md)
<!-- openclaw:wiki:related:end -->
