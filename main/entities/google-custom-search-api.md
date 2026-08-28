---
pageType: entity
id: entity.tool.google-custom-search-api
title: Google Custom Search API
entityType: tool
aliases:
  - Google CSE
  - Google Programmable Search
  - cx Search Engine ID
updatedAt: 2026-08-28T16:05:00.000Z
status: proposed
claims:
  - id: claim.google-cse.consent-block
    text: "从中国 IP 访问 Google 会触发 consent/cookie 拦截页，这是 Google 的反爬与合规机制；预设 Cookie 方案已实测无效，SearXNG 无法自动绕过。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-google-custom-search-b1c6f1be
        weight: 0.9
  - id: claim.google-cse.pricing
    text: "Google Custom Search Engine 本身免费；Custom Search API 免费额度 100 次/天，超出 $5/1000 次（$0.005/次），并存在每日调用上限。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-google-custom-search-b1c6f1be
        weight: 0.9
  - id: claim.google-cse.not-in-searxng
    text: "SearXNG 的 Google 引擎是直接爬取网页，没有内置的 Custom Search API 支持；要用官方 API 只能改 SearXNG 源码新增引擎，或绕过 SearXNG 在搜索脚本里直接调用。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-google-custom-search-b1c6f1be
        weight: 0.85
  - id: claim.google-cse.integration-plan
    text: "接入推荐走「方案 A」：不改 SearXNG，直接在 local-web-search 脚本中调用 Google CSE API，需用户提供 API Key（AIza...）与 Search Engine ID（cx）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-google-custom-search-b1c6f1be
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-30-google-custom-search-b1c6f1be.md
relationships:
  - targetId: entity.tool.searxng
    targetTitle: "SearXNG 本地搜索实例"
    kind: alternative-to
    weight: 0.7

---
# Google Custom Search API

Google 官方搜索 API，用于解决本地 SearXNG 在中国网络环境下拿不到 Google 结果的问题。

## 为什么需要

- 中国 IP 访问 Google 必触发 consent 页，SearXNG 爬不到结果
- 预设 Cookie 绕过已验证无效
- 现有替代（Brave + AOL + Bing）实测可用，约 39 条结果，但广度不足

## 定价

| 项目 | 说明 |
|------|------|
| CSE 搜索引擎 | 免费创建、免费使用 |
| API 免费额度 | 100 次/天 |
| 超出计费 | $5 / 1,000 次 |
| 每日上限 | 有硬上限（付费可提） |

## 接入路径

1. https://console.developers.google.com/ 创建项目并启用 **Custom Search API**
2. 创建 API Key（形如 `AIza...`）
3. https://cse.google.com/cse/all 创建搜索引擎，拿 **Search Engine ID (cx)**
4. 集成方式二选一：
   - **方案 A（推荐）**：在 `local-web-search` 脚本里直接调 API，不动 SearXNG，简单可控
   - **方案 B**：给 SearXNG 写一个自定义引擎文件，需改源码

## Related
- [SearXNG 本地搜索实例](searxng.md)
- [本地搜索中文关键词污染](本地搜索中文关键词污染.md)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [本地搜索中文关键词污染](本地搜索中文关键词污染.md)
<!-- openclaw:wiki:related:end -->
