---
pageType: entity
entityType: bug
id: entity.bug.minimax-oauth
updatedAt: "2026-05-29"
relationships:
  - targetId: entity.project.minimax-oauth
    targetTitle: "minimax-oauth"
    kind: affects
    weight: 0.8
sourceIds:
  -  MEMORY.md


---


# MiniMax国内OAuth配置问题

> entity_type: bug

**类型:** Bug  
**ID:** `bug_minimax_oauth`  
**状态:** identified（需进一步排查）  
**来源:** MEMORY.md

---


## 问题描述

国内服务器调用MiniMax API时出现认证错误。

---

## 可能原因

大陆服务器访问 `api.minimax.io` 需要特殊配置或走国内专属入口。

---

## 状态

问题已识别，需要进一步排查网络和认证配置。

---

*来源: MEMORY.md*

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [MiniMax Anthropic-compatible streaming 泄漏思维链](minimax-anthropic-streaming-bug.md)

### Related Pages

- [daily-questions多轮对话失效Bug](daily-questions-deliver-mode.md)
- [daily-questions定时任务跳过Bug](daily-questions-cron-skip.md)
- [MOBI格式字体大小48px硬限制](ebook-mobi-font-limit.md)
- [payslip任务crontab路径错误](payslip-crontab-path.md)
<!-- openclaw:wiki:related:end -->
