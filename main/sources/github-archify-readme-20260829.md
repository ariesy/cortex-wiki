---
pageType: source
id: source.github.archify-readme-20260829
title: "tt-a1i/archify README 摘录与核实（2026-08-29）"
sourceType: github-readme
url: https://github.com/tt-a1i/archify
rawUrl: https://raw.githubusercontent.com/tt-a1i/archify/main/README.md
status: active
capturedAt: 2026-08-29T00:20:00.000Z
updatedAt: 2026-08-29T00:20:00.000Z
confidence: high
---

# tt-a1i/archify README 摘录

> 本人摘取的事实点，非原文全量复制。用于支撑 `entity.archify` 的论断。

## 定位（原文）

"Turn a codebase or system description into a polished, interactive system map — directly in chat."
"Archify is a Node.js rendering and validation system for Cursor, Claude Code, Codex CLI, and OpenCode. Agents produce typed JSON IR; Archify deterministically compiles it into HTML/SVG."

## 关键事实

- 技术形态：Node.js 渲染 + 校验系统；agent 产出 **typed JSON IR**，Archify **确定性**编译为 HTML/SVG。这是"agent 不直接画图、只产出可被校验的中间表示"的分层设计。
- 支持的 agent/IDE：Cursor、Claude Code、Codex CLI、OpenCode
- 5 种图类型；4 套预设；dark/light 主题；内置品牌标记；有限动效（finite motion）
- 变更评审：对比两个已校验快照，输出 Before / Delta / After，给出精确的 added / removed / changed / moved / rerouted 事实
- 交互可追溯（grounded）：搜索节点、可选打开 revision-verified 源码、追踪上下游 authored reach 与精确路由、比较角色、播放 guided stories，且**不虚构拓扑**
- 导出：自包含单文件 HTML + PNG / SVG / WebM / 1200×630 分享卡片
- 安装：`npx skills add tt-a1i/archify -g`
- 提示语：`Use archify to map this repository's runtime architecture.`
- 版本：v2.16.0-dev.0（MIT）

## API 实测数据（2026-08-29）

- stars 27,333 / forks 1,735 / 语言 JavaScript / License MIT
- 建库 2026-04-15，最后 push 2026-08-28

## 商业化迹象

- 有赞助位（APINEBULA 提供 Claude/GPT/Gemini 统一 API，带 10% off 推广码；EverMind 的 Raven harness 支持 Archify 作为 Skill）
- 有独立项目页 / 场景指南 / Proof Lab 画廊

## 注

主人转述的"单周 +8,530 ⭐"为趋势榜数据，本页未独立复核周增量，只复核了总量。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
