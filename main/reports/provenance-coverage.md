---
pageType: report
id: report.provenance-coverage
title: Provenance Coverage
status: active
updatedAt: 2026-10-30T13:06:57.301Z
---

# Provenance Coverage

## Generated
<!-- openclaw:wiki:provenance-coverage:start -->
- Evidence entries: 648
- Claims missing evidence: 29

### Evidence Classes
- wiki-source: 299
- entity-summary: 81
- report: 57
- financial-data: 38
- research-report: 21
- memory-bridge: 19
- web: 16
- analysis: 12
- source: 12
- synthesis-summary: 12
- financial_data: 8
- news: 8
- industry-data: 7
- policy: 7
- technical-analysis: 7
- market_data: 5
- data: 3
- debugging-report: 3
- valuation-data: 3
- decision-framework: 2
- fund-holding: 2
- industry-news: 2
- valuation: 2
- valuation-model: 2
- analyst_estimate: 1
- analyst-analysis: 1
- analyst-debate: 1
- analyst-estimate: 1
- analyst-report: 1
- financial-analysis: 1
- fund-flow-data: 1
- index-methodology: 1
- kline-data: 1
- management: 1
- market-flow: 1
- multi-agent-decision: 1
- news-data: 1
- ownership: 1
- performance-data: 1
- runtime-config: 1
- stock-research-engine: 1
- synthesis: 1
- tdx-chronos: 1
- wiki-creation: 1

### Top Evidence Sources
- source.entities.investments: 68
- source.research.兴业银行: 15
- source.bridge.workspace-142ea9a2.memory-2026-05-29-memory-sources: 12
- research/小米_1810.HK/2026-07-17_tradingagents: 10
- source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4: 10
- source.syntheses.factor-etf-comparison-2026-06-25: 10
- source.bridge.workspace-142ea9a2.memory-2026-05-05-investment-preferences-update-a4119225: 9
- source.bridge.workspace-142ea9a2.memory-2026-05-07-ima-sync-debug-fix-0a6e63bb: 8
- source.bridge.workspace-142ea9a2.memory-2026-07-02-1322-d13a3e17: 8
- source.research.中信证券: 8
- stock-research-engine:jingneng-power:2026-06-14: 8
- /app/ai-berkshire/reports/泡泡玛特/泡泡玛特-综合投资研究报告-20260803.md: 7
- source.bridge.workspace-142ea9a2.memory-2026-05-07-0055-6ee63358: 7
- source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f: 7
- /app/ai-berkshire/reports/宋城演艺/宋城演艺投资研究报告.md: 6
- inline: 6
- /app/ai-berkshire/reports/工商银行/icbc-601398-investment-research-20260908.md: 5
- /app/ai-berkshire/reports/平安集团/investment-research-2026-08.md: 5
- /app/TradingAgents/reports/300144.SZ_20260902_031218/complete_report.md: 5
- policy:国能发科技〔2026〕34号: 5

### Missing Evidence
- [daily_incr 双调度器并发冲突（tdx 数据快照损坏）](../entities/daily-incr-dual-scheduler-conflict.md): `claim.daily-incr.symptom`: daily 增量报错表现为 tdxgp `[Errno 2] No such file`、`Size mismatch` 交错写入损坏、tdxfin.zip 多出 2752512 bytes 导致 unzip 失败；后果为股本 records=0、财务 parsed=0。
- [daily_incr 双调度器并发冲突（tdx 数据快照损坏）](../entities/daily-incr-dual-scheduler-conflict.md): `claim.daily-incr.rootcause`: 根因是双调度器并发冲突：系统 crontab 中 daily_incr（`30 9 * * 1-5` UTC = 17:30 CST）与 OpenClaw cron 的 tdx-daily-incr（`30 17 * * 1-5` Asia/Shanghai）在同一时刻触发，两个进程并发写同一 snapshot 目录。
- [daily_incr 双调度器并发冲突（tdx 数据快照损坏）](../entities/daily-incr-dual-scheduler-conflict.md): `claim.daily-incr.fix`: 修复措施：禁用系统 crontab 中重复的 daily_incr 行（保留带状态追踪和飞书 delivery 的 OpenClaw cron）；daily_incr.sh 增加 flock 互斥锁作为双保险；重新下载 tdxgp.zip（739MB）与 tdxfin.zip（537MB）并重跑解析。
- [daily_incr 双调度器并发冲突（tdx 数据快照损坏）](../entities/daily-incr-dual-scheduler-conflict.md): `claim.daily-incr.result`: 修复后数据恢复：股本 ok=8,534、records=134,838,102；财务 skipped=242 parsed=18；K线 12,324 与指数 28,119 未受影响；download_log 当天 6 行全部修正为 success。
- [daily_incr 双调度器并发冲突（tdx 数据快照损坏）](../entities/daily-incr-dual-scheduler-conflict.md): `claim.daily-incr.weekly-dedup`: weekly_sync / weekly_doctor 同样存在双调度：系统 crontab 周六 18:00/19:00 UTC（= 周日 02:00/03:00 CST），OpenClaw cron 周日 18:00/19:00 UTC（= 周一 02:00/03:00 CST），两者错一天导致每周各跑两次（时间错开不会写坏数据）；用户确认后按同样方式去重：保留 OpenClaw cron 并把时间修正为脚本注释声明的周日 02:00/03:00 CST，注释掉系统 crontab 行。
- [daily_stock_analysis PR #2154 / Issue #2153 监控任务](../entities/daily-stock-analysis-pr-issue-monitor.md): `claim.dsa-monitor.branch-push`: feature/tdx 分支 9f88df83..284b61c8 已推送到 origin，含本地 8 个提交（场景 1+2 修复、历史区块下移、merge）。
- [daily_stock_analysis PR #2154 / Issue #2153 监控任务](../entities/daily-stock-analysis-pr-issue-monitor.md): `claim.dsa-monitor.pr-comment`: 已在 ZhuLinsen/daily_stock_analysis PR #2154 发布维护者回复（issuecomment-5199163878）：OR-COR-80e5aa42 不可恢复分支补 clearPersistedScreenTask()；OR-COR-3513bd9a 改为历史条目自带筛选条件（策略中文名 + 市场 + 返回数量）而非清除持久化状态；附两条回归测试与验证结果（28 测试通过、build 通过）。
- [daily_stock_analysis PR #2154 / Issue #2153 监控任务](../entities/daily-stock-analysis-pr-issue-monitor.md): `claim.dsa-monitor.cron`: 新建 cron 任务 github-pr-issue-monitor-dsa（ID c7095326，`30 2 * * *` Asia/Shanghai = 每天 02:30 CST），监控 ZhuLinsen/daily_stock_analysis 的 PR #2154 与 Issue #2153，delivery 到用户飞书私聊。
- [daily_stock_analysis PR #2154 / Issue #2153 监控任务](../entities/daily-stock-analysis-pr-issue-monitor.md): `claim.dsa-monitor.script-behavior`: 监控脚本参考现有 check_updates.sh 模式编写，首次运行输出摘要，后续无更新时输出 NO_REPLY 抑制重复通知。
- [Forward PE（远期市盈率）](../entities/forward-pe.md): `claim.forward-pe.definition`: Forward PE（远期市盈率）= 当前股价 ÷ 未来12个月（或下一财年）预期每股收益，也可表述为总市值 ÷ 预期净利润；分母使用分析师预测盈利，而非已实现盈利。
- [Forward PE（远期市盈率）](../entities/forward-pe.md): `claim.forward-pe.vs-trailing`: Trailing PE 使用过去已实现盈利（TTM 或上一年报净利润），Forward PE 使用分析师预测的明年盈利；例：股价100元、去年EPS 5元 → Trailing PE 20倍；预测明年EPS 8元 → Forward PE 12.5倍。
- [Forward PE（远期市盈率）](../entities/forward-pe.md): `claim.forward-pe.why-use`: 使用 Forward PE 的原因：更能反映成长性（高增长公司用历史盈利显得贵）；常用于跨期比较与 PEG 分析（PEG = Forward PE ÷ 预期增速）；港美股研报中的 PE 多默认指 Forward PE。
- [Forward PE（远期市盈率）](../entities/forward-pe.md): `claim.forward-pe.risks`: Forward PE 的风险：分母为预测值，分析师可能过于乐观，盈利不及预期时估值被动抬高；强周期股（券商、航运、半导体）在盈利顶部 Forward PE 最低，反而是危险信号（低 PE 陷阱）；不同数据源对 forward 口径定义不同（未来12个月 vs 下一财年），横向比较需确认口径。
- [Forward PE（远期市盈率）](../entities/forward-pe.md): `claim.forward-pe.a-share-analogy`: A股的“动态市盈率”有时指用预测或年化盈利计算的市盈率，与港美股 Forward PE 概念相近但不完全一致，需留意行情软件的计算口径。
- [OpenCode 权限规则顺序 Bug（reports 写入被 auto-reject）](../entities/opencode-permission-rule-order-bug.md): `claim.opencode-perm.symptom`: AI Berkshire 分析进程正常结束但报告未写入：报告写入被权限拦截，非交互模式下权限询问被 auto-reject。
- [OpenCode 权限规则顺序 Bug（reports 写入被 auto-reject）](../entities/opencode-permission-rule-order-bug.md): `claim.opencode-perm.rootcause`: 根因是 opencode.json 权限规则顺序问题：`edit: "*": "ask"` 规则先于 `reports/**/*.md: "allow"` 匹配，导致报告写入落入 ask；非交互模式下无法应答即 auto-reject。ACP 子代理超时也是同一原因（权限询问无法应答）。
- [OpenCode 权限规则顺序 Bug（reports 写入被 auto-reject）](../entities/opencode-permission-rule-order-bug.md): `claim.opencode-perm.workaround`: 临时规避：用 `--dangerously-skip-permissions` 参数重跑（不修改项目文件），分析即可成功完成并生成报告。
- [OpenCode 权限规则顺序 Bug（reports 写入被 auto-reject）](../entities/opencode-permission-rule-order-bug.md): `claim.opencode-perm.lesson`: 教训：权限规则按顺序匹配，最具体的 allow 规则必须放在宽泛的 `"*": "ask"` 之前；非交互/子代理场景下任何落到 ask 的规则都等同于拒绝。
- [Wiki lint 批量修复（613 → 7 警告）](../entities/wiki-lint-batch-fix-2026-08-05.md): `claim.wiki-lint-batch.conclusion`: 2026-08-05 wiki lint 批量修复完成：613 条警告降至 7 条、0 错误；剩余 7 条均为内容性标记（contradictions / open questions），属知识管理标注而非格式错误，保留合理。
- [Wiki lint 批量修复（613 → 7 警告）](../entities/wiki-lint-batch-fix-2026-08-05.md): `claim.wiki-lint-batch.broken-wikilink`: 断链 Broken wikilink 41 → 0：修正路径错误（`entities/syntheses/` ↔ `syntheses/entities/` 互指）、按标题匹配改为文件路径（如中宠/乖宝）、不存在的目标改为纯文本。
- [Wiki lint 批量修复（613 → 7 警告）](../entities/wiki-lint-batch-fix-2026-08-05.md): `claim.wiki-lint-batch.sourceid`: 缺 sourceIds 119 → 0：通过映射 AI Berkshire 报告路径、并从 claims evidence 中的 sourceId 反查 sources/ 补齐。
- [Wiki lint 批量修复（613 → 7 警告）](../entities/wiki-lint-batch-fix-2026-08-05.md): `claim.wiki-lint-batch.claims`: 约 40 条 claim 缺证据（`evidence: []`）已补 evidence；12 条 claim 竞争变体（两页同 id 不同文本，如小米 death-cross）与 1 条低置信度 claim 一并处理。
- [Wiki lint 批量修复（613 → 7 警告）](../entities/wiki-lint-batch-fix-2026-08-05.md): `claim.wiki-lint-batch.yaml-errors`: 最终 2 个 YAML 解析错误根因：ai-berkshire 框架文件删除 claim 后留下残留块；上证50AH 的 sourceId 值不合法。修复后错误归零。
- [恒生科技ETF (513180)](../entities/恒生科技ETF-513180.md): `claim.hstech.index-profile`: 恒生科技指数（HSTECH）为香港上市 30 家科技主题公司的流通市值加权指数，覆盖互联网、AI、芯片、新能源汽车；2020 年 7 月推出，基日 2014-12-31、基值 3000 点。
- [恒生科技ETF (513180)](../entities/恒生科技ETF-513180.md): `claim.hstech.concentration`: 恒生科技指数前十大权重合计约 69%，单一成分股权重上限 8%；行业分布约为资讯科技 45%、非必需消费 45%、医疗保健 5%。
- [恒生科技ETF (513180)](../entities/恒生科技ETF-513180.md): `claim.hstech.history`: 恒生科技指数历史区间：2021-02 高点约 10902 点，2022-10 低点约 2800 点，2024 年反弹至约 6000 点，2026-02 在 4800-5000 区间筑底。
- [恒生科技ETF (513180)](../entities/恒生科技ETF-513180.md): `claim.hstech.rebalance-2026-06`: 恒生科技指数 2026 年 6 月调整窗口：拟纳入 MiniMax（智谱AI，市值超 777 亿港元），剔除金蝶国际（约 455 亿警戒线以下）与金山软件。
- [恒生科技ETF (513180)](../entities/恒生科技ETF-513180.md): `claim.hstech.sentiment-2026-05`: 2026-05 判断：恒生科技处于预期驱动向业绩验证过渡阶段，5 月 4 日指数大涨 3.22% 突破 5000 点是政策、产业、资金三重共振的结果，而非单纯超跌反弹。
- [恒生科技ETF (513180)](../entities/恒生科技ETF-513180.md): `claim.hstech.premium-channel`: 513180 溢价率 0.39%，超过历史 78% 时间，走港股通渠道购买更划算。
<!-- openclaw:wiki:provenance-coverage:end -->
