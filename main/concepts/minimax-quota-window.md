---
pageType: concept
id: concept.minimax-quota-window
title: "MiniMaxQuota窗口时间不一致"
updatedAt: "2026-05-29"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-04-29-mmx-quota-windows
---

# MiniMaxQuota窗口时间不一致

> entity_type: pattern

**类型:** Pattern  
**ID:** `pattern_minimax_quota_window`  
**来源:** mmx quota调查

---

## 问题描述

API对不同模型返回不同时间窗口，脚本直接透传没有说明：

| 模型类型 | 窗口时间 |
|----------|----------|
| 文本/编码模型 | **5小时**窗口 |
| 媒体生成模型 | **24小时**窗口 |

---

## 根因

API设计层面的差异，非脚本bug。

---

## 解决方案

输出时备注哪些是24h窗口模型，避免用户困惑。

---

*来源: memory/2026-04-29-mmx-quota-windows.md*

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
