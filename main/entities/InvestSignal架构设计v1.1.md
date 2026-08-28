---
pageType: entity
entityType: project
id: entity.project.investsignal-architecture-v1-1
updatedAt: "2026-08-28"
relationships:
  - targetId: entity.task.investsignal-target-price-alert
    targetTitle: "InvestSignal目标价预警优化"
    kind: parent-of
    weight: 0.7
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-03-14-0408-121079d1
---

# InvestSignal 架构设计 v1.1

> entity_type: project

InvestSignal 项目架构设计文档从 v1.0 修订到 v1.1，基于 POC 验证结果与评审报告建议完成。修订于 2026-03-14 由用户确认后落地。

---

## 技术决策（ADR）变更

| 决策项 | 原方案 v1.0 | 新方案 v1.1（POC 验证后） |
|--------|------------|--------------------------|
| 翻译服务 | 本地模型 qwen3:8b（60 秒/条） | Cloud 模型 qwen3-coder:480b-cloud（1.8 秒/条） |
| 数据源 | 多种免费源 | AkShare（主）+ Tushare（备，仅沪市） |

---

## 架构简化：Phase 渐进式实现

评审报告建议移除情绪面/宏观面以简化架构，采用按价值排序的三阶段：

- **Phase 1（MVP）**：技术面 + 资金面 — 约 80% 价值，10-12h
- **Phase 2**：基本面 + 完整回测 + 报告 — 约 15% 价值，10-12h
- **Phase 3**：情绪面 + 宏观面 — 约 5% 价值，10-15h

其他调整：
- 翻译逻辑下移到采集层
- 报告结构改为「先洞察后数据」

---

## 交互设计

支持双命令模式：
- 精确代码：`查询 600519`
- 自然语言：`帮我看看茅台`

---

## 关联

- 文档位置：InvestSignal 项目 `docs/` 下 prd / functionspec / 架构设计 / 评审结果报告 / POC 结果
- 相关任务：[InvestSignal目标价预警优化](investsignal-target-price-alert.md)

---

*来源: memory/2026-03-14-0408.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-03-14-0408](../sources/bridge-workspace-142ea9a2-memory-2026-03-14-0408-121079d1.md)
<!-- openclaw:wiki:related:end -->
