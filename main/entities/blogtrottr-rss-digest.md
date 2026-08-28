---
pageType: entity
id: entity.project.blogtrottr-rss-digest
title: Blogtrottr RSS 邮件订阅日报
entityType: project
aliases:
  - Blogtrottr
  - Blogtrottr 日报
  - Karpathy 精选 RSS 日报
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.blogtrottr.mechanism
    text: "Blogtrottr 的工作机制是把 RSS 订阅更新推送到指定邮箱（形如 your-blogtrottr@blogtrottr.com 或自定义域名），因此接入前必须知道该专用邮箱地址，并具备能读取该邮箱的客户端。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-18-blogtrottr-digest-4159ec8e
        weight: 0.9
  - id: claim.blogtrottr.mail-clients
    text: "workspace 中可用的邮件访问工具：himalaya（通用 IMAP/SMTP CLI）与 gog（Google Workspace CLI，可访问 Gmail）；选哪个取决于 Gmail 是否开启 IMAP。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-18-blogtrottr-digest-4159ec8e
        weight: 0.85
  - id: claim.blogtrottr.schedule
    text: "日报发送时间对齐 Karpathy RSS 日报的惯例：每天中午 12 点发送到飞书群。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-18-blogtrottr-digest-4159ec8e
        weight: 0.8
  - id: claim.blogtrottr.output-format
    text: "产出格式为「核心主题」导语 + 按条展开的资讯汇总，每期标注条数（如「共 4 条更新」「共 13 条更新」），标题形如 `# YYYY-MM-DD - XXX 精选 RSS 日报`。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-20-blogtrottr-daily-a591f28c
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-18-blogtrottr-digest-4159ec8e.md
  - sources/bridge-workspace-142ea9a2-memory-2026-04-20-blogtrottr-daily-a591f28c.md

---
# Blogtrottr RSS 邮件订阅日报

把 RSS 订阅经邮件通道汇总后投递到飞书群的日报流水线。

## 链路

```
RSS 源 → Blogtrottr → 专用邮箱 → (himalaya / gog) → 汇总 → 飞书群
```

## 接入前提（三个必答问题）

| # | 需确认 | 说明 |
|---|--------|------|
| 1 | Blogtrottr 邮箱地址 | 如 `xxx@blogtrottr.com` 或自定义域名 |
| 2 | 邮件访问工具 | `himalaya`（通用 IMAP/SMTP）或 `gog`（Gmail）；取决于 Gmail 是否开 IMAP |
| 3 | 发送时间 | 每天 **12:00** 发飞书群（对齐 Karpathy 日报） |

## 产出格式

```
# YYYY-MM-DD - Karpathy 精选 RSS 日报
> ... 资讯汇总 | 共 N 条更新
## 🔥 核心主题：一句话概括本期主线
## 分类小标题
```

命中率参考：某期 4 条更新聚焦「传统车企反攻新能源——线控制动量产上车与芯片供应链博弈」；另一期 13 条聚焦「AI 工具定价战」。

## 相关

- [[feishu-4000-char-split-limit]] — 长日报投递到飞书时的 4000 字符拆分坑
- [[searxng]] — 另一条联网信息获取通道

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
