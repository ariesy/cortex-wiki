---
pageType: entity
entityType: project
id: entity.project.research-zhu-kun-com
updatedAt: "2026-07-30"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-07-30-0901-250b5701
  - source.bridge.workspace-142ea9a2.memory-2026-07-30-1110-071a8e6c
claims:
  - id: claim.research-zhu-kun-com.type
    text: "research.zhu-kun.com 是一个投资研究报告展示网站"
    status: established
    confidence: 0.95
    evidence:
      - kind: source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-30-0901-250b5701
        note: "部署完成，首页展示3份ETF分析报告"
  - id: claim.research-zhu-kun-com.reports
    text: "网站展示中证白酒(161725.SZ)、科创50ETF(588000.SS)、储能电池ETF(159566.SZ)三份报告，使用AI Berkshire和TradingAgents双框架分析"
    status: established
    confidence: 0.95
    evidence:
      - kind: source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-30-0901-250b5701
        note: "部署完成，报告包含10个章节：产品概况、估值分析、技术面、多空辩论等"
  - id: claim.research-zhu-kun-com.monitoring
    text: "通过UptimeFlare进行监控，使用ob-man技能添加到监测列表"
    status: established
    confidence: 0.9
    evidence:
      - kind: source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-30-1110-071a8e6c
        note: "使用ob-man技能把research.zhu-kun.com加入监测列表"
---

# research.zhu-kun.com

> entity_type: project

**类型:** Project  
**ID:** `research_zhu_kun_com`  
**状态:** active  
**优先级:** medium  
**来源:** 飞书群聊对话

---

## 概述

research.zhu-kun.com 是一个投资研究报告展示网站，用于发布使用 AI 框架（AI Berkshire 和 TradingAgents）生成的 ETF 分析报告。

## 当前报告

| # | 报告 | 评级 | 最新日期 |
|:---:|:---|:---:|:---:|
| 1 | 🍶 中证白酒 (161725.SZ) | **Hold** | 2026-07-30 |
| 2 | 🔻 科创50ETF (588000.SS) | Underweight | 2026-07-30 |
| 3 | ⚡ 储能电池ETF (159566.SZ) | Hold | 2026-07-30 |

## 分析框架

- **AI Berkshire** - 四大师综合评分（生意质量/护城河/文明趋势/估值）
- **TradingAgents** - 技术面分析 + 多空辩论 + 组合经理裁定

## 基础设施

- **部署**: Cloudflare Workers
- **监控**: UptimeFlare (通过 ob-man 技能配置)
- **数据源**: InvestSignal ETF 数据接口

## 相关 Entity

- InvestSignal (investsignal-target-price-alert)
- 储能电池ETF (159566.SZ)
- 科创50ETF (588000.SS)

## 时间线

- 2026-07-30: 网站部署完成，发布3份报告
- 2026-07-30: 添加 UptimeFlare 监控

---

*最后更新: 2026-07-30*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-07-30-0901](../sources/bridge-workspace-142ea9a2-memory-2026-07-30-0901-250b5701.md)
- [Memory Bridge (main): 2026-07-30-1110](../sources/bridge-workspace-142ea9a2-memory-2026-07-30-1110-071a8e6c.md)
<!-- openclaw:wiki:related:end -->
