---
pageType: entity
id: entity.archify
title: archify
entityType: tool
aliases:
  - archify
  - tt-a1i/archify
sourceIds:
  - sources/github-archify-readme-20260829.md
updatedAt: 2026-08-29T00:20:00.000Z
tags:
  - agent-skill
  - 图表
  - 文档自动化
  - diagram
confidence: high
relationships:
  - targetId: entity.awesome-gpt-image-2
    targetTitle: "awesome-gpt-image-2"
    kind: same-cohort
    weight: 0.6
  - targetId: entity.superresearch
    targetTitle: "superresearch"
    kind: complementary
    weight: 0.4
---

# archify

**让 agent 产出的架构图可被校验、可追溯、可评审 —— 而不是画一张好看但编造的图。**

GitHub: [tt-a1i/archify](https://github.com/tt-a1i/archify)
语言：JavaScript / Node.js · License：MIT · 版本 v2.16.0-dev.0
实测（2026-08-29）：★ 27,333 / forks 1,735 · 建库 2026-04-15

## 它解决什么真问题

agent 画架构图的老毛病是**幻觉拓扑**——图很漂亮，连线和代码实际对不上，人看了还以为是真的。Archify 的解法不是"让模型画得更准"，而是**在架构上剥夺模型直接画图的权利**：

> agent 产出 typed JSON IR → Archify 确定性编译成 HTML/SVG

模型只输出结构化中间表示，渲染是确定性的、可校验的。这一步把"生成质量"问题转成了"编译正确性"问题，是这批 skill 里**工程质量最高的一处设计**。

## 能力清单

| 维度 | 内容 |
|------|------|
| 图类型 | 5 种（架构 / workflow / 时序 / 数据流 / lifecycle） |
| 预设与主题 | 4 套预设、dark/light、内置品牌标记、finite motion |
| 导出 | 自包含单文件 HTML + PNG / SVG / WebM / 1200×630 分享卡片 |
| 接入 | Cursor、Claude Code、Codex CLI、OpenCode |
| 安装 | `npx skills add tt-a1i/archify -g` |

## 两个被低估的特性

**1. 变更前评审（Before / Delta / After）**
对比两个已校验快照，给出精确的 `added / removed / changed / moved / rerouted` 事实。这把架构图从"文档"升级成了**可 diff 的工件**——架构评审终于有了和 code review 同等的语义。

**2. grounded 交互（不虚构拓扑）**
搜索节点、打开 revision-verified 源码、追踪上下游 authored reach 与精确路由、比较角色、播放 guided stories。核心约束是 **without inventing topology**——交互层也不允许凭空生成。

## 判断

- **值得装。** 这是本周四个仓库里我唯一认为可以**直接进工作流**的。主人日常有 wiki / 研究报告 / 系统说明的输出需求，架构图可 diff + 可追溯源码这两点直接命中"文档自动化最痛的一环"。
- **成熟度风险低但存在**：版本仍是 `2.16.0-dev.0`（dev 后缀），活跃开发中，IR schema 可能变动。
- **锁定风险小**：MIT 许可，输出是自包含 HTML，不依赖其服务。
- 与其余三个相比，Archify 是**生产力工具**，不是内容库或平台赌注。

## 观察点

- dev → stable 的节奏，以及 IR schema 是否稳定
- 已有商业赞助（APINEBULA 提供多模型统一 API、EverMind 的 Raven harness 内置支持）——社区动能真实，但需注意 README 里带推广码的赞助位是**软性变现**，不影响工具中立性

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
