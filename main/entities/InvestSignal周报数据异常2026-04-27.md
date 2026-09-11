---
pageType: entity
id: entity.bug.investsignal-weekly-data-anomaly
title: InvestSignal 周报数据异常（2026-04-27 周期）
entityType: bug
aliases:
  - InvestSignal 周报数据缺失
  - 北向资金量级异常
updatedAt: 2026-09-11T13:06:31.713Z
status: identified
claims:
  - id: claim.investsignal-weekly.data-broken
    text: 2026-04-21~04-27 周期的 InvestSignal
      周报数据链路异常：主要指数行情显示「行情数据获取中...」为空值，北向资金净流入输出 34124151亿 这种明显失真量级，观察列表标的多为「⚪
      无法分析 / 置信度 0%」，报告名存实亡。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-investsignal-weekly-3b85963b
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2.memory-2026-04-30-investsignal-weekly-3b85963b.md
relationships:
  - targetId: entity.concept.investment-push-channels
    targetTitle: 投资信息推送渠道现状
    kind: related-to
    weight: 0.5
---

# InvestSignal 周报数据异常（2026-04-27 周期）

2026-04-30 收到周报推送时暴露的数据链路问题：数据缺失被静默降级为占位符，而非报错。

## 症状

| 栏目 | 输出 |
|------|------|
| 主要指数表现 | 「行情数据获取中...」（空值） |
| 资金流向 | 北向资金净流入 `34124151亿`（量级失真） |
| 观察列表分析 | 标的普遍「⚪ 无法分析 / 置信度 0%」 |
| 重要资讯回顾 | 「本周暂无重要资讯」 |

## 影响

周报的「数据完整性: 观察列表数据完整」结论与各标的实际无法分析相矛盾，报告会被当成有效信号误读，需先修数据源与字段校验。

## Related
- [投资信息推送渠道现状](投资信息推送渠道.md)

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
