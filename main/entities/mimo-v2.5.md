---
pageType: entity
entityType: ai-model
id: entity.ai-model.mimo-v2.5
canonicalId: xiaomi.mimo-v2.5
aliases:
  - MiMo V2.5
  - MiMo
  - 小米MiMo
privacyTier: public
updatedAt: "2026-06-05"
lastRefreshedAt: "2026-06-05T00:00:00.000Z"
bestUsedFor:
  - AI编码任务
  - 多语言对话
  - 技术分析
notEnoughFor:
  - 视频生成
  - 图像生成
claims:
  - id: claim.mimo-v2.5.pricing
    text: "MiMo V2.5海外定价：缓存命中$0.08/未命中$0.40/输出$2.00，上下文1M tokens"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-02-1347-435ec224
        weight: 0.9
  - id: claim.mimo-v2.5.comparison-deepseek
    text: "MiMo V2.5在输出价格上高于DeepSeek V4 Flash（$2.00 vs $0.28），但低于DeepSeek V4 Pro（$2.00 vs $3.33）"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-02-1347-435ec224
        weight: 0.85
  - id: claim.mimo-v2.5.openclaw-model
    text: "MiMo V2.5是OpenClaw当前运行的默认模型"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: runtime-config
        sourceId: source.runtime
        weight: 0.95
relationships:
  - targetId: entity.project.openclaw
    targetTitle: OpenClaw
    kind: used-by
    weight: 0.9
    note: "作为OpenClaw的默认运行模型"
  - targetId: entity.ai-model.deepseek-v4
    targetTitle: DeepSeek V4
    kind: competitor
    weight: 0.8
    note: "价格和能力上的直接竞品"
---

# MiMo V2.5

> 小米自研AI大模型，是OpenClaw当前运行的默认模型

## 基本信息

- **开发商**：小米
- **类型**：大语言模型
- **上下文窗口**：1M tokens
- **发布状态**：已发布（2026年）

## 定价（海外）

| 模型 | 缓存命中输入 | 缓存未命中输入 | 输出 |
|---|---|---|---|
| MiMo V2.5 | $0.08 | $0.40 | $2.00 |
| MiMo V2.5-Pro | $0.20 | $1.00 | $3.00 |

## 与DeepSeek V4对比

| 模型 | 缓存命中输入 | 缓存未命中输入 | 输出 |
|---|---|---|---|
| **MiMo V2.5** | $0.08 | $0.40 | $2.00 |
| **MiMo V2.5-Pro** | $0.20 | $1.00 | $3.00 |
| **DeepSeek V4 Flash** | ~$0.03 | ~$0.14 | ~$0.28 |
| **DeepSeek V4 Pro** | ~$0.28 | ~$1.67 | ~$3.33 |

## 关键特点

- 1M tokens超长上下文
- 支持编码、多语言、技术分析等多任务
- OpenClaw集成：作为默认模型运行
- Pro版本在推理能力上更强

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
