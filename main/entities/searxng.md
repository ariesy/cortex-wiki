---
pageType: entity
id: entity.tool.searxng
title: SearXNG 本地搜索实例
entityType: tool
aliases:
  - SearXNG JSON API
  - Scrapling
updatedAt: 2026-09-04T13:14:11.012Z
status: active
claims:
  - id: claim.searxng.port
    text: 本地 SearXNG 实例运行在端口 8888，搜索技能需显式配置该端口才能接入。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-29-searxng-setup-f9dbee3f
        weight: 0.9
  - id: claim.searxng.json-api-gotcha
    text: 排障要点：SearXNG 的 formats 配置为空会静默禁用 JSON API，导致程序化调用失败。必须在 settings.yml 的
      search.formats 中启用 json 后重启容器。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-29-searxng-setup-f9dbee3f
        weight: 0.9
  - id: claim.searxng.scrapling
    text: 抓取引擎选用 Scrapling 并配合持久化配置；Playwright 因需要 sudo 跳过，基础 Fetcher 模式已足够日常使用。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-29-searxng-setup-f9dbee3f
        weight: 0.85
  - id: claim.searxng.google-blocked
    text: "SearXNG 无法使用 Google 搜索引擎，2026-05-05 立案为待办 TSK-652B「解决 SearXNG 无法使用 Google
      搜索引擎的问题」；该问题是 Google 引擎侧的整体失效，而非本地 JSON API / 端口配置问题（后者已在 03-29 排障中解决）。后续
      2026-05-09 排查指向 Google 对 SearXNG 实例的 TLS/HTTP2 指纹封锁（GitHub issue #2515）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-searxng-google-ead00353
        weight: 0.85
        note: "TSK-652B 立案；根因 #2515 出自 2026-05-09 searxng-google-fix 源"
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-03-29-searxng-setup-f9dbee3f.md
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-searxng-google-ead00353.md
---

# SearXNG 本地搜索实例

自托管的元搜索实例，作为联网搜索技能的后端。

## 配置

| 项 | 值 |
|----|----|
| 端口 | 8888 |
| JSON API | 需在 `search.formats` 显式启用，否则被禁用 |
| 抓取引擎 | Scrapling（持久化配置） |
| Playwright | 需 sudo，已跳过；Fetcher 模式够用 |

## 排障清单

1. 搜索返回 403 / 非 JSON → 检查 `formats` 是否为空（最常见的静默失败点）
2. 连不上 → 确认容器监听 8888 且技能配置指向该端口
3. 改完 `settings.yml` 必须重启容器才生效

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Google Custom Search API](google-custom-search-api.md)
- [本地搜索中文关键词污染](本地搜索中文关键词污染.md)

### Related Pages

- [ffmpeg 不在 OpenClaw 可信路径导致 TTS 无法转码语音消息](openclaw-ffmpeg-trusted-path.md)
<!-- openclaw:wiki:related:end -->
