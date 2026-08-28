---
pageType: entity
id: entity.bug.minimax-anthropic-streaming
title: MiniMax Anthropic-compatible streaming 泄漏思维链
entityType: bug
aliases:
  - MiniMax anthropic-messages 流式不兼容
  - MiniMax reasoning_content 泄漏
updatedAt: 2026-08-28T16:05:00.000Z
status: identified
claims:
  - id: claim.minimax-streaming.root-cause
    text: "MiniMax 的 Anthropic-compatible streaming 端点用 OpenAI 风格 delta chunk 输出 `reasoning_content`，而不是原生 Anthropic thinking blocks；与 OpenClaw 的 Anthropic 流式显示逻辑不完全兼容，会隐式启用并把内部推理泄漏到可见输出中。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-minimax-api-switch-7099cdab
        weight: 0.9
  - id: claim.minimax-streaming.config-trigger
    text: "触发条件是配置走 `anthropic-messages`：minimax-cn / minimax-portal 的 `baseUrl` 指向 `https://api.minimaxi.com/anthropic` 且 `api: \"anthropic-messages\"`。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-minimax-api-switch-7099cdab
        weight: 0.85
  - id: claim.minimax-streaming.fix
    text: "推荐修复：把 MiniMax 配置切到 OpenAI-compatible——`baseUrl: \"https://api.minimaxi.com/v1\"`、`api: \"openai-completions\"`、`authHeader: true`，写在 `~/.openclaw/openclaw.json` 中；改前先 `cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak`。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-minimax-api-switch-7099cdab
        weight: 0.8
  - id: claim.minimax-streaming.isolation
    text: "排障隔离方法：临时 `/model deepseek/deepseek-v4-flash` 等其他模型，若 streaming 正常即可确认是 MiniMax 特有问题；另可对比 Hermes Agent 使用的 MiniMax API 格式是否有差异。"
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-minimax-api-switch-7099cdab
        weight: 0.75
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-30-minimax-api-switch-7099cdab.md
relationships:
  - targetId: entity.bug.minimax-oauth
    targetTitle: "MiniMax国内OAuth配置问题"
    kind: related-to
    weight: 0.5

---
# MiniMax Anthropic-compatible streaming 泄漏思维链

OpenClaw 中把 MiniMax 配成 `anthropic-messages` 时，模型的内部推理会作为可见输出泄漏出来。

## 根因

> MiniMax's streaming endpoint emits `reasoning_content` in OpenAI-style delta chunks instead of native Anthropic thinking blocks, which can leak internal reasoning into visible output if left enabled implicitly.

即：MiniMax 只做到了「形似 Anthropic」，流式字段名/结构沿用 OpenAI 习惯，OpenClaw 的 Anthropic 流式解析路径识别不了 thinking block，于是把推理内容当正文渲染。

## 触发配置

```jsonc
"minimax-cn": {
  "baseUrl": "https://api.minimaxi.com/anthropic",
  "api": "anthropic-messages"   // ← 问题来源
}
```

## 修复

```bash
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak
```

```jsonc
"minimax-portal": {
  "baseUrl": "https://api.minimaxi.com/v1",   // 去掉 /anthropic
  "api": "openai-completions",                 // 改 openai-completions
  "authHeader": true
}
```

## 排查顺序

1. 换模型（如 `deepseek/deepseek-v4-flash`）确认是否 MiniMax 特有
2. 确认配置走的是 `/anthropic` + `anthropic-messages`
3. 对照 Hermes Agent 的 MiniMax API 格式
4. 切 OpenAI-compatible 端点验证

## 教训

国内厂商的「Anthropic 兼容」端点往往是**协议形似而非语义等价**，接入前应先验证流式字段；遇到流式输出异常时，优先怀疑兼容层而不是模型本身。

## Related
- [MiniMax国内OAuth配置问题](minimax-oauth.md)

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
