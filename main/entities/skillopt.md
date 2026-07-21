---
pageType: entity
id: entity.skillopt
title: SkillOpt
entityType: tool
aliases:
  - SkillOpt
  - Microsoft SkillOpt
sourceIds:
  - "skillopt-README"
updatedAt: 2026-07-18T13:24:00.000Z
relationships:
  - targetId: entity.darwin-skill
    targetTitle: "darwin-skill"
    kind: listed-integration
    weight: 1.0
---

# SkillOpt

**像训练神经网络一样训练 Agent Skills——有 epoch、mini-batchsize、learning rate 和 validation gates，但不碰模型权重。**

GitHub: [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)  
项目主页: [microsoft.github.io/SkillOpt](https://microsoft.github.io/SkillOpt/)  
论文: [arXiv 2605.23904](https://arxiv.org/abs/2605.23904)  
许可证: MIT  
PyPI: `pip install skillopt`

## 核心理念

现代的 agent skills 通常手工编写、由强 LLM 一次性生成、或通过松散的自我修订进化——这些都不像一个深度学习优化器的行为，也都没有保证在反馈下能稳定提升。

**SkillOpt 把 skill 文档视为 frozen agent 的可训练状态**，以权重空间优化同样的纪律来训练它。一个独立的 optimizer 模型将 scored rollouts 转换为对单份 skill 文档的有界增/删/替换编辑；候选编辑仅在严格提升 held-out validation score 时才被接受。

## 关键特性

- **文本空间训练**：训练 agent skill 的文本本身，不碰模型权重
- **验证门控（Validation Gate）**：每次 edit 必须通过 held-out 验证集检验，分数没提高就拒绝
- **文本学习率预算**：控制每次编辑的 token 修改量，防止剧烈变化
- **回退缓冲区**：被拒绝的 edit 存入缓冲区，防止重复犯同样的错
- **epoch-wise 慢/元更新**：让 skill 训练稳定收敛

## 已部署的产物

`best_skill.md`（通常 300–2,000 tokens），在部署时对目标模型零开销。

## 效果

在 **6 个 benchmark、7 个目标模型、3 个执行框架**（direct chat、Codex CLI、Claude Code CLI）上，SkillOpt 在所有 **52 个 (model, benchmark, harness) 单元格**上取得最优或并列最优：

- GPT-5.5 提升：direct chat **+23.5 分**，Codex agentic loop **+24.8 分**，Claude Code **+19.1 分**
- 优化后的 skill 在模型规模间可迁移、在 Codex 和 Claude Code 之间可迁移、在相近任务之间可迁移

## 版本里程碑

- **v0.1.0** (2026-06-02)：首个 PyPI 发布，完整训练循环 + 多后端 + 6 个内置 benchmark + WebUI
- **v0.2.0** (2026-07-02)：新增 **SkillOpt-Sleep**（夜间离线自进化引擎），集成 Claude Code / Codex / Copilot / Devin / OpenClaw 接口

## 与 darwin-skill 的关系

SkillOpt 与 darwin-skill 是**双向认可**的关系：

- darwin 2.0 吸收了 SkillOpt 的 **validation-gated 框架**和 **SkillLens** 论文的维度升级
- darwin 被 SkillOpt 官方列入了 **集成名单**（与 gbrain, gbrain-evals 并列）

两者的核心区别：
- **SkillOpt**：全自动设计，追求零人工干预
- **darwin-skill**：保留 **Human in the Loop** 三层守关，强调人在关键节点做判断

## 安装

```bash
pip install skillopt
```

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
