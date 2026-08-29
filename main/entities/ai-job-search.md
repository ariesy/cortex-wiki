---
pageType: entity
id: entity.ai-job-search
title: ai-job-search
entityType: tool
aliases:
  - ai-job-search
  - MadsLorentzen/ai-job-search
sourceIds:
  - sources/github-ai-job-search-readme-20260829.md
updatedAt: 2026-08-29T00:20:00.000Z
tags:
  - agent-skill
  - 求职
  - Claude-Code
  - 工作流
confidence: medium-high
relationships:
  - targetId: entity.archify
    targetTitle: "archify"
    kind: same-cohort
    weight: 0.5
  - targetId: entity.openhuman
    targetTitle: "openhuman"
    kind: same-cohort
    weight: 0.4
---

# ai-job-search

**把 Claude Code 变成全套求职助理，跑在你自己机器上：数据不出本地，"fork 即拥有"。**

GitHub: [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)
语言：Python · License：MIT
实测（2026-08-29）：★ 37,723 / forks **12,766** · 建库 2026-03-18

## 工作流

```
/setup            /scrape              /apply <url>
  |                  |                     |
  v                  v                     v
填画像           多门户搜索            匹配度打分
  |              去重 + fit 排序           |
  v                  v                     v
画像文件就绪     挑一个匹配         起草 LaTeX 简历 + 求职信
                                          |
                                          v
                                   Reviewer agent 批评
                                    -> 修订 -> 终稿
```

- **`/setup`** —— 三条路径：读 `documents/`（CV PDF、LinkedIn 导出、学历、推荐信、历史申请）、粘贴单份 CV、或访谈式问答。自动检测已有材料，**documents 模式幂等**，可随补料反复重跑。
- **`/scrape`** —— 多门户搜索、去重、按 fit 排序
- **`/apply <url>`** —— 评估打分 → 起草量身定制的 LaTeX 简历与求职信 → **reviewer agent 批评** → 修订 → 终稿

## 设计要点

- **核心流水线与语言、国家无关**（自我画像 / 匹配评估 / drafter-reviewer）
- **门户层绑定丹麦市场**：Jobindex、Jobnet、Akademikernes Jobbank 等，但模式设计为可替换本地招聘站
- 编码了职业指导最佳实践：结构化评估标准、**前瞻性**求职信框架、可选薪资对标
- **drafter-reviewer 双 agent 结构**是关键——生成者不自我审查，由独立的 reviewer 批评后再修订

## 关于「fork/star 比 33.8%」

实测 fork/star ≈ **33.8%**，显著高于同批对照（archify 6.4%、awesome-gpt-image-2 9.9%、openhuman 9.8%）。

主人原推断是"大家真在用而不是在收藏"。这个推断**方向合理，但需要打折**：

- 支持证据：fork 绝对值 1.27 万量级；框架确实要求 fork 后填自己的 `documents/` 才能跑
- 反证：README 明写 **"Fork it and own it"** —— 产品主张本身就在鼓励 fork，这会推高**仪式性 fork**（先 fork 囤着、未必真跑）
- 结论：高 fork 比证明**意图强烈**，不等于**使用深度已验证**。真正的验证指标应该是 fork 后的 commit 活跃度与 issue 质量，尚未查证。

## 判断

- **方法论值得借鉴，本体对主人价值有限。** 主人不在求职市场，但 **drafter-reviewer 双 agent 流水线**和**幂等 profile 构建**是两个可直接迁移到投资研究流水线的模式（例如：起草研报 → 独立 critic agent 挑刺 → 修订）。
- **地域限制是硬伤**：默认门户全丹麦，换中文/国内招聘站需要自己写 skill，工作量不小。
- MIT 许可，无锁定风险。

## 观察点

- 是否出现非丹麦市场的社区 fork（决定它能否从区域工具长成通用框架）
- fork 后的实际 commit 活跃度（验证"真在用"假设）

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
