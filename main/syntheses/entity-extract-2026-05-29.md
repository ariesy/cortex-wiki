---
pageType: synthesis
id: synthesis.entity-extract-2026-05-29
title: "实体提取汇总 2026-05-29"
status: active
updatedAt: "2026-05-29T16:02:00.000Z"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-05-29-1247-72519746
  - source.bridge.workspace-142ea9a2.memory-2026-05-29-1030-afa662bf
  - source.bridge.workspace-142ea9a2.memory-2026-05-29-e8b4db1b
  - source.bridge.workspace-142ea9a2.memory-2026-05-28-1418-3438f599
  - source.bridge.workspace-142ea9a2.memory-2026-05-28-0733-de1c9513
  - source.bridge.workspace-142ea9a2.memory-2026-05-27-0937-a6ecb387
  - source.bridge.workspace-142ea9a2.memory-2026-05-27-0459-083b67f7
  - source.bridge.workspace-142ea9a2.memory-2026-05-26-1544-25f17a7e
  - source.bridge.workspace-142ea9a2.memory-2026-05-25-0801-e81e4534
  - source.bridge.workspace-142ea9a2.memory-2026-05-25-0735-530735a4
  - source.bridge.workspace-142ea9a2.memory-2026-05-24-1102-6b9a4e3d
  - source.bridge.workspace-142ea9a2.memory-2026-05-22-1144-56c3d6b0
  - source.bridge.workspace-142ea9a2.memory-2026-05-15-pangu-finetuning-terminology-4996e404
  - source.bridge.workspace-142ea9a2.memory-2026-05-16-elderly-friendly-video-adjustm-32b9ae8a
claims:
  - id: claim.entity-extract.20260529.feishu-bug-channel-turn
    text: "飞书插件在OpenClaw 2026.5.27版本中因SDK API重构（runtime.channel.turn被移除）导致TypeError"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-29-1030-afa662bf
        weight: 0.9
  - id: claim.entity-extract.20260529.p0-workflow-completed
    text: "P0优化工作流于2026-05-29完成，为32个investment entities补充了claims、relationships和privacyTier"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-29-1247-72519746
        weight: 0.9
  - id: claim.entity-extract.20260529.micron-surge
    text: "美光科技(MU) 2026-05-27涨超19%，市值首破1万亿美元，存储芯片板块爆发"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-28-1418-3438f599
        weight: 0.85
  - id: claim.entity-extract.20260529.huawei-logic-folding
    text: "华为发布半导体韬定律，秋季将发新麒麟芯片（逻辑折叠技术）"
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-28-1418-3438f599
        weight: 0.8
  - id: claim.entity-extract.20260529.us-iran-conflict
    text: "美伊冲突升级，美国对伊朗实施军事打击，霍尔木兹海峡局势紧张，原油接近100美元"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-28-1418-3438f599
        weight: 0.85
relationships:
  - targetId: entities.investments.贵州茅台_600519
    targetTitle: 贵州茅台
    kind: references-in-synthesis
    weight: 0.7
    note: "茅台作为关键投资标的在P0工作流中被优先处理"
  - targetId: entities.investments.五粮液_000858
    targetTitle: 五粮液
    kind: references-in-synthesis
    weight: 0.6
    note: "五粮液与茅台同业竞争关系在P0工作流中建立"
  - targetId: entities.bugs.minimax-oauth
    targetTitle: MiniMax OAuth Bug
    kind: relates-to
    weight: 0.5
    note: "SDK兼容性问题的同类bug"
  - targetId: concepts.hbm-memory-shortage
    targetTitle: HBM 存储芯片短缺
    kind: relates-to
    weight: 0.6
    note: "美光暴涨与HBM存储需求相关"
---

# 实体提取汇总 2026-05-29

## 本周重点实体提取（2026-05-15 ~ 2026-05-29）

### 投资分析
- **美光科技(MU)**：2026-05-27涨超19%，市值首破1万亿美元，存储芯片板块爆发
- **半导体指数**：费城半导体指数涨5.53%刷新历史新高
- **宇树科技**：科创板IPO 6月1日上会，计划募资约42亿元
- **长鑫科技**：科创板IPO 5月27日上会
- **英伟达**：GTC Taipei 2026将于6月1-4日举办
- **华为**：发布半导体韬定律，秋季将发新麒麟芯片（逻辑折叠技术）

### Bug发现
- **飞书插件runtime.channel.turn Bug**：在OpenClaw 2026.5.27版本中，飞书插件因SDK API重构（`runtime.channel.turn` 被移除）导致 `TypeError: Cannot read properties of undefined (reading 'run')`。该bug影响了飞书群消息的正常dispatch

### 技能使用
- **Superpowers调试流程**：使用superpowers技能的系统化调试流程追踪飞书插件bug，从root cause investigation到pattern analysis
- **P0 Workflow执行**：启动3个subagents同时执行claims补充、relationships建立、privacyTier标注工作流

### 概念讨论
- **PanGu微调术语**：讨论了PanGu微调涉及的terminology和技术细节
- **老年人友好视频调整**：针对 elderly-friendly video adjustments 的技术方案讨论
- **逻辑折叠技术**：华为麒麟芯片的逻辑折叠（logic folding）技术概念

### 配置变更
- **Wiki P0优化**：为32个investment entities补充了core claims（bull-case/bear-case/key-metric），建立了板块relationships，标注了privacyTier

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-05-29-1247](sources/bridge-workspace-142ea9a2-memory-2026-05-29-1247-72519746.md)
- [Memory Bridge (main): 2026-05-29-1030](sources/bridge-workspace-142ea9a2-memory-2026-05-29-1030-afa662bf.md)
- [Memory Bridge (main): 2026-05-29](sources/bridge-workspace-142ea9a2-memory-2026-05-29-e8b4db1b.md)
- [Memory Bridge (main): 2026-05-28-1418](sources/bridge-workspace-142ea9a2-memory-2026-05-28-1418-3438f599.md)
- [Memory Bridge (main): 2026-05-28-0733](sources/bridge-workspace-142ea9a2-memory-2026-05-28-0733-de1c9513.md)
- [Memory Bridge (main): 2026-05-27-0937](sources/bridge-workspace-142ea9a2-memory-2026-05-27-0937-a6ecb387.md)
- [Memory Bridge (main): 2026-05-27-0459](sources/bridge-workspace-142ea9a2-memory-2026-05-27-0459-083b67f7.md)
- [Memory Bridge (main): 2026-05-26-1544](sources/bridge-workspace-142ea9a2-memory-2026-05-26-1544-25f17a7e.md)
- [Memory Bridge (main): 2026-05-25-0801](sources/bridge-workspace-142ea9a2-memory-2026-05-25-0801-e81e4534.md)
- [Memory Bridge (main): 2026-05-25-0735](sources/bridge-workspace-142ea9a2-memory-2026-05-25-0735-530735a4.md)
- [Memory Bridge (main): 2026-05-24-1102](sources/bridge-workspace-142ea9a2-memory-2026-05-24-1102-6b9a4e3d.md)
- [Memory Bridge (main): 2026-05-22-1144](sources/bridge-workspace-142ea9a2-memory-2026-05-22-1144-56c3d6b0.md)
- [Memory Bridge (main): 2026-05-15-pangu-finetuning-terminology](sources/bridge-workspace-142ea9a2-memory-2026-05-15-pangu-finetuning-terminology-4996e404.md)
- [Memory Bridge (main): 2026-05-16-elderly-friendly-video-adjustm](sources/bridge-workspace-142ea9a2-memory-2026-05-16-elderly-friendly-video-adjustm-32b9ae8a.md)
<!-- openclaw:wiki:related:end -->
