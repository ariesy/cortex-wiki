# daily-questions多轮对话失效Bug

> --deliver模式是单次会话，不支持多轮对话，已修复

**类型:** Bug  
**ID:** `bug_daily_questions_deliver_mode`  
**状态:** fixed ✅  
**修复commit:** 5d61aee  
**日期:** 2026-03-25  
**来源:** MEMORY.md

---

## 症状

cron触发后用 `--deliver` 发送问题，用户回复后无agent处理。

---

## 根因

`--deliver` 是**单次会话模式**，不支持多轮对话。

---

## 修复方案

1. SKILL.md 重构为"单次发送全部6题 + 异步多轮回复"架构
2. cron发完卡片后写 `current_daily.json`，主agent读取该文件感知上下文
3. SOUL.md 增加群聊特殊规则：收到消息时检查 `current_daily.json`
4. `answered_questions.json` 改为新格式（含 id/answerText 字段）

---

*来源: MEMORY.md Bug修复记录*