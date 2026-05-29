---
pageType: entity
entityType: bug
id: entity.bug.payslip-crontab-path
updatedAt: "2026-05-29"
---

# payslip任务crontab路径错误

> entity_type: bug

**类型:** Bug  
**ID:** `bug_payslip_crontab_path`  
**状态:** fixed ✅  
**日期:** 2026-04-03  
**来源:** MEMORY.md

---

## 症状

cron重定向目录与脚本内DATA_DIR不一致，shell在脚本运行前就失败。

---

## 根因

| 位置 | 路径 |
|------|------|
| crontab | `data/payslip/cron.log`（无i） |
| 脚本内 | `data/payslips`（有i） |

---

## 教训

cron重定向在脚本执行前就失败，脚本内的 `mkdir -p` 无法补救。

**创建cron任务时，确保外层重定向目录存在。**

---

*来源: MEMORY.md Bug修复记录*