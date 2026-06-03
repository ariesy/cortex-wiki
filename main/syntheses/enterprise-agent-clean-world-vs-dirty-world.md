---
pageType: synthesis
id: synthesis.enterprise-agent-clean-world-vs-dirty-world
title: "Enterprise Agent: Clean World vs Dirty World"
sourceIds:
  - agent-bottleneck-zhihu
status: active
updatedAt: 2026-06-02T00:35:04.994Z
---

# Enterprise Agent: Clean World vs Dirty World

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# Enterprise Agent: Clean World vs Dirty World

## Overview

这篇知乎文章（2026-06-01）系统性地阐述了 **Agent 开发的两个世界** 这一核心矛盾。作者指出，当前所有前沿 Agent 框架（Claude Code、Hermes、OpenClaw、Cursor Agent）都是为"干净世界"设计的——任务所有者即执行者、环境反馈清晰、错误可回滚。而企业级 Agent 面临的是完全不同的"脏世界"：脏数据、半结构化诅咒、长上下文陷阱、业务逻辑模糊、矛盾需求。

## 核心框架

### 五堵墙（问题诊断）
1. **数据脏** — 扫描件/混乱文件名/版本矛盾
2. **半结构化诅咒** — 有格式但不严格，规则和 LLM 两头不靠
3. **长上下文伪命题** — 厂商标称 vs 实际有效推理窗口（8K-32K）
4. **业务逻辑模糊** — 法律必须留解释空间，规则本身不清晰
5. **矛盾需求** — 快/准/便宜/简单的不可能三角

### 五层解法（系统工程）
1. **脏数据预处理管道** — 让 LLM 远离原始数据，数据治理先行
2. **混合解析** — 确定字段归规则，模糊字段归 LLM
3. **长上下文治理** — 图遍历代替线性 ReAct
4. **模糊逻辑规则化** — 让 LLM 做判断，不让 LLM 做定义
5. **用户预期管理** — 把不可能三角变成多级服务模式

### 评估哲学
- 追求**相对改进**而非绝对准确
- 和基线比、量置信度、做盲测、监控漂移
- 承认企业 Agent 没有标准答案

## Key Insights

- 前 80% 的失败项目死在第一层（数据预处理），这一层跟 LLM 完全无关
- "信息差"是一种复合优势——作者把数据工程、业务工程、产品设计与 Harness 并列，远超主流 Agent 博客的视角
- 企业 Agent 的本质是**确定性产品**，用户付费的不是 AI 能力，是"知道交给你之后会发生什么"
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Agent 干净世界 vs 脏世界](concepts/clean-world-dirty-world.md)
- [Claude Code](entities/claude-code.md)
- [Hermes Agent](entities/hermes-agent.md)
- [企业Agent五堵墙](concepts/five-walls-enterprise-agent.md)
- [企业Agent五层解法](concepts/five-layer-solution.md)
- [相对改进评估](concepts/relative-improvement-evaluation.md)
<!-- openclaw:wiki:related:end -->
