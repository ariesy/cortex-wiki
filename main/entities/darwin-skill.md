---
pageType: entity
id: entity.darwin-skill
title: darwin-skill
entityType: tool
aliases:
  - darwin-skill
  - 达尔文技能
sourceIds:
  - "darwin-skill-README"
updatedAt: 2026-07-18T13:18:00.000Z
relationships:
  - targetId: entity.nuwa-skill
    targetTitle: "nuwa-skill"
    kind: related-to
    weight: 1.0
  - targetId: entity.cangjie-skill
    targetTitle: "cangjie-skill"
    kind: related-to
    weight: 1.0
---

# darwin-skill

**自动进化任意 AI Skill。**

GitHub: [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill)

## 使命

让技能自动进化。nuwa-skill 和 cangjie-skill 产出的 skill 包可以通过 darwin-skill 不断迭代优化，让 skill 在实际使用中持续改进。

## 核心能力

- **自动测试与验证**：读取 skill 的 `test-prompts.json`，自动运行测试
- **回炉进化**：未通过测试的 skill 自动回炉，基于失败分析生成改进版
- **持续迭代**：支持多轮进化，每次迭代都保存版本历史
- **兼容格式**：严格遵循 nuwa-skill 和 cangjie-skill 输出的 test-prompts.json 格式

## 与 cangjie-skill 的衔接

cangjie-skill 的阶段 4（压力测试）产出的 `test-prompts.json` 严格遵循 darwin-skill 的格式标准，确保产出可直接接入 darwin 做自动进化。

## 生态定位

darwin-skill 是更大 skill 生态的一部分：
- **[nuwa-skill](https://github.com/alchaincyf/nuwa-skill)** — 蒸馏人（思维方式、表达 DNA）
- **[cangjie-skill](https://github.com/kangarooking/cangjie-skill)** — 蒸馏书/视频（方法论、框架、原则）
- **darwin-skill**（本仓库）— 进化任意 skill

三者咬合：nuwa 蒸馏人，cangjie 蒸馏书，darwin 让它们持续进化。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
