---
pageType: entity
id: entity.bug.mx-data-cron-octal-bug
title: "mx-data cron 脚本 bash 八进制陷阱（08: value too great for base）"
entityType: concept
aliases:
  - bash 08 八进制陷阱
  - value too great for base (error token is "08")
  - mx-data-cron.sh exit=2
  - 10# 强制十进制
tags: [bug, bash, cron, mx-data, 定时任务, 数值解析]
updatedAt: "2026-08-16"
status: resolved
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-16-0812-0eba9729
claims:
  - id: claim.mxdata-cron-octal.symptom
    text: "症状：定时任务「mx-data 异步数据获取」在 2026-08-16 08:00 UTC 运行失败（exit=2），输出末尾连续三条报错：scripts/mx-data-cron.sh: line 13 `08: value too great for base (error token is \"08\")`、line 15 `[: -gt: unary operator expected`、line 20 `printf: 08: invalid octal number`。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0812-0eba9729
        weight: 0.9
  - id: claim.mxdata-cron-octal.rootcause
    text: "根因：bash 经典八进制陷阱。`date -u +%H` 在 8 点整返回 `08`，bash 算术中 0 开头的数字按八进制解析，而 8 不是合法八进制位，导致三处连环报错：line 13 `BATCH=$((UTC_HOUR / 2 + 1))` 报 value too great for base 使 BATCH 变空 → line 15 `[ $BATCH -gt 12 ]` 因空值报 unary operator expected → line 20 `printf '%02d' $UTC_HOUR` 报 invalid octal number。此前未触发是因为奇数小时（07/09）或 ≤06 的偶数小时恰好是合法八进制。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: source-code
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0812-0eba9729
        weight: 0.85
  - id: claim.mxdata-cron-octal.fix
    text: "修复（scripts/mx-data-cron.sh 两处）：`BATCH=$((10#$UTC_HOUR / 2 + 1))` 强制按十进制解析；`LOG_FILE=...$(printf '%02d' $((10#$UTC_HOUR))).log` 同样显式转十进制。验证：语法检查通过；模拟 08 点场景得到 BATCH=5、日志名 mx-job-08.log、正常执行不跳过，三处报错全部消除；下一步整点（10:00 UTC）自动按新脚本运行，无需重启服务。"
    status: fixed
    confidence: 0.9
    evidence:
      - kind: source-code
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0812-0eba9729
        weight: 0.85
  - id: claim.mxdata-cron-octal.generalization
    text: "可复用经验：任何 cron 脚本中用 `date +%H`/`%M`/`%S` 等零填充数字参与 shell 算术或 printf 的地方，都应写成 `10#${VAR}` 显式十进制，否则在 08、09 两个小时/分钟/秒进位会随机炸。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0812-0eba9729
        weight: 0.75
---

# mx-data cron 脚本 bash 八进制陷阱（08: value too great for base）

## 一句话

`date -u +%H` 在 8 点返回 `08`，被 bash 当八进制解析 → 8 非法 → 三行连环报错 → 定时任务 exit=2。

## 报错链

```bash
# line 13
BATCH=$((UTC_HOUR / 2 + 1))      # 08: value too great for base，BATCH 变空
# line 15
[ $BATCH -gt 12 ]                # [: -gt: unary operator expected（空值连锁）
# line 20
printf '%02d' $UTC_HOUR          # printf: 08: invalid octal number
```

## 修复

```bash
BATCH=$((10#$UTC_HOUR / 2 + 1))
LOG_FILE=...$(printf '%02d' $((10#$UTC_HOUR))).log
```

`10#` 前缀强制十进制解析。验证结果：08 点场景 → `BATCH=5`、日志 `mx-job-08.log`、不跳过。

## 为什么之前没炸

只有 **08 和 09** 两个零填充字符串在八进制下不合法（8、9 不是八进制位）。奇数小时 `07`/`09` 路径不同，≤`06` 的偶数小时 `0x` 是合法八进制，因此长期潜伏。

## 相关

- [[mx-data-null-notnull-crash]] — 同一任务（mx-data 异步数据获取）的另一类崩溃
- [[cron-notify-通知包装机制]] — 本次靠 cron-notify 报错才发现
- [[bash-heredoc-fstring-cron-bug]] — 同类 bash/cron 陷阱

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-16-0812](../sources/bridge-workspace-142ea9a2-memory-2026-08-16-0812-0eba9729.md)
<!-- openclaw:wiki:related:end -->
