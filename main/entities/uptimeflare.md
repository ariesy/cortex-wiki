---
pageType: entity
id: entity.tool.uptimeflare
title: UptimeFlare
entityType: tool
aliases:
  - uptimeflare
updatedAt: "2026-07-31T22:00:00.000Z"
status: active
claims:
  - id: claim.uptimeflare.architecture
    text: "UptimeFlare 是自建站点可用性监控服务，部署于 Cloudflare Workers，通过 ob-man 技能管理监测列表；检查频率为每分钟一次（`* * * * *` cron trigger），配置文件为 `/app/uptimeflare/uptime.config.ts`，worker 入口为 `worker/src/index.ts`。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-1526-62346a43
        weight: 0.9
  - id: claim.uptimeflare.grace-period
    text: "`gracePeriod` 是全局设置、所有监控共用，语义为「服务连续 DOWN 后的第 N 次检查（约 N×60 秒）才发通知」；`kvWriteCooldownMinutes` 默认 3 分钟，只影响 KV 写入频率，与检查无关。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-1526-62346a43
        weight: 0.9
  - id: claim.uptimeflare.no-per-monitor-interval
    text: "UptimeFlare 本身没有 per-monitor 检查频率配置，所有 monitor 共用同一 cron 与 gracePeriod；要按 monitor 独立间隔需改 `worker/src/index.ts` 增加 `skipEveryN` 字段，并在 `types/config.ts` 与 cron 逻辑中同步改动，属侵入式修改。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-1526-62346a43
        weight: 0.85
  - id: claim.uptimeflare.immich-false-positive
    text: "Immich 误报根因：偶发非 200（反代出错返回 nginx 502 页面），叠加 `gracePeriod: 2` 时短时毛刺即触发通知。2026-07-31 已将全局 `gracePeriod` 2 → 5 并 push 到 main（GitHub Actions 自动部署），短时毛刺不再误报，代价是其他服务通知延迟 3 分钟。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-1526-62346a43
        weight: 0.9
  - id: claim.uptimeflare.response-keyword-option
    text: "减少单点误报的备选方案（未实施）：给 Immich monitor 加 `responseKeyword: 'immich'`，要求响应内容含 Immich 特征字符串才算 UP，可从源头区分「反代返回的 200」与「真实 Immich 的 200」，且不影响其他监控。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-1526-62346a43
        weight: 0.8
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-07-31-1526-62346a43
---

# UptimeFlare

自建的站点可用性监控服务，部署于 Cloudflare Workers，通过 `ob-man` 技能维护监测列表；`research.zhu-kun.com` 等站点由它监控。

## 工作机制

| 项目 | 值 |
|------|-----|
| 检查频率 | 每分钟一次（`* * * * *` cron trigger） |
| `gracePeriod` | 全局设置，所有监控共用；原 2 分钟 → 2026-07-31 改为 5 分钟 |
| `kvWriteCooldownMinutes` | 默认 3 分钟，只影响 KV 写入频率，与检查无关 |
| 配置文件 | `/app/uptimeflare/uptime.config.ts` |
| Worker 入口 | `worker/src/index.ts` |

`gracePeriod` 语义：服务连续 DOWN 后的第 N 次检查（约 N×60 秒）才发通知。为 2 分钟时，每次误报约持续 2 分钟。

## 已知限制

- **没有 per-monitor 检查频率配置**：所有 monitor 共用同一个 cron 与 gracePeriod。要按 monitor 独立间隔，需修改 `worker/src/index.ts` 增加 `skipEveryN` 字段，并同步改 `types/config.ts` 与 cron 逻辑，属侵入式改动。

## Immich 误报治理（2026-07-31）

- **根因**：Immich 偶发非 200（反代出错时返回 nginx 502 页面），在 `gracePeriod: 2` 下短时毛刺即触发通知。
- **已实施**：全局 `gracePeriod` 2 → 5，push 到 `main`，GitHub Actions 自动部署。短时毛刺不再误报；代价是其他服务（NAS、VT 等容错较高）通知延迟约 3 分钟。
- **备选（未实施）**：给 Immich monitor 加 `responseKeyword: 'immich'`，要求响应内容含 Immich 特征字符串才算 UP，从源头区分「反代返回的 200」与「真实 Immich 的 200」，且不影响其他监控。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-07-31-1526](../sources/bridge-workspace-142ea9a2-memory-2026-07-31-1526-62346a43.md)
<!-- openclaw:wiki:related:end -->
