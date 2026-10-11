---
pageType: entity
id: entity.tool.deepseek-tui
title: DeepSeek-TUI
entityType: tool
aliases:
  - deepseek-tui
  - DeepSeek TUI
updatedAt: 2026-08-05T15:11:28.000Z
status: active
claims:
  - id: claim.deepseek-tui.positioning
    text: "DeepSeek-TUI 是终端原生的 AI 编程助手，专为 DeepSeek V4 系列模型打造，从协议层到工具层深度适配；MIT 开源，作者 Hayden Brown，2026-05-01 上线 24h 获 +580 stars。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-deepseek-tui-research-2b6758be
        weight: 0.8
  - id: claim.deepseek-tui.features
    text: "DeepSeek-TUI 核心特点：基于 ratatui 的纯终端键盘操作 TUI（无需 IDE）、1M token 上下文（DeepSeek V4 百万级窗口 + prefix cache）、原生思维流实时展示 chain-of-thought、架构为 dispatcher → TUI → engine → tools，工具注册支持 shell/文件/git/网页搜索/子 agent/MCP。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-deepseek-tui-research-2b6758be
        weight: 0.8
  - id: claim.deepseek-tui.install
    text: "DeepSeek-TUI 发布为 Rust 二进制（<5MB，不需要 Node/Python 运行时），也有 npm 包；安装：npm i -g deepseek-tui（或 crates.io / AUR），本地启动：deepseek serve --http。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-deepseek-tui-research-2b6758be
        weight: 0.8
  - id: claim.deepseek-tui.tradeoffs
    text: "DeepSeek-TUI 优势在高频小改动、局部重构、文档生成，成本约为 Claude Sonnet 4.6 的 1/20；弱项是跨文件大规模重构（配置间接层容易漏）、全新架构设计，以及已合规落地 Anthropic 企业版的场景。与 Claude Code Max 是互补而非替代关系。"
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-deepseek-tui-research-2b6758be
        weight: 0.75
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-06-deepseek-tui-research-2b6758be.md
---
# DeepSeek-TUI

终端原生的 AI 编程助手，专为 **DeepSeek V4** 系列模型打造 —— 不是简单的 API 封装，而是从协议层到工具层都深度适配 DeepSeek。仓库：github.com/Hmbown/DeepSeek-TUI

## 核心特点

- **纯终端驱动**：基于 ratatui 的键盘操作 TUI，不需要 IDE
- **1M token 上下文**：利用 DeepSeek V4 的百万级上下文窗口 + prefix cache
- **原生思维流**：实时展示模型的 chain-of-thought 推理过程
- **架构**：`dispatcher → TUI → engine → tools`，工具注册支持 shell / 文件 / git / 网页搜索 / 子 agent / MCP
- **发布形式**：Rust 二进制（<5MB，不需要 Node/Python 运行时），也有 npm 包
- **MIT 开源**，作者 Hayden Brown，2026-05-01 上线 24h 获得 +580 stars（后一周达 8,701 星）

## 安装

```bash
npm i -g deepseek-tui   # 或 crates.io / AUR
deepseek serve --http   # 本地启动
```

## 优势场景

- 高频小改动、局部重构、文档生成
- 成本：DeepSeek V4 ≈ Claude Sonnet 4.6 的 1/20 价格
- 印度/东南亚/中东团队成本差可达 3-5 倍

## 弱项

- 跨文件大规模重构（涉及配置间接层容易漏）
- 全新架构设计（需要大量设计决策时不如 Claude）
- 已合规落地 Anthropic 企业版的场景

## 定位

和 Claude Code Max 是**互补关系，不是替代**。官方建议两者配合使用。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
