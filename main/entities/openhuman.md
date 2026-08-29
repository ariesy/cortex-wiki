---
pageType: entity
id: entity.openhuman
title: openhuman
entityType: tool
aliases:
  - openhuman
  - tinyhumansai/openhuman
  - OpenHuman
sourceIds:
  - sources/github-openhuman-readme-20260829.md
updatedAt: 2026-08-29T00:20:00.000Z
tags:
  - agent-harness
  - 本地优先
  - memory
  - Rust
confidence: medium
relationships:
  - targetId: entity.ai-job-search
    targetTitle: "ai-job-search"
    kind: same-cohort
    weight: 0.4
  - targetId: entity.autoresearch
    targetTitle: "autoresearch"
    kind: related
    weight: 0.3
---

# openhuman

**本地优先的"个人超级智能"：持久记忆的大脑 + agent 舰队编排 + 深度研究。Early Beta，Rust 实现。**

GitHub: [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)
语言：**Rust** · License：**GPL-3.0** · 状态：**Early Beta**
实测（2026-08-29）：★ 38,723 / forks 3,802 · 建库 2026-02-18

## 三个支柱（README 原结构）

| 支柱 | 主张 |
|------|------|
| 🧠 **The brain** | 构建持久的、**本地优先**的生活记忆 |
| 🕸️ **The orchestrator** | 在 **durable graphs** 上跑 agent 舰队与工作流 |
| 🔬 **The deep researcher & doer** | 在你问完之前就扫完你的数据与网页 |
| 🧍 **Human, private, yours** | 数据归你 |

## 项目方自述（需打折）

> "OpenHuman is not AGI. But it is a meaningful architectural step closer, with better memory, better orchestration, and better tooling."
> "🎉 Within one week of launch, OpenHuman became the number one trending repository on GitHub for nine days in a row."

## 与其他三家的关键差异

| 项 | openhuman | archify / awesome-gpt-image-2 / ai-job-search |
|----|-----------|---------------------------------------------|
| **性质** | 平台 / harness 赌注 | 单用途 skill |
| **许可** | **GPL-3.0（传染性）** | MIT |
| **成熟度** | Early Beta，README 明写 "Expect rough edges" | 已可用 |
| **试用成本** | 装客户端 / 系统包（Homebrew、.deb、AUR） | `npx` 一行 |

## 判断

**四个里我最保留意见的一个。** 理由：

1. **成熟度与热度严重不匹配。** 38.7k star 配 Early Beta —— README 自己也写了 "Expect rough edges"。三大能力（持久记忆 / 舰队编排 / 深度研究）**实际完成度未经独立验证**，README 描述的是愿景还是现状，无法从文档判断。
2. **趋势声明是项目方自述。** "GitHub 趋势第一连续九天"没有第三方交叉验证，属营销话术范畴。
3. **GPL-3.0 是实质约束。** 与其余三个 MIT 仓库不同，GPL-3.0 有传染性——若未来要把它的组件并入自有工作流或商业产品，需先评估合规。**这也是它与 OpenClaw 这类已有本地记忆体系集成时的现实障碍。**
4. **功能高度重叠已有设施。** "本地优先记忆 + agent 编排 + 深度研究"与主人在跑的 OpenClaw / wiki / memory 体系**定位重叠**。引入第二个记忆中枢会分散数据，边际收益存疑。
5. **商标/命名风险**：与已存在的 Open Humans Foundation / `openhumans` 项目同名，需留意后续是否更名。

**结论：观察，不部署。** 与 Archify 那种"今天装了明天能用"不同，OpenHuman 现在投入时间是押注。等它出 stable release、且有独立第三方的完成度评测后再评估。

## 观察点

- Early Beta → stable 的时间表
- 是否出现第三方（非项目方）的完成度评测，尤其是**记忆检索质量**与**编排可靠性**的实测
- 命名争议是否有后续（更名 / 商标问题）
- durable graphs 的技术实现细节（这是它相对普通 agent 框架的核心差异点，README 语焉不详）

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
