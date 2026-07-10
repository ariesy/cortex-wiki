---
pageType: entity
id: entity.bash-heredoc-fstring-cron-bug
title: Bash heredoc f-string 沉默 bug
entityType: concept
aliases:
  - cron bash heredoc bug pattern
updatedAt: 2026-07-06T13:24:25.000Z
status: active
claims:
  - id: claim.bash-heredoc-fstring.pattern
    text: "Bash heredoc 内 Python f-string {VAR} 不会展开为 bash 变量，Python 执行时 NameError。正确做法是 bash heredoc 内用 $VAR 展开，让 Python 看到最终字符串。"
    status: supported
    confidence: 0.98
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-06-3bcca33e
        weight: 0.98
  - id: claim.bash-heredoc-fstring.silent-birth
    text: "沉默 bug 诞生路径：Sprint 5 写 cron 用时测试过 Step 1 但未完整 DRY-RUN 全流程 -> 配 schedule -> 32 天无人触发 -> 第一次真触发全部 crash -> cron log 只显示 header 误判 idle。教训：cron script 必须 DRY-RUN 至少 1 次完整流程才能 commit。"
    status: supported
    confidence: 0.95
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-06-3bcca33e
        weight: 0.95
---
# Bash heredoc f-string 沉默 bug

tdx-chronos Sprint 9 期间发现的系统性 cron bug 模式。

## Bug 模式
- `<< EOF`（无引号）: bash 展开 `$VAR` `$(cmd)` 
- `<< 'EOF'`（带引号）: bash 不展开，Python 看到字面 `$VAR`
- **不能混用**: heredoc 内 Python f-string `f"{$VAR}"` 永远错
- 正确做法: bash heredoc 内用 `"$VAR"` 让 bash 展开 → Python 看到 final string

## 2016-07-06 发现 & 修复
主人下指令 debug daily_incr 失败 → 系统性扫描 4 个 cron 脚本 → 修复 6 处 bug
- 3 cron jobs 32 天从未真跑过
- 全部修复后 3 个 cron 首次全部跑通

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
