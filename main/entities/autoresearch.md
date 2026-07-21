---
pageType: entity
id: entity.autoresearch
title: autoresearch
entityType: tool
aliases:
  - autoresearch
  - Karpathy autoresearch
sourceIds:
  - "autoresearch-README"
updatedAt: 2026-07-18T13:24:00.000Z
relationships:
  - targetId: entity.darwin-skill
    targetTitle: "darwin-skill"
    kind: inspired-by
    weight: 1.0
---

# autoresearch

**AI agents 在单 GPU nanochat 训练上自动跑研究实验。**

GitHub: [karpathy/autoresearch](https://github.com/karpathy/autoresearch)  
作者：Andrej Karpathy  
许可证：MIT

## 核心理念

给 AI agent 一个完整但精简的 LLM 训练代码，让它在夜里自主实验。agent 修改代码、训练 5 分钟、检查效果是否提升、保留或丢弃结果、反复循环。你早上醒来看到的是实验日志和（希望是）一个更好的模型。

> *"这 repo 揭示了这一切最初是怎么开始的。"* — @karpathy, March 2026

## 项目结构

整个仓库只有三个核心文件：

- **`prepare.py`** — 固定常量、一次性数据准备（下载训练数据、训练 BPE tokenizer）和运行时工具（数据加载器、评估函数）。**不修改。**
- **`train.py`** — agent 唯一修改的文件。包含完整 GPT 模型、优化器（Muon + AdamW）、训练循环。模型架构、超参数、优化器、batch size 等均属修改范围。**由 agent 编辑和迭代。**
- **`program.md`** — 面向一个 agent 的基线指令。指向此处让它启动。**由人类编辑和迭代。**

## 设计哲学

- **单文件修改**：agent 只碰 `train.py`，保持范围可控
- **固定 5 分钟时间预算**：每次训练跑正好 5 分钟，无论什么平台。约 12 exp/h，一夜 ~100 个实验
- **自包含**：除 PyTorch 外无复杂外部依赖
- **metric**：`val_bpb`（验证 bits per byte）——越低越好，与词表大小无关

## 使用方式

```
# 安装
uv sync

# 一次性数据准备
uv run prepare.py

# 手动跑一次单实验
uv run train.py

# 启动 agent
→ 把 Claude/Codex 指向 program.md，让它开始
```

## 与 darwin-skill 的关系

darwin-skill 的核心理念——**"把自主实验循环从模型训练搬到 Skill 优化领域"**——直接受 autoresearch 启发。autoresearch 是实验循环的原型，darwin 将其方法论迁移到了 agent skill 的文本空间优化。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
