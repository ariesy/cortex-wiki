---
pageType: entity
entityType: skill
id: entity.skill.council-of-the-wise
updatedAt: "2026-08-28"
relationships:
  - targetId: entity.project.investsignal-architecture-v1-1
    targetTitle: "InvestSignal 架构设计 v1.1"
    kind: related
    weight: 0.5
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-03-22-session-compression-4775e485
---

# council-of-the-wise（智者委员会）技能

> entity_type: skill

OpenClaw 用户自定义技能，触发名称为 `council`。提供多专家视角审查（在 InvestSignal 项目中表现为 5 位专家多视角审查并提出 Action Items）。

---

## 安装与加载

- 原安装于工作区（workspace）版本已卸载
- 重新安装到 `~/.openclaw/skills` 目录后成功加载
- 触发名称：`council`

---

## 使用记录

在 InvestSignal 项目 Sprint 3 / Sprint 4 / Sprint 7 的开发流程中被复用：
- S3-T3 融资融券模块：5 位专家审查后补充节假日处理、历史回填、symbol 字段预留
- S3-T4 资金面信号组合：审查后补充分歧警告、置信度公式、降级逻辑、可解释性输出
- S4-T9 港股数据支持：Tech Spec 审核并提出多项改进建议

---

## 关联排查记录

同一会话中还处理了其他技能问题：
- ClawHub API 速率限制：原因为未登录账号，未认证用户配额较低，登录后可提升到 20-30 请求/15 分钟
- session-watchdog 技能：结构正常但因名称冲突被系统屏蔽，重命名为 test-watchdog 后成功加载
- session-logs 技能依赖：仅需要 `jq` 和 `ripgrep` 两个命令行工具
- 已安装技能总数：44 个用户自定义技能，19 个已加载，25 个未加载

---

*来源: memory/2026-03-22-session-compression.md*

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-03-22-session-compression](../sources/bridge-workspace-142ea9a2-memory-2026-03-22-session-compression-4775e485.md)
<!-- openclaw:wiki:related:end -->
