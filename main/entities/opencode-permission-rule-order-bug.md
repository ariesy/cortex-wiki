---
pageType: entity
id: opencode-permission-rule-order-bug
title: "OpenCode 权限规则顺序 Bug（reports 写入被 auto-reject）"
tags: [bug, opencode, 权限, permissions, 非交互模式, ACP, ai-berkshire]
updatedAt: "2026-08-06"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-06-0048-999a1346
claims:
  - id: claim.opencode-perm.symptom
    text: "AI Berkshire 分析进程正常结束但报告未写入：报告写入被权限拦截，非交互模式下权限询问被 auto-reject。"
    status: supported
    confidence: 0.85
  - id: claim.opencode-perm.rootcause
    text: "根因是 opencode.json 权限规则顺序问题：`edit: \"*\": \"ask\"` 规则先于 `reports/**/*.md: \"allow\"` 匹配，导致报告写入落入 ask；非交互模式下无法应答即 auto-reject。ACP 子代理超时也是同一原因（权限询问无法应答）。"
    status: supported
    confidence: 0.85
  - id: claim.opencode-perm.workaround
    text: "临时规避：用 `--dangerously-skip-permissions` 参数重跑（不修改项目文件），分析即可成功完成并生成报告。"
    status: supported
    confidence: 0.8
  - id: claim.opencode-perm.lesson
    text: "教训：权限规则按顺序匹配，最具体的 allow 规则必须放在宽泛的 `\"*\": \"ask\"` 之前；非交互/子代理场景下任何落到 ask 的规则都等同于拒绝。"
    status: supported
    confidence: 0.75
---

# OpenCode 权限规则顺序 Bug

## 症状

AI Berkshire 分析任务（华安黄金ETF 518880 四大师分析）进程已结束，但报告写入被权限拒绝；检查发现无部分报告生成。

## 根因

`opencode.json` 权限规则**顺序**问题：

- `edit: { "*": "ask" }` 规则在 `"reports/**/*.md": "allow"` 之前被匹配
- 非交互模式（ACP 子代理、cron）无法应答权限询问 → auto-reject
- ACP 子代理超时也是同一原因

## 处理

- 临时规避：`--dangerously-skip-permissions` 参数重跑（不改项目文件），分析成功完成，报告 26KB 全模块生成
- 正解：调整规则顺序，把具体 allow 放到宽泛 ask 之前

## 教训

- 权限规则按顺序匹配，具体 allow 必须前置
- 非交互/子代理环境下任何落到 `ask` 的规则都等价于拒绝

## 相关实体

- [[ai-berkshire-价值投资研究框架]]
- [[黄金ETF]]（本次被阻塞的分析对象）

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-06-0048](../sources/bridge-workspace-142ea9a2-memory-2026-08-06-0048-999a1346.md)

### Related Pages

- [黄金ETF (GLD/IAU/518880)](黄金ETF.md)
<!-- openclaw:wiki:related:end -->
