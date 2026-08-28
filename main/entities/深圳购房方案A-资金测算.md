---
pageType: entity
id: entity.project.shenzhen-mortgage-plan-a
title: 深圳购房方案A（直接买二套）资金与月供测算
entityType: project
aliases:
  - 方案A
  - 二套购房测算
  - 帝港
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.mortgage-plan-a.scope
    text: "方案A 定义为「在帝港不出售的前提下直接买二套」，因此需承担双房贷压力，测算需计入帝港现有月供及租金补贴的可能。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-30-plan-a-mortgage-1079f846
        weight: 0.9
  - id: claim.mortgage-plan-a.brief
    text: "C2 调研任务（方案A 详细资金与月供测算）研究深度 L2（标准），依赖 C1 已完成的政策税费数据；调研范围含三档总价 600/650/700 万月供对比、商业贷/公积金贷/组合贷最优方案、DTI 压力评估（2 万可承受线）、双房贷压力分析、总成本汇总表。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-30-plan-a-mortgage-1079f846
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-03-30-plan-a-mortgage-1079f846.md

---
# 深圳购房方案A（直接买二套）资金与月供测算

深圳二套购房决策研究中的「方案A」分支。

## 方案定义

**前提**：帝港不出售 → 买二套后同时背负两处房贷，可用帝港租金做部分对冲。

## C2 调研设计（L2 标准深度）

| 维度 | 内容 |
|------|------|
| 总价档位 | 600 / 650 / 700 万三档月供对比 |
| 贷款方式 | 商业贷 / 公积金贷 / 组合贷 最优方案 |
| 压力测试 | DTI 是否落在 2 万/月可承受范围内 |
| 双房贷 | 含帝港月供 + 租金补贴情景 |
| 汇总 | 总成本汇总表 |

## 依赖

- 上游 **C1**：政策与税费数据（已完成）
- 下游：与「出售帝港再置换」方案做对比决策

## 相关

- [[sz-odata-skill]] — 深圳本地房价/政策数据取数通道
- [[superresearch]] — 本次研究采用的流程框架

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
