---
pageType: entity
entityType: bug
id: entity.bug.daily-questions-cron-skip
updatedAt: "2026-05-29"
relationships:
  - targetId: entity.project.daily-questions-cron-skip
    targetTitle: "daily-questions-cron-skip"
    kind: affects
    weight: 0.8
---


# daily-questions定时任务跳过Bug

> entity_type: bug

**类型:** Bug  
**ID:** `bug_daily_questions_cron_skip`  
**状态:** fixed ✅  
**修复commit:** 7c10724  
**日期:** 2026-03-25  
**来源:** MEMORY.md

---


## 症状

每天20:00的每日问答未发送，但gateway实际在运行。

---

## 根因

`systemctl --user` 在cron环境中返回 `Runtime: unknown`，grep 匹配失败导致误判。

---

## 修复方案

改用 `ss -ltn | grep ":18789"` 直接检查端口监听状态，不依赖 systemctl。

---

## 影响范围

2026-03-22 至 2026-03-24 每日任务被跳过。

---

*来源: MEMORY.md Bug修复记录*