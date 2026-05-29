---
pageType: entity
entityType: task
id: entity.task.tradingagents-tushare
updatedAt: "2026-05-29"
---

# TradingAgents tushare数据支持

> entity_type: task

**类型:** Task  
**ID:** `todo_tradingagents_tushare`  
**状态:** pending  
**优先级:** medium  
**来源:** ToDo创建

---

## 任务描述

增强TradingAgents支持A股数据源，解决Yahoo Finance对A股支持弱的问题

---

## 解决方案

新增 `tushare_tools.py` 封装数据获取，通过格式适配层转换

---

## 关键设计

| 设计点 | 说明 |
|--------|------|
| 格式适配层 | tushare日线 → Yahoo Finance格式 |
| 缓存策略 | 日线1天 / 财务7天 |
| Fallback | tushare不可用时降级Yahoo Finance |

---

## 范围

数据层增强，**不修改框架源码**

---

*来源: memory/2026-05-08-tushare-integration.md*