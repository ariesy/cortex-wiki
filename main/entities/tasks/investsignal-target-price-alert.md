# InvestSignal目标价预警优化

> entity_type: task

**类型:** Task  
**ID:** `todo_investsignal_target_price_alert`  
**状态:** pending  
**优先级:** medium  
**预计工时:** 5h  
**来源:** ToDo创建

---

## 任务描述

优化InvestSignal观察报告，增加目标价预警功能（突破/接近/安全三档）

---

## 实施步骤

| Step | 内容 |
|------|------|
| 1 | 数据采集层：新增 `analyst_target_prices` 表和 tushare 采集器 |
| 2 | 报告展示层：新增 `_format_target_price_dimension()` |
| 3 | 预警标签层：增加 🚀突破 / ⚠️接近 / ✅安全 标签 |

---

## 修改文件

- `signal_dao.py`
- `collector/`
- `scheduler/`
- `formatter.py`
- `reporter.py`

---

*来源: memory/2026-05-08-tushare-integration.md*