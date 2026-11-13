---
pageType: entity
id: entity.concept.deepseek-v4-pro-pricing-hike-2026-08
title: DeepSeek V4 Pro 涨价与 opencode Go 套餐冲击（2026-08）
entityType: concept
aliases:
  - DeepSeek V4 Pro 涨价
  - V4-Pro-0813
  - opencode Go 套餐缩水
updatedAt: 2026-08-14T09:45:40.740Z
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-14-0945-3fe94146
claims:
  - id: claim.deepseek-v4pro-hike.2026-08-13.pricing
    text: 2026-08-13 晚 DeepSeek 上线 V4 Pro 正式版（V4-Pro-0813），公布峰谷定价于 8月17日 00:00 生效：高峰缓存命中 0.30 元 / 未命中 9.0 元 / 输出 27.0 元，闲时 0.15 / 4.5 / 13.5 元；涨价前为 0.025 / 3.0 / 6.0 元。高峰涨幅：缓存命中 1100%、未命中 200%、输出 350%；V4 Flash 同步上涨 250-350%。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-0945-3fe94146
        weight: 1.0
  - id: claim.deepseek-v4pro-hike.2026-08-14.opencode-go
    text: 截至 2026-08-14 opencode Go 未针对 DeepSeek 涨价发布新公告：套餐仍为 $5 首月 / $10 每月，限额 5h $12 / 周 $30 / 月 $60，文档最后更新 8月4日，V4 Pro 内部定价仍为 $0.435/$0.87/$0.003625（旧价）。但 Go 模型表已把 DeepSeek V4 Pro 放入 $15 低额度档；GitHub issue #28846（要求上调额度）仍 open；工程师 dax 称 Go 实际消耗成本约为官方 API 4 倍（缓存命中率低）。若内部定价跟进，V4 Pro 月额度请求数将从约 17,150 次大幅缩水。
    status: supported
    confidence: 0.7
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-0945-3fe94146
        weight: 1.0
  - id: claim.deepseek-v4pro-hike.2026-08-14.recommendation
    text: 对高频重度用户的建议：等 8月17日涨价生效后 opencode Go 额度大概率缩水，直连 DeepSeek 官方 API（尤其闲时段）成本更可控；此前通过 opencode.ai 网关调 DeepSeek 曾出现超时挂死教训。
    status: supported
    confidence: 0.65
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-14-0945-3fe94146
        weight: 1.0
---

# DeepSeek V4 Pro 涨价与 opencode Go 套餐冲击（2026-08）

## 价格对比

| | 缓存命中 | 缓存未命中 | 输出 |
|---|---|---|---|
| V4 Pro 高峰 | 0.30 元 | 9.0 元 | 27.0 元 |
| V4 Pro 闲时 | 0.15 元 | 4.5 元 | 13.5 元 |
| 涨价前 | 0.025 元 | 3.0 元 | 6.0 元 |

## opencode Go 套餐

- 订阅：首月 $5，之后 $10/月
- 额度：5h $12 / 周 $30 / 月 $60
- 截至 2026-08-14 未见配套调整，V4 Pro 已被放入 $15 低额度档
- 关联 issue：opencode #28846

## 相关

- [[deepseek-tui]]
- [[opencode-permission-rule-order-bug]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-14-0945](../sources/bridge-workspace-142ea9a2-memory-2026-08-14-0945-3fe94146.md)
<!-- openclaw:wiki:related:end -->
