---
pageType: entity
id: entity.bug.feishu-cardkit-400-streaming
title: 飞书 CardKit 流式卡片 HTTP 400
entityType: bug
aliases:
  - 飞书 streaming start failed
  - cardkit 400
  - create card request failed
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.feishu-cardkit-400.log-signature
    text: "典型错误日志：`feishu[default]: streaming start failed; using non-streaming card fallback for 60s: Error: Create card request failed with HTTP 400`。系统会自动 fallback 到普通消息模式并持续 60 秒。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-feishu-streaming-fix-45b40229
        weight: 0.85
  - id: claim.feishu-cardkit-400.call-path
    text: "故障调用点是 OpenClaw 调用飞书 CardKit API 创建流式卡片：`POST /cardkit/v1/cards`，body 为 `{ type: \"card_json\", data: JSON.stringify(cardJson) }` 返回 HTTP 400；随后本应把卡片 ID 通过 `im.message.create` 以 interactive 类型消息发出并用 PATCH 增量更新内容。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-feishu-streaming-fix-45b40229
        weight: 0.8
  - id: claim.feishu-cardkit-400.not-blockstreaming
    text: "该问题不能通过调整 blockStreamingDefault 解决——即使开启 block streaming，若飞书创建卡片的 API 调用本身返回 400，streaming 依然无法工作。这是飞书应用权限或 API 限流问题，不是 OpenClaw 输出配置问题。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-feishu-streaming-fix-45b40229
        weight: 0.85
  - id: claim.feishu-cardkit-400.causes
    text: "HTTP 400 的常见原因：CardKit API 权限缺失（应用未开通 cardkit:card 相关权限）、卡片 header.subtitle 或 elements 内容为空/格式错误、卡片 JSON 超出大小限制、短时间内频繁创建卡片触发飞书限流。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-29-feishu-streaming-fix-45b40229
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-29-feishu-streaming-fix-45b40229.md

---
# 飞书 CardKit 流式卡片 HTTP 400

## 错误特征

```
feishu[default]: streaming start failed; using non-streaming card fallback for 60s:
Error: Create card request failed with HTTP 400
```

出现后会 fallback 成普通消息（无流式效果），持续 60 秒。

## 定位

故障调用：

```
POST /cardkit/v1/cards
Body: { type: "card_json", data: JSON.stringify(cardJson) }
→ HTTP 400
```

正常链路本应是：创建卡片拿到卡片 ID → `im.message.create` 发 interactive 类型消息 → PATCH 增量更新卡片内容实现流式。

## 关键判断

**这不是 blockStreamingDefault 能修的问题。** 改输出流式配置只影响 OpenClaw 侧如何切分输出；卡片创建请求本身被飞书拒绝，配置再怎么调都流式不起来。排查方向应该是飞书应用权限与 API 限流。

## 可能原因

1. CardKit API 权限缺失 — 应用未开通 `cardkit:card` 相关权限
2. 卡片 `header.subtitle` 或 `elements` 内容为空或格式错误
3. 卡片 JSON 超出大小限制
4. 短时间内创建卡片过于频繁，触发飞书限流

## 处理方案

**方案一（推荐，求稳）：关闭 streaming card**，改用普通消息模式，没有流式效果但稳定：

```json
{ "channels": { "feishu": { "streaming": false } } }
```

**方案二：检查飞书应用权限。** 登录飞书开放平台 → 权限管理，确认开通：
- `cardkit:card:readonly` / `cardkit:card:create`
- `im:message:create_card`
- `im:message`
- `im:message.p2p_msg:readonly`

## 相关

- [[blockStreamingDefault-config]] — 容易被误认为本问题的解药，实际是两回事

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
