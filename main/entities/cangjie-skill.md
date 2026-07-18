---
pageType: entity
id: entity.cangjie-skill
title: cangjie-skill
entityType: tool
aliases:
  - cangjie-skill
  - 仓颉技能
  - RIA-TV++
sourceIds:
  - "cangjie-skill-README"
updatedAt: 2026-07-18T13:18:00.000Z
relationships:
  - targetId: entity.nuwa-skill
    targetTitle: "nuwa-skill"
    kind: related-to
    weight: 1.0
  - targetId: entity.darwin-skill
    targetTitle: "darwin-skill"
    kind: related-to
    weight: 1.0
---

# cangjie-skill

**把书、长视频、播客里的方法论，蒸馏成可调用的 AI Skills。**

GitHub: [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)  
作者：袋鼠帝 (kangarooking)  
许可证：MIT

## 使命

把一本书里沉淀的方法论，拆解成一组**原子化、可被 agent 在真实场景下调用**的 skills，让读者真正用起来，而不是让知识躺在收藏夹落灰。

## 核心方法论：RIA-TV++

RIA-TV++ 是一个 7 阶段流水线，借鉴了多个成熟方法论：

### 7 阶段流水线

| 阶段 | 名称 | 产出 |
|---|---|---|
| 0 | Adler 整书理解 | BOOK_OVERVIEW.md |
| 1 | 5 个 sub-agent 并行提取 | 候选方法论单元池 |
| 1.5 | 三重验证筛选 | 通过验证的单元 |
| 2 | RIA++ 构造 skill | 每个 skill 的 SKILL.md |
| 3 | Zettelkasten 链接 | INDEX.md + GLOSSARY.md |
| 4 | 压力测试 | test-prompts.json + 回炉 |
| 5 | 交付 | DIGEST.md + 安装到 skills 目录 |

### 命名拆解

- **RIA** — 赵周《这样读书就够了》的便签拆书法（Reading / Interpretation / Appropriation）
- **TV** — Triple Verification，三重验证
- **++** — 面向 agent 执行的扩展：E (Execution 可执行步骤) + B (Boundary 边界)

### 三重验证（核心质量门）

每个候选方法论单元必须通过三项检验（通过率通常 25-50%）：

1. **V1 跨域验证**：书中至少 2 个独立语境有佐证
2. **V2 预测力测试**：能用这个方法论推导出书里没明说的新问题答案
3. **V3 独特性检验**：不是常识，必须是作者的独特视角

### RIA++ 构造（6 维）

每个 skill 按 R / I / A1 / A2 / E / B 六个维度结构化，确保不只是一段描述，而是真实可调用的工具。

## 5 个并行提取器

| 提取器 | 提取目标 |
|---|---|
| 框架提取器 | 思维模型、决策框架、推理方法 |
| 原则提取器 | 原则、清单、规则 |
| 案例提取器 | 作者用过的具体实例 |
| 反例提取器 | 书中警告的失败模式 |
| 术语提取器 | 关键概念词典 |

## 生态定位

cangjie-skill 是更大 skill 生态的一部分：
- **[nuwa-skill](https://github.com/alchaincyf/nuwa-skill)** — 蒸馏人（思维方式、表达 DNA）
- **cangjie-skill**（本仓库）— 蒸馏书/视频（方法论、框架、原则）
- **[darwin-skill](https://github.com/alchaincyf/darwin-skill)** — 进化任意 skill

三者咬合：nuwa 蒸馏人，cangjie 蒸馏书，darwin 让它们持续进化。

## 已生成的 skill 包（部分）

| 仓库 | 来源 | Skills 数 |
|---|---|---|
| [buffett-letters-skill](https://github.com/kangarooking/buffett-letters-skill) | 巴菲特致股东的信 (1957-2023) | 20 |
| [duan-yongping-skill](https://github.com/kangarooking/duan-yongping-skill) | 段永平投资问答录 | 15 |
| [cognitive-dividend-skill](https://github.com/kangarooking/cognitive-dividend-skill) | 《认知红利》 | 15 |
| [poor-charlies-almanack-skill](https://github.com/kangarooking/poor-charlies-almanack-skill) | 《穷查理宝典》 | 12 |
| [influence-skill](https://github.com/kangarooking/influence-skill) | 《影响力》 | 12 |
| [mao-selected-works-skill](https://github.com/kangarooking/mao-selected-works-skill) | 《毛泽东选集》1-5 卷 | 25 |
| [huangdi-neijing-skill](https://github.com/kangarooking/huangdi-neijing-skill) | 《黄帝内经》 | 22 |
| [ai-for-everyone-skill](https://github.com/kangarooking/ai-for-everyone-skill) | 吴恩达 AI for Everyone 课程 | 25 |

## 仓库结构

```
cangjie-skill/
├── README.md               ← 主文档
├── SKILL.md                ← 元 skill 定义（执行规范本体）
├── LICENSE                 ← MIT
├── methodology/            ← RIA-TV++ 各阶段方法论文档
├── extractors/             ← 5 个提取器的 prompt 定义
└── templates/              ← SKILL.md / INDEX.md / BOOK_OVERVIEW.md 模板
```

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
