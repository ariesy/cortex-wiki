---
pageType: entity
entityType: bug
id: entity.bug.payslip-crontab-path
updatedAt: "2026-05-29"
relationships:
  - targetId: entity.project.payslip-crontab-path
    targetTitle: "payslip-crontab-path"
    kind: affects
    weight: 0.8
sourceIds:
  -  MEMORY.md


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

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [daily-questions多轮对话失效Bug](daily-questions-deliver-mode.md)
- [daily-questions定时任务跳过Bug](daily-questions-cron-skip.md)
- [MiniMax国内OAuth配置问题](minimax-oauth.md)
- [MOBI格式字体大小48px硬限制](ebook-mobi-font-limit.md)
<!-- openclaw:wiki:related:end -->
