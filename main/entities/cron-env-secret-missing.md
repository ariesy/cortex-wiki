---
pageType: entity
id: entity.concept.cron-env-secret-missing
title: cron 环境变量/密钥缺失（rc 文件不被加载）
entityType: concept
aliases:
  - MX_APIKEY 未配置
  - cron 里读不到 .bashrc
  - 定时任务密钥缺失
updatedAt: 2026-08-12T01:11:30.520Z
status: active
claims:
  - id: claim.cron-env.rc-not-loaded
    text: cron 使用非交互 shell，不加载 ~/.bashrc / ~/.profile，因此只写在 rc 文件里的密钥（如 MX_APIKEY）在定时任务中恒为未配置；症状是脚本不报错而是静默降级——某周报 9 次运行累计 39 次「MX_APIKEY 未配置」、210 次「未设置API密钥」。
    status: supported
    confidence: 0.95
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-12-e90b359a
        weight: 0.95
  - id: claim.cron-env.fix-pattern
    text: 修复模式：密钥集中放项目 .env（示例文件补模板），所有定时脚本开头统一 `set -a; source .env; set +a` 导出；不要依赖 rc 文件，也不要只修一个脚本（本项目 4 个脚本：weekly_report.sh / etf_scale_daily.sh / capital_flow_daily.sh / financial_report_collect.sh 需同时改）。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-12-e90b359a
        weight: 0.9
  - id: claim.cron-env.verify
    text: 验证方式：干净环境（env -i 或新 shell）冒烟跑一次采集脚本，并直接调 reporter.generate_report(save=True, send_to_feishu=False) 生成完整周报，确认密钥类错误计数归零；不要直接跑写死 send_to_feishu=True 的入口脚本。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-12-e90b359a
        weight: 0.85
  - id: claim.cron-env.kill-gotchas
    text: 排查期踩到的两个工具坑：`pkill -f` 会匹配到自身命令行导致自杀（SIGTERM）；exec timeout 会误杀长任务，外层 kill 后子进程仍存活，需按进程组清理。
    status: observed
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-12-e90b359a
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-08-12-e90b359a.md
relationships:
  - targetId: entity.bug.investsignal-weekly-data-anomaly
    targetTitle: "InvestSignal 周报数据异常（2026-04-27 周期）"
    kind: related-to
    weight: 0.6
  - targetId: entity.project.blogtrottr-rss-digest
    targetTitle: "Blogtrottr RSS 邮件订阅日报"
    kind: same-class-bug
    weight: 0.35
---

# cron 环境变量/密钥缺失（rc 文件不被加载）

**一句话**：密钥写在 `~/.bashrc` 里，cron 永远读不到；脚本不报错，只是把数据静默置空。

## 症状

- 日志里高频刷「XXX 未配置」「未设置API密钥」，但任务退出码正常。
- 依赖该密钥的数据源（财务利润表/资产负债表、情绪面）整块失败或长期为空。
- 持续时间长却无人发现——因为失败不体现在报表标题上。

## 本次案例（2026-08-12，InvestSignal 周报）

`MX_APIKEY` 仅存在于 `~/.bashrc`（133-134 行重复）与 `~/.profile`；只有 `mx-data-cron.sh`（commit 0ce0d96, 3/22）做了 `source ~/.profile`，`weekly_report.sh` 自 3/18 起从未加载。问题自 2026-06-30 起存在，跨 9 次周报运行。

## 修复清单

| 步骤 | 内容 |
|------|------|
| 1 | `.env` 追加密钥（备份 `.env.bak.YYYYMMDD`，本项目 47 字符） |
| 2 | `.env.example` 补模板条目，避免新环境漏配 |
| 3 | 每个定时脚本头部加 `set -a; source .env; set +a` |
| 4 | 干净环境冒烟 + 完整产出验证，错误计数归零 |

## 验证纪律

- 别直接跑生产入口脚本（可能写死 `send_to_feishu=True` 真的推送出去）。
- 用 reporter 层函数生成但不发送：`generate_report(save=True, send_to_feishu=False)`。

## 相关

- [[InvestSignal周报数据异常2026-04-27]] — 同一「静默降级为占位符」模式的另一个出处

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
