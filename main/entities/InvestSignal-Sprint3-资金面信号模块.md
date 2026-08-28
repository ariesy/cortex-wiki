---
pageType: entity
entityType: project
id: entity.project.investsignal-sprint3-capital-signal
updatedAt: "2026-08-28"
relationships:
  - targetId: entity.project.investsignal-architecture-v1-1
    targetTitle: "InvestSignal 架构设计 v1.1"
    kind: belongs-to
    weight: 0.9
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-03-15-05bd91a4
---

# InvestSignal Sprint 3：融资融券与资金面信号模块

> entity_type: project

InvestSignal 项目 Sprint 3（2026-03-15）完成资金面数据采集与组合信号生成链路，采用 TDD + 智者委员会（5 位专家多视角）审查的开发流程。

---

## S3-T3 融资融券模块

- 沪市 `stock_margin_sse()`、深市 `stock_margin_szse()` 双 API 验证通过
- 输出指标：融资余额、融资买入额、融券余量、融券余额
- 设计文档：`docs/technical-spec/S3-T3_Margin_Module_Design.md`
- 代码：`src/collector/margin/`（models.py / collector.py / tests/）
- 提交：commit 524d903（设计）、daeb01f（实现，17 个单测通过）

**审查后补充：**
- 节假日处理 `get_latest_available_date()`
- 历史回填机制 `history_days=30`
- 预留 `symbol` 字段便于扩展
- 统一 Signal 输出格式

**已知坑：深市两融数据单位是「亿元」，需转换为「元」** → 增加 `is_szse` 参数处理单位转换（修复已含于 commit 784a1d7）

---

## S3-T4 资金面信号组合模块

- 数据模型 `CapitalFlowSignal`，组合器 `src/collector/capital_flow/combiner.py`
- 22 个单元测试通过，提交 commit 784a1d7

**审查后补充：**
- 分歧警告机制：`consensus_warning`，分歧度 >= 0.5 触发
- 置信度公式：基于标准差计算
- 降级逻辑：某模块失败时使用默认 neutral
- 可解释性输出：`explanation` 字段

---

## S3-T5 组合信号生成模块

- 综合技术面 + 资金面信号，权重各 50%
- 数据模型 `CombinedSignal`，生成器 `src/signaler/combined/combiner.py`
- 19 个单元测试通过，提交 commit d450131
- 设计文档：`docs/technical-spec/S3-T5_Combined_Signal_Design.md`

---

## 技术验证结果

| API | 状态 | 返回字段 |
|-----|------|---------|
| stock_margin_sse | ✅ 可用 | 融资余额, 融资买入额, 融券余量, 融券余额 |
| stock_margin_szse | ✅ 可用 | 同上 |
| stock_margin_account_info | ✅ 可用 | 账户信息 |

---

*来源: memory/2026-03-15-05bd91a4.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-03-15](../sources/bridge-workspace-142ea9a2-memory-2026-03-15-05bd91a4.md)
<!-- openclaw:wiki:related:end -->
