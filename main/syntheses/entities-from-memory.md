# Entities Wiki - Memory Source Consolidation

> 从 memory/*.md 和 ontology graph.jsonl 中提取的关键实体汇总，便于快速查询和关联检索。

**实体目录：** [投资](../entities/investments/) · [项目](../entities/projects/) · [任务](../entities/tasks/) · [概念](../entities/concepts/) · [Bug记录](../entities/bugs/) · [人物](../entities/persons/) · [文档](../entities/documents/) · [小说人物](../entities/people-fiction/) · [书籍](../entities/books/)

---

## 📈 投资实体 (Investments)

> [返回投资列表](../entities/investments/)

| ID | 名称 | 代码 | 市场 | 评级/结论 | 来源 |
|----|------|------|------|-----------|------|
| `stock_601088_shenhua` | 中国神华 | 601088 | A股 | ⭐⭐⭐⭐强烈推荐，股息4.9% | superresearch |
| `stock_9618_jd` | 京东集团 | 9618.HK | 港股 | 卖出(Underweight)，PE 7.5x | stock-research-engine |
| `stock_688008_lanqi` | 澜起科技 | 688008.SH | A股+港股 | 高弹性预期驱动 | stock-research-engine |
| `stock_09992_popmart` | 泡泡玛特 | 09992.HK | 港股 | 目标价HK$248-435 | 券商目标价汇总 |
| `etf_513180_hstech` | 华夏恒生科技ETF | 513180 | A股(QDII) | 低估值+高增长组合 | stock-research-engine |
| `etf_513050_china_internet` | 中概互联网ETF | 513050.SS | A股 | 目标1.27/1.31/1.46，止损1.19 | 4周研究汇总 |
| `stock_159995_chip_etf` | 华夏芯片ETF | 159995.SZ | A股 | 减持，RSI 71.88超买 | stock-research-engine |

---

## 🔧 项目/技能 (Projects & Skills)

> [返回项目列表](../entities/projects/)

| ID | 名称 | 类型 | 状态 | 说明 |
|----|------|------|------|------|
| `project_stock_research_engine` | stock-research-engine | Project | active | 多Agent股票分析框架 |
| `project_tradingagents` | tradingagents | Project | research | AI对冲基金模拟系统（14种大师Agent） |
| `skill_superresearch` | superresearch | Skill | active | 强制Phase流程的深度研究框架 |
| `skill_bilibili_all_in_one` | bilibili-all-in-one | Skill | active | B站上传技能，已配置账号 |
| `skill_ebook_manager` | ebook-manager | Skill | active | Calibre管理：搜索/元数据/导入/备份 |
| `skill_ebook_flashcard` | ebook-flashcard | Skill | active | 电子书→记忆卡PDF，用于Paperwhite |
| `skill_daily_questions` | daily-questions | Skill | active | 每日20:00问答群卡片 |
| `skill_mmx_cli` | mmx-cli | Skill | active | MiniMax额度查询工具 |
| `project_open_design` | open-design | Project | active | 开源设计工具，16种AI CLI |
| `project_guardians_eye` | 守护眼公众号 | Project | active | 防骗内容创作，WeChat订阅号 |
| `project_ai_news_phase2` | AI News Phase 2 | Project | blocked | Code review 6.5/10，4个CRITICAL/HIGH问题 |
| `project_deerflow_integration` | DeerFlow与OpenClaw集成 | Project | completed | 集成方案已完成 |

---

## 📋 任务 (Tasks)

> [返回任务列表](../entities/tasks/)

| ID | 名称 | 状态 | 优先级 | 说明 |
|----|------|------|--------|------|
| `todo_investsignal_target_price_alert` | InvestSignal目标价预警优化 | pending | medium | 5h工作量，三档预警 |
| `todo_tradingagents_tushare` | TradingAgents tushare数据支持 | pending | medium | A股数据层增强 |

---

## 🧠 概念/模式 (Concepts & Patterns)

> [返回概念列表](../entities/concepts/)

| ID | 名称 | 说明 |
|----|------|------|
| `concept_ai_hedge_fund_agent_styles` | AI对冲基金多Agent风格分类 | 14种投资大师Agent |
| `concept_hbm_memory_shortage` | AI内存短缺危机 | HBM挤压消费级产能 |
| `concept_warm_aging` | 养老防骗意识 | 老人理解诈骗但未必内化 |
| `concept_elderly_fraud_patterns` | 老人诈骗模式分类 | 健康养生馆/保健酒/百日灸等 |
| `concept_openai_threat_model` | Altman威胁模型论 | AI无情感，需设计层面嵌入价值观 |
| `pattern_lanqi_fake_report` | 澜起科技假研报识别特征 | 出货文特征：日期超前/数据夸张/无来源 |
| `pattern_ai_news_critical_bugs` | AI News Phase 2 Critical Bugs | 4个CRITICAL/HIGH问题自检清单 |
| `pattern_minimax_quota_window` | MiniMax窗口时间不一致 | API设计，文本5h/媒体24h |

---

## 🐛 Bug记录 (Bugs)

> [返回Bug列表](../entities/bugs/)

| ID | 名称 | 状态 | 说明 |
|----|------|------|------|
| `bug_bilibili_audio_uploader` | bilibili-api-python AudioUploader bug | known_issue | AttributeError |
| `bug_stubzero_google_cloud` | StubZero RCE漏洞 | CVE-2026-2031 | Google Cloud protobuf端点泄漏 |
| `bug_daily_questions_deliver_mode` | daily-questions多轮对话失效 | fixed ✅ | --deliver模式单次会话问题 |
| `bug_daily_questions_cron_skip` | daily-questions定时任务跳过 | fixed ✅ | systemctl检查失效 |
| `bug_payslip_crontab_path` | payslip路径错误 | fixed ✅ | crontab重定向目录不存在 |
| `bug_ebook_mobi_font_limit` | MOBI字体48px限制 | fixed ✅ | 改用PDF输出 |
| `bug_minimax_oauth` | MiniMax国内OAuth | identified | 大陆服务器认证问题 |

---

## 👤 人物 (Persons)

> [返回人物列表](../entities/persons/)

| ID | 名称 | 说明 |
|----|------|------|
| `person_zhu_kun` | 朱琨 | 主人，个人投资者 |
| `person_yao_wenhai` | 姚文海 | 配偶 |
| `person_zhu_lingxiao` | 朱凌霄 | 儿子，幼儿园 |
| `person_sam_altman` | Sam Altman | OpenAI CEO |
| `person_canaan` | 陆天一笑 | 主人飞书账号 |

---

## 📚 文档/笔记 (Documents)

> [返回文档列表](../entities/documents/)

| ID | 标题 | 类型 | 说明 |
|----|------|------|------|
| `note_investment_research_resources_v2` | 投资研究资源完整版 | Note | 12本书+4博客+5数据源 |
| `note_research_tracker_4week` | 4周研究跟踪汇总 | Note | 中概互联网ETF/泡泡玛特目标价 |
| `note_karpathy_rss_20260523` | Karpathy RSS 日报 | Note | HBM短缺/StubZero漏洞 |
| `paper_autonomous_research_agents_2026` | From Copilots to Colleagues | 学术论文 | L1-L5分类，当前前沿L4 |

---

## 📖 书籍/小说人物 (Books & Fiction)

> [返回书籍列表](../entities/books/) · [返回小说人物](../entities/people-fiction/)

| ID | 名称 | 类型 | 说明 |
|----|------|------|------|
| `book_five_dysfunctions` | The Five Dysfunctions of a Team | Book | Patrick Lencioni，团队领导力经典 |
| `people-fiction/five-dysfunctions-team` | 五种功能障碍团队 | Fiction | Kathryn/Jeff/Nick/Mikey等人物关系 |

---

## 🔗 关键关系 (Key Relationships)

```
person_zhu_kun → tracks → [etf_513050, stock_09992]
person_zhu_kun → investments → [stock_601088_shenhua, etf_513180_hstech, stock_688008_lanqi]
person_zhu_kun → spouse/child → [person_yao_wenhai, person_zhu_lingxiao]
project_stock_research_engine → analyzed → [京东/神华/澜起/芯片ETF/恒生科技]
skill_superresearch → governs → project_stock_research_engine
project_ai_news_phase2 → has_bug → pattern_ai_news_critical_bugs
bug_daily_questions_deliver_mode → fixed_in → skill_daily_questions
concept_openai_threat_model → held_by → person_sam_altman
```

---

## 📊 实体统计（截至2026-05-29）

| 目录 | 数量 |
|------|------|
| investments/ | 7 |
| projects/ | 12 |
| tasks/ | 2 |
| concepts/ | 8 |
| bugs/ | 7 |
| persons/ | 5 |
| documents/ | 4 |
| books/ | 1 |
| people-fiction/ | 1 |
| **合计** | **47 entity pages** |

---

*最后更新：2026-05-29*
*来源：memory/*.md + ontology graph.jsonl*
*整理方式：遍历ontology实体，批量创建对应的wiki entity pages*