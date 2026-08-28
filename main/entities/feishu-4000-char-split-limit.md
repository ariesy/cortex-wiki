---
pageType: entity
id: entity.concept.feishu-4000-char-split-limit
title: 飞书消息 4000 字符拆分限制与卡片消息绕过
entityType: concept
aliases:
  - 飞书 4000 字符限制
  - 消息被拆分
  - 飞书卡片消息
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.feishu-4000-split.limit
    text: "OpenClaw 内部对单条消息有 4000 字符拆分限制，超长内容会被自动拆成多条发送（例如 5400 字符报告被拆成 ~4000 + ~1434 两条），API 仍返回 ok，发送是成功的。"
    status: supported
    confidence: 0.95
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-feishu-card-message-fix-70bad9ee
        weight: 0.95
  - id: claim.feishu-4000-split.misdiagnosis
    text: "「报告没发全」类反馈的常见误判：消息其实发成功了，只是被拆成两条，后半段被忽略。排查时应先确认是否触发拆分，而不是去查发送逻辑。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-feishu-card-message-fix-70bad9ee
        weight: 0.9
  - id: claim.feishu-4000-split.card-solution
    text: "用飞书卡片（interactive card）消息格式发送长 Markdown，可绕过 4000 字符拆分限制，且渲染效果优于纯文本。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-feishu-card-message-fix-70bad9ee
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-19-feishu-card-message-fix-70bad9ee.md

---
# 飞书消息 4000 字符拆分限制与卡片消息绕过

长报告「发送不全」问题的真正原因。

## 机制

OpenClaw 内部对单条消息有 **4000 字符**上限，超出部分自动拆成多条：

```
5400 字符报告 → 第1条 ~4000 字符（核心结论）
              → 第2条 ~1434 字符（后半部分）
```

**关键点**：API 返回 `ok`，两条都真的发出去了。

## 误判模式

用户反馈「报告只收到一半」→ 通常不是发送失败，而是第二条被忽略。

排查顺序：
1. 先数内容长度，判断是否触发拆分
2. 再去翻完整消息流找第二条
3. 最后才怀疑发送逻辑

## 解法

长 Markdown 改用**飞书卡片消息**（interactive card）：

- 绕过 4000 字符拆分
- 渲染效果比纯文本好

## 相关

- [[feishu-plugin-bundle-conflict]] — 飞书通道的另一类故障

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
