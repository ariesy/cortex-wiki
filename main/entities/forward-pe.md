---
pageType: entity
id: forward-pe
title: "Forward PE（远期市盈率）"
tags: [金融概念, 估值, PE, 市盈率, Forward-PE, 投资分析]
updatedAt: "2026-08-05"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-05-1448-926907e2
claims:
  - id: claim.forward-pe.definition
    text: "Forward PE（远期市盈率）= 当前股价 ÷ 未来12个月（或下一财年）预期每股收益，也可表述为总市值 ÷ 预期净利润；分母使用分析师预测盈利，而非已实现盈利。"
    status: supported
    confidence: 0.9
  - id: claim.forward-pe.vs-trailing
    text: "Trailing PE 使用过去已实现盈利（TTM 或上一年报净利润），Forward PE 使用分析师预测的明年盈利；例：股价100元、去年EPS 5元 → Trailing PE 20倍；预测明年EPS 8元 → Forward PE 12.5倍。"
    status: supported
    confidence: 0.85
  - id: claim.forward-pe.why-use
    text: "使用 Forward PE 的原因：更能反映成长性（高增长公司用历史盈利显得贵）；常用于跨期比较与 PEG 分析（PEG = Forward PE ÷ 预期增速）；港美股研报中的 PE 多默认指 Forward PE。"
    status: supported
    confidence: 0.8
  - id: claim.forward-pe.risks
    text: "Forward PE 的风险：分母为预测值，分析师可能过于乐观，盈利不及预期时估值被动抬高；强周期股（券商、航运、半导体）在盈利顶部 Forward PE 最低，反而是危险信号（低 PE 陷阱）；不同数据源对 forward 口径定义不同（未来12个月 vs 下一财年），横向比较需确认口径。"
    status: supported
    confidence: 0.8
  - id: claim.forward-pe.a-share-analogy
    text: "A股的“动态市盈率”有时指用预测或年化盈利计算的市盈率，与港美股 Forward PE 概念相近但不完全一致，需留意行情软件的计算口径。"
    status: supported
    confidence: 0.7
---

# Forward PE（远期市盈率）

## 定义

Forward PE（远期市盈率）是基于**未来预期盈利**计算的市盈率：

```
Forward PE = 当前股价 ÷ 未来12个月（或下一财年）预期 EPS
           = 总市值 ÷ 预期净利润
```

## 与 Trailing PE 的区别

| 口径 | 分母 | 说明 |
|------|------|------|
| Trailing PE（滚动/静态） | 过去已实现盈利（TTM 或上一年报） | 反映历史 |
| Forward PE（远期） | 分析师预测的明年盈利 | 反映预期 |

**举例**：股价 100 元，去年 EPS 5 元 → Trailing PE = 20 倍；分析师预测明年 EPS 8 元 → Forward PE = 12.5 倍。

## 为什么用 Forward PE

1. **更能反映成长性** —— 高增长公司用过去盈利算 PE 会显得很贵，用预期盈利更能看清估值合理性
2. **常用于跨期比较与 PEG 分析** —— PEG = Forward PE ÷ 预期增速，判断估值是否匹配成长
3. 港股/美股研报里的 PE 很多默认是 Forward PE

## 风险点

- 分母是**预测值**，分析师可能过于乐观；盈利不及预期时 Forward PE 会瞬间被动抬高
- 强周期股（券商、航运、半导体）在盈利顶部时 Forward PE 最低，反而是危险信号 —— 所谓“低 PE 陷阱”
- 不同数据源对 "forward" 的定义不同（未来12个月 vs 下个财年），横向比较时要确认口径
- A股“动态市盈率”有时即指预测/年化盈利口径，与港美股 Forward PE 相近但不完全一致，看行情软件时需留意计算口径

## 相关实体

- [[investment-preferences]]（估值口径偏好）
- [[ai-berkshire-价值投资研究框架]]（四大师估值维度）

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-05-1448](../sources/bridge-workspace-142ea9a2-memory-2026-08-05-1448-926907e2.md)
<!-- openclaw:wiki:related:end -->
