---
pageType: entity
id: entity.bug.investsignal-weekly-data-anomaly
title: InvestSignal 周报数据异常（2026-04-27 周期）
entityType: bug
aliases:
  - InvestSignal 周报数据缺失
  - 北向资金量级异常
updatedAt: 2026-08-12T01:11:30.520Z
status: identified
claims:
  - id: claim.investsignal-weekly.data-broken
    text: 2026-04-21~04-27 周期的 InvestSignal
      周报数据链路异常：主要指数行情显示「行情数据获取中...」为空值，北向资金净流入输出 34124151亿 这种明显失真量级，观察列表标的多为「⚪
      无法分析 / 置信度 0%」，报告名存实亡。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-30-investsignal-weekly-3b85963b
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2.memory-2026-04-30-investsignal-weekly-3b85963b.md
relationships:
  - targetId: entity.concept.investment-push-channels
    targetTitle: 投资信息推送渠道现状
    kind: related-to
    weight: 0.5
---

# InvestSignal 周报数据异常（2026-04-27 周期）

2026-04-30 收到周报推送时暴露的数据链路问题：数据缺失被静默降级为占位符，而非报错。

## 症状

| 栏目 | 输出 |
|------|------|
| 主要指数表现 | 「行情数据获取中...」（空值） |
| 资金流向 | 北向资金净流入 `34124151亿`（量级失真） |
| 观察列表分析 | 标的普遍「⚪ 无法分析 / 置信度 0%」 |
| 重要资讯回顾 | 「本周暂无重要资讯」 |

## 影响

周报的「数据完整性: 观察列表数据完整」结论与各标的实际无法分析相矛盾，报告会被当成有效信号误读，需先修数据源与字段校验。

## Related
- [投资信息推送渠道现状](投资信息推送渠道.md)

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->

---

## 2026-08-12 延伸：MX_APIKEY 在 cron 环境下缺失（已修复）

同一「数据被静默置空」问题的第二例，根因与 4 月周期同源：**取数密钥缺失后被降级为占位符**，而非报错。

| 环节 | 事实 |
|------|------|
| 症状 | 周报「MX_APIKEY 未配置」累计 39 次、「未设置 API 密钥」累计 210 次；利润表/资产负债表全部失败 |
| 起点 | 2026-06-30 起持续存在（9 次周报运行），非近期改动导致 |
| 根因 | `MX_APIKEY` 仅写在 `~/.bashrc`（133-134 行重复）与 `~/.profile`，cron 的非交互 shell 不加载；只有 `mx-data-cron.sh`（3/22, commit 0ce0d96）做了 `source ~/.profile`，`weekly_report.sh` 自 3/18 创建起从未加载 |
| 修复（方案 A） | ① `.env` 追加 47 字符 `MX_APIKEY`（备份 `.env.bak.20260812`）；② `.env.example` 补模板条目；③ 4 个定时脚本统一加 `set -a; source .env; set +a`：`weekly_report.sh` / `etf_scale_daily.sh` / `capital_flow_daily.sh` / `financial_report_collect.sh` |
| 验证 | 干净环境冒烟测试 ETF 净值 OK；完整周报 `success=True`（`send_to_feishu=False`），产出 `report_20260812_011015.md`；错误 39→0、210→0，财务数据从全失败变为完整显示 |

**遗留**（非 key 问题）：限流 `status=115` 出现 150 次（并发实例 + `mx-data-cron` 每 2h 任务叠加）；宏观利率/汇率为 0（macro collector 数据不足）；`news_dao` 未配置（情绪面数据不足）；指数接口 `000001.SH` 返回空。

**教训**：
- `pkill -f` 会匹配到自身命令行导致自杀（SIGTERM）——匹配模式需排除自身 PID。
- exec timeout 会误杀长任务：外层 kill 后子进程仍存活，清理要按进程组。
- 验证周报不要直接跑 `weekly_report.sh`（写死 `send_to_feishu=True`），应直接调 `reporter.generate_report(save=True, send_to_feishu=False)`。
- 密钥类配置一律进 `.env` 并由脚本显式 source，**不要依赖 rc 文件**——cron/系统服务都不读 rc。
