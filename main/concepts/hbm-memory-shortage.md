---
pageType: concept
id: concept.hbm-memory-shortage
title: "AI内存短缺危机"
updatedAt: "2026-05-29"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-05-23-1101
relationships:
  - targetId: entity.concept.minimax-quota-window
    targetTitle: "MiniMaxQuota窗口时间不一致"
    kind: related-to
    weight: 0.5
    note: "同为硬件资源问题"
---


# AI内存短缺危机

> HBM需求暴涨挤压消费级内存产能，廉价设备市场萎缩

**类型:** Concept  
**ID:** `concept_hbm_memory_shortage`  
**来源:** Karpathy RSS 2026-05-23

---


## 核心问题

全球仅存的三家内存厂商（Samsung、SK Hynix、Micron）晶圆产能固定，需要在以下类型之间分配：
- DDR（桌面/服务器）
- LPDDR（手机/低功耗设备）
- **HBM（GPU/AI数据中心）**

---

## 数据变化

| 指标 | 2025年 | 2026年底（预计） |
|------|--------|-----------------|
| HBM占晶圆产能 | 2% | **20%** |
| 每GB HBM消耗晶圆 | 基准 | **3倍以上** |

---

## 影响

1. **低端智能手机涨价** — 非洲、南亚市场受冲击最大
2. **树莓派6推迟至2028** — DRAM短缺导致高性能SBC成本翻倍
3. **廉价设备消亡** — AI在消灭廉价工作岗位的同时，也在消灭廉价设备

---

## 根因

HBM利润率远超消费级内存，厂商有强烈动机优先供货数据中心。内存厂商从历史中学到的教训是"宁可产能不足也不要过度扩张"，意味着短缺将持续数年。

---

*来源: memory/2026-05-23-1101.md (Karpathy RSS日报)*

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
