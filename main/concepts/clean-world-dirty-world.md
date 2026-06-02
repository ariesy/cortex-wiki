---
pageType: concept
id: concept.clean-world-dirty-world
title: "Agent 干净世界 vs 脏世界"
updatedAt: "2026-06-02"
sourceIds:
  - agent-bottleneck-zhihu
relationships:
  - targetId: concept.five-walls-enterprise-agent
    targetTitle: "企业Agent五堵墙"
    kind: problem-diagnosis
    weight: 1.0
  - targetId: concept.five-layer-solution
    targetTitle: "企业Agent五层解法"
    kind: solution-to
    weight: 1.0
  - targetId: concept.relative-improvement-evaluation
    targetTitle: "相对改进评估"
    kind: related-to
    weight: 0.7
---

# Agent 干净世界 vs 脏世界

"你学的Agent技术，和你实际做的Agent，根本不是一件事。"

## 干净世界 (Clean World)

Agent 博客、框架、论文描述的世界：
- **代表**：Claude Code、Hermes、OpenClaw、Cursor Agent
- **用户类型**：程序员 + 能像程序员一样操作环境的个人用户
- **核心特征**：任务所有者 = 任务执行者，即时验收、即时纠正、即时撤销
- **环境反馈**：清晰、结构化（编译器、测试用例、stderr）
- **错误成本**：几乎为零（git revert）
- **工作模式**：读 → 改 → 测 → 提交（线性）

## 脏世界 (Dirty World)

企业级 Agent 实际面对的世界：
- **数据**：扫描件、混乱文件名、版本矛盾、有格式但不严格的半结构化数据
- **反馈**：延迟的、模糊的、需要协商的（业务主管"下周给你回复"）
- **错误成本**：不可恢复（漏审违约金条款 = 实际损失）
- **工作模式**：需要图遍历而非线性处理
- **核心任务**：脏世界 → 干净世界的翻译

## 核心区别

| 维度 | 干净世界 | 脏世界 |
|------|----------|--------|
| 意图来源 | 自己的代码意图 | 业务方含糊的口头需求 |
| 目标状态 | 结构化、可验证、可回滚 | 脏数据上的具体动作 |
| 输入 | 清晰 | 模糊 |
| 反馈 | 实时 | 延迟 |
| 错误 | 可逆 | 不可逆、可追责 |

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Claude Code](entities/claude-code.md)
- [Enterprise Agent: Clean World vs Dirty World](syntheses/enterprise-agent-clean-world-vs-dirty-world.md)
- [Hermes Agent](entities/hermes-agent.md)
- [企业Agent五堵墙](concepts/five-walls-enterprise-agent.md)
- [企业Agent五层解法](concepts/five-layer-solution.md)
- [相对改进评估](concepts/relative-improvement-evaluation.md)
<!-- openclaw:wiki:related:end -->
