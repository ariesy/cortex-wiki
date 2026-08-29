---
pageType: source
id: source.github.ai-job-search-readme-20260829
title: "MadsLorentzen/ai-job-search README 摘录与核实（2026-08-29）"
sourceType: github-readme
url: https://github.com/MadsLorentzen/ai-job-search
rawUrl: https://raw.githubusercontent.com/MadsLorentzen/ai-job-search/master/README.md
status: active
capturedAt: 2026-08-29T00:20:00.000Z
updatedAt: 2026-08-29T00:20:00.000Z
confidence: high
---

# MadsLorentzen/ai-job-search README 摘录

> 本人摘取的事实点，非原文全量复制。用于支撑 `entity.ai-job-search` 的论断。

## 定位（原文）

"The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it."

## 核心工作流

```
/setup          /scrape              /apply <url>
  |                |                     |
  v                v                     v
Fill in        Search job           Evaluate fit
your profile   portals              Score & recommend
  |                |                     |
  v                v                     v
Profile        Present matches      Draft CV + Cover Letter
files ready    with fit ratings     (LaTeX, tailored)
                   |                     |
                   v                     v
               Pick a match         Reviewer agent critiques
               -> /apply            -> Revise -> Final output
```

- `/setup` — 三条路径：读 `documents/` 目录（CV PDF、LinkedIn 导出、学历、推荐信、历史申请）、粘贴单份 CV、或走访谈式问答。自动检测已有材料；documents 模式**幂等**，可反复重跑。
- `/scrape` — 多门户搜索、去重、按 fit 排序展示；可直接挑一个跑 `/apply`
- `/apply <url>` — 评估匹配度打分 → 起草 LaTeX 简历与求职信 → **reviewer agent 批评** → 修订 → 输出终稿

## 关键设计

- 核心工作流（自我画像、匹配评估、drafter-reviewer 申请流水线）**语言与国家无关**
- 求职门户搜索 skill 面向**丹麦市场**（Jobindex、Jobnet、Akademikernes Jobbank 等），但模式设计为可替换成本地招聘站
- 编码了职业指导最佳实践：结构化评估标准、**前瞻性**（forward-looking）求职信框架、可选薪资对标
- README 明确讨论"它真的工作吗？"（Does it actually work?）章节
- 支持扩展：门户、模板、评估标准；鼓励从其他 fork 借鉴
- License：MIT

## API 实测数据（2026-08-29）

- stars 37,723 / forks **12,766** / 语言 Python / License MIT
- 建库 2026-03-18，最后 push 2026-08-27
- fork/star 比 ≈ **33.8%** —— 异常高（对比 archify 6.4%、awesome-gpt-image-2 9.9%、openhuman 9.8%）

## 注

主人转述"单周 +4,706 ⭐、fork 高达 1.27 万"——fork 数与实测 12,766 吻合。
「fork/收藏比高说明大家真在用」是一个**合理但需谨慎**的推断：高 fork 也可能来自"fork 即拥有"的产品主张（README 明写 "Fork it and own it"）驱动的仪式性 fork，尚未验证实际使用强度。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
