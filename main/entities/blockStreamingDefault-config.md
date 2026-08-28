---
pageType: entity
id: entity.config.blockstreamingdefault
title: OpenClaw blockStreamingDefault 配置（飞书流式输出）
entityType: config
aliases:
  - blockStreamingDefault
  - 飞书流式输出
  - blockStreamingBreak
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.blockstreaming.schema-values
    text: "`blockStreamingDefault` 的 schema 只允许两个值：`on`（所有输出累积后一次性发送）和 `off`（所有输出实时流式发送）。不存在 `text` 这个取值——曾按 `text` 配置过，是无效的。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-block-streaming-config-5ab5ac0e
        weight: 0.85
  - id: claim.blockstreaming.restart-overwrites
    text: "直接编辑 OpenClaw 配置文件改 blockStreamingDefault 会被 Gateway 重启覆盖回去。第一次改成 `text` 后看似生效，Gateway 重启时文件被写回原值，必须通过 OpenClaw 自身的配置修改途径（而非手改文件）才能持久化。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-block-streaming-config-5ab5ac0e
        weight: 0.85
  - id: claim.blockstreaming.on-symptom
    text: "`blockStreamingDefault: \"on\"` 的表现是：Agent 的思考过程、工具调用结果、分步分析全部不会实时推送，只有整个 turn 完成后（blockStreamingBreak: text_end）才一次性发出。日志上表现为 streaming 卡片 Started 与 Closed 仅相隔数秒。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-block-streaming-config-5ab5ac0e
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-29-block-streaming-config-5ab5ac0e.md

---
# OpenClaw blockStreamingDefault 配置

控制 Agent 输出是否实时流式推送到飞书。

## 取值（只有两个）

| 值 | 行为 |
|----|------|
| `on` | 所有输出累积，整个 turn 完成后（`text_end`）一次性发送 |
| `off` | 输出实时流式推送 |

**没有 `text` 值。** 曾尝试配置 `blockStreamingDefault: "text"` 期望"文本流式、工具调用不流式"，schema 不接受，属于无效配置。

## 踩过的坑

1. **手改配置文件会被覆盖。** 改成 `text` 后报告"已修改完成、Gateway 已重启"，实际下次检查发现配置没生效——Gateway 重启时把文件覆盖回原值。改动必须走 OpenClaw 自身的配置修改方式。
2. **改错值要承认。** 第一次给出的 `text` 选项是错的，正确做法是先核对 schema 再告知用户。

## 如何判断当前是否真的流式

看 Gateway 日志里 streaming 卡片的 Started / Closed 时间戳间隔：

- 间隔只有几秒 → 是最终输出一次性发送，不是实时流式
- 用户侧现象：长时间看不到中间过程，最后突然收到完整报告

## 相关

- [[feishu-cardkit-400-streaming]] — 即使改成 off，若飞书卡片 API 报 400 依然流式不起来

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
