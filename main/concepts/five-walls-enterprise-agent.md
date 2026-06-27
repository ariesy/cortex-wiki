---
pageType: concept
id: concept.five-walls-enterprise-agent
title: "企业Agent五堵墙"
updatedAt: "2026-06-02"
sourceIds:
  - agent-bottleneck-zhihu
relationships:
  - targetId: concept.clean-world-dirty-world
    targetTitle: "Agent 干净世界 vs 脏世界"
    kind: detailed-diagnosis
    weight: 1.0
  - targetId: concept.five-layer-solution
    targetTitle: "企业Agent五层解法"
    kind: problem-solution
    weight: 1.0
---

# 企业Agent五堵墙

企业 Agent 开发同时撞上的五重障碍，来源为知乎文章《Agent目前最大的瓶颈是什么？》。

## 第一堵墙：数据是脏的
30% 扫描件、15% Word 嵌截图扫描件、5% 截图再被截图。文件名矛盾，"最终版"有 4 个，v2 比 v3 还新。光确定有效版本就要半个月数据治理。

## 第二堵墙：半结构化数据
完全结构化 → SQL Agent；完全非结构化 → LLM 处理。最难的是中间层——有格式但格式不严格，有结构但结构会破（合并单元格、编号异常）。正则解不动，LLM 看不全。

## 第三堵墙：长上下文是伪命题
厂商标称 100 万 token，实际复杂推理有效窗口仅 8K-32K。找事实（needle-in-a-haystack）和推理多事实关系是两种完全不同任务。企业文档互相引用但没有编译器，不能用线性 ReAct。

## 第四堵墙：业务逻辑本身模糊
"合理期限"、"明显"、"必要时"——法律条文必须留解释空间。Agent 不能假装规则清晰。

## 第五堵墙：用户既要又要还要
准、快、便宜、简单——四个矛盾需求间找路。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agent 干净世界 vs 脏世界](clean-world-dirty-world.md)
- [Claude Code](../entities/claude-code.md)
- [Enterprise Agent: Clean World vs Dirty World](../syntheses/enterprise-agent-clean-world-vs-dirty-world.md)
- [Hermes Agent](../entities/hermes-agent.md)
- [企业Agent五层解法](five-layer-solution.md)
- [相对改进评估](relative-improvement-evaluation.md)
<!-- openclaw:wiki:related:end -->
