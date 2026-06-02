---
pageType: concept
id: concept.five-layer-solution
title: "企业Agent五层解法"
updatedAt: "2026-06-02"
sourceIds:
  - agent-bottleneck-zhihu
relationships:
  - targetId: concept.five-walls-enterprise-agent
    targetTitle: "企业Agent五堵墙"
    kind: solution-to
    weight: 1.0
  - targetId: concept.clean-world-dirty-world
    targetTitle: "Agent 干净世界 vs 脏世界"
    kind: solution-framework
    weight: 1.0
---

# 企业Agent五层解法

针对"五堵墙"的系统性工程解法，核心哲学：解法不在模型里，在 Agent 系统工程里。

## 第一层：脏数据预处理管道
让 LLM 远离原始数据。直接喂多模态 LLM 的三个问题：黑盒（出事无法回溯）、不可复现、数据不能沉淀。
- 文档解析（OCR + LLM 互补）
- 结构化索引（章节树 / 引用关系图谱）
- 分级存储（原文 / 摘要 / 索引）
- **80% 项目死在这层**，且这层跟 LLM 无关

## 第二层：混合解析
- 结构化字段（金额/日期/编号）→ 正则 + 解析器 → 100% 确定
- 模糊文本 → LLM，只给相关片段
- **核心原则**："LLM 是用来吸收不确定性的，不是用来制造不确定性的"

## 第三层：长上下文治理
分治策略：按主题/章节拆片 → 每片配引用上下文 → 顶层汇总
- Coding Agent 用线性 ReAct，企业 Agent 用**图遍历**

## 第四层：模糊逻辑规则化
- 离线将模糊条款翻译为 3-5 条具体化判断标准
- 标准可配置、可版本化、可追溯
- **核心原则**："让 LLM 做判断，不让 LLM 做定义"

## 第五层：用户预期管理
多级模式（快速/标准/深度），共用同一套底层管道，区别仅调度策略。
- **核心洞察**："你卖的不是 Agent，是确定性产品"

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agent 干净世界 vs 脏世界](concepts/clean-world-dirty-world.md)
- [Claude Code](entities/claude-code.md)
- [Enterprise Agent: Clean World vs Dirty World](syntheses/enterprise-agent-clean-world-vs-dirty-world.md)
- [Hermes Agent](entities/hermes-agent.md)
- [企业Agent五堵墙](concepts/five-walls-enterprise-agent.md)
- [相对改进评估](concepts/relative-improvement-evaluation.md)
<!-- openclaw:wiki:related:end -->
