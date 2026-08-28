---
pageType: entity
id: entity.bug.web-search-fallback-chain
title: web_search fallback 链误判（Brave key 其实已配置）
entityType: bug
aliases:
  - Tavily 432
  - Brave API key 不存在误判
  - 搜索 provider fallback
updatedAt: 2026-08-28T16:10:00.000Z
status: active
claims:
  - id: claim.search-fallback.chain
    text: "web_search 的 provider fallback 链为：Tavily（默认）→ FireCrawl → Brave Search API → local-web-search（SearXNG, localhost:8888）→ minimax → Exa（最后，仅语义补充）。默认 provider 返回错误/超时/无结果时应依次尝试下一个，全部失败才告知用户搜索不可用。"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-web-search-652f19fb
        weight: 0.9
  - id: claim.search-fallback.misdiagnosis
    text: "判断某个搜索 provider 是否可用，不能只看环境变量（如 BRAVE_API_KEY）。Brave API key 实际配置在 openclaw.json 里，只检查 env 会得出「未配置」的错误结论，导致 assistant 跳过合法的 fallback 步骤并向用户谎报「环境不支持」。正确做法是检查 OpenClaw 配置文件，而不是 shell 环境变量。"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-school-search-a9e52462
        weight: 0.9
  - id: claim.search-fallback.tavily-432
    text: "Tavily 额度耗尽时 web_search 返回 432 错误，这是 fallback 链的正常触发点，不是搜索功能整体不可用。不应在此时直接跳到 local-web-search 或向用户宣告失败。"
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-school-search-a9e52462
        weight: 0.85
  - id: claim.search-fallback.searxng-zh-poor
    text: "local-web-search（SearXNG）对中文教育/政务类查询质量很差，会返回完全无关结果（如查「福苑学校」返回赛百味、五岳阅卷）。这类查询不宜依赖 SearXNG。"
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-school-search-a9e52462
        weight: 0.85
  - id: claim.search-fallback.workarounds
    text: "搜索 provider 全部不给力时的补充手段：① 用 tavily_extract / web_fetch 直接抓取已知权威站点页面（如 zs.szft.gov.cn）；② 直接请用户在浏览器打开权威站点自查，比反复换搜索引擎更快更准。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-school-search-a9e52462
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-30-school-search-a9e52462.md
  - sources/bridge-workspace-142ea9a2-memory-web-search-652f19fb.md

---
# web_search fallback 链误判（Brave key 其实已配置）

排查「搜索搜不到东西」类问题时的典型误判：把**单个 provider 额度耗尽**当成**整个搜索不可用**，并且用错方法验证后续 provider 是否配置。

## 正确的 fallback 链

| 优先级 | Provider | 备注 |
|---|---|---|
| 1 | Tavily | 默认 provider，额度耗尽返回 **432** |
| 2 | FireCrawl | 搜索 + 抓取解析 Markdown |
| 3 | Brave Search API | 配置在 `openclaw.json` |
| 4 | local-web-search | 本地 SearXNG，`http://localhost:8888` |
| 5 | minimax | MiniMax Token Plan search API |
| 6 | Exa | neural search，仅语义补充（控成本） |

触发条件：默认 provider 报错 / 超时 / 无结果 → 下一个。全部失败才告诉用户搜索不可用。

## 误判模式

```
Tavily 432
  ↓
❌ 只查环境变量 BRAVE_API_KEY → 没找到 → 断言「Brave 未配置」
  ↓
❌ 直接跳到 local-web-search → 质量差 → 向用户报告「搜索基础设施有限」
```

实际情况：Brave key 早就写在 `openclaw.json` 里，这一步本可以直接走通。

> **规则**：查 provider 配置 → 看 OpenClaw 配置文件，不是看 shell 环境变量。

## 已知弱点：SearXNG 中文垂类

local-web-search 对中文教育/政务类查询返回无关结果（查「福苑」返回赛百味、五岳阅卷）。中文垂类查询不要把 SearXNG 当主力。

## 兜底手段

1. 用 `tavily_extract` / `web_fetch` 直接抓已知权威站点（如 `zs.szft.gov.cn`）
2. 请用户自己在浏览器打开权威站点核对 —— 通常比换搜索引擎更快

## 相关

- [[搜索工具使用规范]] — 搜索技能的优先级与 superresearch 强制流程
- [[local-web-search]] — 自建 SearXNG 搜索引擎

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
