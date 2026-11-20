---
pageType: entity
id: entity.bug.scheduled-script-exit143-sigterm
title: "定时脚本启动即 exit 143（SIGTERM）排查"
entityType: bug
aliases:
  - 定时脚本 exit 143
  - 脚本启动即被 kill
  - cron 任务被 SIGTERM
tags: [bug, cron, shell, bash, sigterm, exit-143]
updatedAt: "2026-08-16"
status: open
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-16-0042-bd1a9572
claims:
  - id: claim.exit143.symptom
    text: "症状：定时/验证脚本启动后立刻以 143（SIGTERM）退出，日志无业务输出，连 `verify2.log` 这类启动即写的日志文件都没生成，说明失败发生在脚本主体执行之前（环境加载阶段）。"
    status: observed
    confidence: 0.7
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0042-bd1a9572
        weight: 0.7
  - id: claim.exit143.verify-pattern
    text: "验证规避：嵌套引号会导致 `bash -lc \"...\"` 启动即失败，改为先把验证逻辑写成临时脚本文件再执行；长任务验证要轮询日志等待完成，不要靠 exec timeout 硬杀（外层 kill 后子进程仍可能存活）。"
    status: observed
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0042-bd1a9572
        weight: 0.8
  - id: claim.exit143.secret-effect
    text: "同批次对照证据：脚本加 `set -a; source .env; set +a` 导出密钥后，报错从「MX_APIKEY 未配置」变成「API返回错误状态: 115（限流）」与解析类错误，证明 API 已连通，剩余问题是上游限流（并发 + 每 2h 任务叠加）而非密钥。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0042-bd1a9572
        weight: 0.8
---

# 定时脚本启动即 exit 143（SIGTERM）

## 症状

脚本启动后无任何业务输出即以 `143`（SIGTERM）退出；连启动即落盘的日志文件都没生成 → 失败发生在脚本主体执行前。

## 排查顺序

1. 用 `bash -x script.sh` 定位最后执行到哪一行
2. 在干净环境 `env -i PATH=... bash script.sh` 复现（排除 rc 文件干扰）
3. 检查环境加载阶段：变量名与 shell 内建/信号名冲突、`source` 的 .env 里含破坏语法的内容、shebang 与解释器不一致
4. 检查是否被外部 `pkill -f` / exec timeout 误杀（按进程组清理，注意 `pkill -f` 会匹配自身命令行）

## 验证纪律

- 不要把复杂逻辑塞进 `bash -lc "..."`（嵌套引号极易启动失败），写临时脚本文件
- 长任务用轮询日志等待，不要用外层 timeout 硬杀

## 关联

- 密钥生效判据：`MX_APIKEY 未配置` 消失、改报上游 115 限流 → 见 [cron 环境变量/密钥缺失](./cron-env-secret-missing.md)

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-16-0042](../sources/bridge-workspace-142ea9a2-memory-2026-08-16-0042-bd1a9572.md)
<!-- openclaw:wiki:related:end -->
