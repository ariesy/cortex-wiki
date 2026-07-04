---
pageType: entity
id: entity:ai-berkshire
title: ai-berkshire
category: 开源项目/投资研究
description: AI时代价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行对抗研究。兼容Claude Code与Codex。
updatedAt: 2026-07-04T10:26:00.000Z
sourceIds:
  - https://github.com/xbtlin/ai-berkshire
  - https://github.com/xbtlin/ai-berkshire/tree/main/skills
  - https://github.com/xbtlin/ai-berkshire/tree/main/reports
  - https://github.com/xbtlin/ai-berkshire/blob/main/tools/financial_rigor.py
  - https://github.com/xbtlin/ai-berkshire/blob/main/skills/financial-data.md
claims:
  - id: basic-stats
    text: GitHub星标9.4k，Forks 1.2k，Commit数1207（2026-07-04）
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire
        confidence: 0.95
  - id: four-masters
    text: 框架整合巴菲特、芒格、段永平、李录四位价值投资大师的方法论，通过多Agent并行架构实施对抗研究
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire
        confidence: 0.95
  - id: agent-parallel
    text: 四Agent并行研究：Agent1段永平(商业模式)、Agent2巴菲特(财务估值)、Agent3芒格(行业竞争)、Agent4李录(风险管理)
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire
        confidence: 0.95
  - id: financial-data-us
    text: 美股财务数据主来源为macrotrends.net，副来源为stockanalysis.com，原始一手为SEC EDGAR
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/financial-data.md
        confidence: 0.95
  - id: financial-data-hk
    text: 港股财务数据主来源为aastocks.com，副来源为macrotrends(ADR)，原始一手为HKEX披露易
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/financial-data.md
        confidence: 0.95
  - id: financial-data-a
    text: A股财务数据主来源为东方财富eastmoney.com，副来源为巨潮资讯cninfo.com.cn
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/financial-data.md
        confidence: 0.95
  - id: cross-validation-rule
    text: 每个关键财务数据必须来自2个独立来源，误差>1%须标记，>5%须查原始财报
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/financial-data.md
        confidence: 0.95
  - id: morningstar-fair-value
    text: 估值数据最权威来源为晨星公允价值，数据存储于data/morningstar_fair_value_20260519.csv（批量抓取，非实时API）
    status: verified
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/tree/main/data
        confidence: 0.9
  - id: three-scenario-valuation
    text: 自建三情景估值模型(three-scenario)内置于tools/financial_rigor.py，输入EPS+增速+目标PE，输出精确计算的乐观/中性/悲观目标价
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/tools/financial_rigor.py
        confidence: 0.95
  - id: decimal-precision
    text: 所有财务计算使用Python decimal.Decimal，不用float，避免LLM心算误差
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire
        confidence: 0.95
  - id: primary-source-priority
    text: 财报精读(skills/earnings-review.md)坚持一手资料优先：财报原文>电话会纪要>管理层致股东信，拒绝卖方研报
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/earnings-review.md
        confidence: 0.95
  - id: exit-verification
    text: 报告完成后执行15%随机抽样核验准出流程，通过后才发布
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/investment-research.md
        confidence: 0.95
  - id: moat-rating-abc
    text: 信息丰富度评级机制(A/B/C)：A级信息充裕、B级信息适中、C级信息稀缺，防止AI对信息稀缺公司用推测填充空白
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/skills/investment-research.md
        confidence: 0.95
  - id: tools-financial-rigor
    text: 金融严谨性工具箱(tools/financial_rigor.py)提供：市值验算、估值验算、多源交叉验证、三情景估值、Benford定律检测、精确计算器
    status: verified
    confidence: 0.95
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/tools/financial_rigor.py
        confidence: 0.95
  - id: 2024-return
    text: 自述2024全年收益+69.29%，但未经过独立验证
    status: unverified
    confidence: 0.3
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire
        confidence: 0.3
        note: 仅为项目自述，无第三方审计或验证
  - id: dcf-used
    text: 部分报告（如贵州茅台DCF估值研究）使用DCF估值，但核心假设（永续增长率、折现率）由AI主观判断，非量化模型
    status: verified
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/tree/main/reports
        confidence: 0.9
  - id: morningstar-data-lag
    text: 晨星公允价值数据为批量抓取，非实时API，存在数据滞后问题
    status: verified
    confidence: 0.9
    evidence:
      - kind: web
        sourceId: https://github.com/xbtlin/ai-berkshire/blob/main/reports/%E5%85%A8%E7%90%83AI%E5%85%AC%E5%8F%B8-%E6%99%A8%E6%98%9F%E5%85%AC%E5%85%81%E5%85%AC%E5%8D%95vs%E5%BD%93%E5%89%8D%E8%82%A1%E4%BB%B7-20260519.md
        confidence: 0.9
confidence: 0.88
---

# ai-berkshire

AI时代价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行对抗研究。兼容Claude Code与Codex。

## 基本信息

| 项目 | 内容 |
|------|------|
| GitHub | https://github.com/xbtlin/ai-berkshire |
| Stars | ~9.4k（2026-07-04） |
| Forks | ~1.2k |
| 定位 | 兼容 Claude Code / Codex 的价值投资 Skill 合集 |
| 核心理念 | 四大师方法论 + 多Agent并行对抗研究 |
| 实战业绩 | 2024全年 +69.29%（自述，未独立验证） |

## 架构设计

### 多Agent并行体系

```
Team Lead（统筹）
├─ Agent 1：段永平视角 → 商业模式 + 管理层
├─ Agent 2：巴菲特视角 → 护城河 + 财务估值
├─ Agent 3：芒格视角 → 逆向思考 + 行业竞争
└─ Agent 4：李录视角 → 文明趋势 + 风险管理
```

**设计原则**：四人互相挑战，强制输出"通过/不通过/灰色地带"，避免AI两面讨好。

## 数据来源体系

### 财务数据（按市场分层）

| 市场 | 主来源 | 副来源 | 原始一手 |
|------|--------|--------|----------|
| 美股 | macrotrends.net | stockanalysis.com | SEC EDGAR |
| 港股 | aastocks.com | macrotrends（ADR） | HKEX披露易 |
| A股 | 东方财富 eastmoney.com | 巨潮资讯 cninfo.com.cn | 年报PDF |

**交叉验证规则**：每关键数据必须来自2个独立来源，误差>1%标记，>5%打回查原始财报。

### 估值体系（三层）

1. **晨星公允价值**（最权威）— 美股分析师报告（高）、港股分析师报告（中高）、A股量化模型+券商一致预期（中）；数据为批量抓取，有滞后
2. **三情景估值模型**（自建工具）— `tools/financial_rigor.py`，输入EPS+增速+目标PE，精确计算乐观/中性/悲观目标价
3. **DCF**（部分报告）— 假设由AI判断，非量化模型

## 主要Skills

- `/investment-research` — 四大师综合分析
- `/investment-team` — 多Agent并行研究
- `/earnings-review` — 财报精读（一手资料）
- `/industry-research` — 行业价值链扫描
- `/portfolio-review` — 组合管理
- `/dyp-ask` — 段永平问答
- `/industry-funnel` — 筛选漏斗（全市场→10家→3家）

## 优缺点

**值得学习**：多Agent对抗框架、交叉验证+精确计算、一手资料优先

**需要注意**：Morningstar数据抓取有滞后；三情景/DCF假设为AI主观判断；实战业绩未独立验证

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
