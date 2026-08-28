---
pageType: entity
id: entity.tool.semantic-router
title: semantic-router 技能（框架版，缺运行时实现）
entityType: tool
aliases:
  - semantic-router
  - halfmoon82/semantic-router
  - 语义路由
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.semantic-router.framework-only
    text: "从 ClawHub 安装的 semantic-router（halfmoon82/semantic-router）是'框架版'技能，缺少实际的 OpenClaw 插件代码。其 clawhub.yaml 的 description 明确写着 'Framework-only update. Runtime implementation has been removed from the published artifact.'，即运行时实现已从发布版本中移除。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-semantic-router-d8d36d40
        weight: 0.85
  - id: claim.semantic-router.doc-vs-reality
    text: "semantic-router 的文档描述与实际情况不符：文档称'通过 before_prompt_build hook 注入 prependContext'，实际没有实现该 hook 的插件代码；文档称'OpenClaw Gateway → POST /route → webhook server'，实际没有配置 webhook 调用、也不会自动调用 semantic_check.py。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-semantic-router-d8d36d40
        weight: 0.8
  - id: claim.semantic-router.skillmd-not-mandatory
    text: "SKILL.md 与 prependContext 是两个独立的东西：SKILL.md 是技能作者写好的说明书，OpenClaw 把其内容注入 agent 提示词后，由 agent 自己决定是否执行；prependContext 是 OpenClaw 系统注入的上下文。SKILL.md 中声明 hook 并不能让 prependContext 生效。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-semantic-router-d8d36d40
        weight: 0.85
  - id: claim.semantic-router.agentsmd-workaround
    text: "让 semantic-router 在所有 session 生效的可行办法是在 AGENTS.md 中写明强制指令（每次收到用户消息必须调用 semantic_check.py 分析、按返回 pool 切换模型池、在响应第一行输出路由声明），而不是依赖 SKILL.md。"
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-semantic-router-d8d36d40
        weight: 0.75
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-29-semantic-router-d8d36d40.md

---
# semantic-router 技能

来源：`halfmoon82/semantic-router`（ClawHub）。目标是按消息语义路由到不同模型池。

## ⚠️ 核心问题：文档与实现脱节

这是一个**框架版**技能，没有运行时实现。clawhub.yaml 里写得很直白：

```
description: |
  Framework-only update. Runtime implementation has been removed from the published artifact.
```

| 文档描述 | 实际情况 |
|---------|---------|
| 通过 `before_prompt_build` hook 注入 prependContext | ❌ 没有实现该 hook 的插件代码 |
| OpenClaw Gateway → POST /route → webhook server | ❌ 没有配置 webhook 调用 |
| 自动调用 semantic_check.py | ❌ 不会自动调用 |

**这解释了为什么 README 里找不到配置说明**——因为对应的实现根本不在发布包里。

## SKILL.md ≠ prependContext

常被混淆的两个概念：

| 概念 | 是什么 | 谁控制 |
|------|--------|--------|
| SKILL.md | 技能文档，告诉 agent 该怎么做 | 技能作者写好 |
| prependContext | 在 agent 处理前注入上下文 | OpenClaw 系统注入 |

SKILL.md 只是一份说明书：OpenClaw 把内容注入提示词，agent 读了之后**自己决定**要不要执行。在 SKILL.md 里声明 hook 不会对 prependContext 产生任何影响。

## 为什么某些 session 没触发

1. 该 session 的 agent 没有读到 semantic-router 的 SKILL.md
2. 或者读到了但选择不执行
3. `semantic_check.py` 必须被**显式调用**才会工作

## 可行的生效方式

在 **AGENTS.md** 中写明强制指令：

```
## 语义路由规则
每次收到用户消息时，必须执行：
1. 调用 semantic_check.py 分析消息
2. 根据返回的 pool 切换模型池
3. 在响应第一行输出路由声明
```

## 教训

安装 ClawHub 技能后，先核对 `clawhub.yaml` 的 description 与实际交付物是否包含运行时代码，不要只看 README 的功能描述就认定能自动生效。

## 相关

- [[skillopt]]
- [[superresearch]]

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
