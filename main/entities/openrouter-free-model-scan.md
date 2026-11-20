---
pageType: entity
id: entity.project.openrouter-free-model-scan
title: OpenRouter 免费模型周扫（openrouter-free-model-scan）
entityType: project
aliases:
  - openrouter-free-model-scan
  - OpenRouter 免费模型扫描
  - 每周免费模型推荐
updatedAt: "2026-08-16"
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-16-1157-614ca6bf
  - source.bridge.workspace-142ea9a2.memory-2026-08-16-1145-07d14764
claims:
  - id: claim.openrouter-free-scan.schedule
    text: "定时任务 openrouter-free-model-scan：每周五 18:00（北京时间 UTC+8）自动执行，首次/下次运行 2026-08-21 周五；流程为抓取 OpenRouter 全部模型 → 筛出免费模型 → 按 1M 上下文推理模型 / 快速响应视觉模型 / 快速响应 TTS 模型 / 快速响应 embedding 模型 四类推荐；完整报告存 `research/openrouter-free-models/日期.md`，精简版周报自动推送。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1157-614ca6bf
        weight: 0.9
  - id: claim.openrouter-free-scan.delivery
    text: "投递目标初始按规范走飞书私聊，后按用户要求改为群聊 oc_812b4a80dbf93832f71b6135ef6cb25a，其余配置不变（每周五 18:00 北京时间执行）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1157-614ca6bf
        weight: 0.85
  - id: claim.openrouter-free-scan.baseline-20260816
    text: "2026-08-16 预扫基线：OpenRouter API 共 413 个模型，免费模型 19 个。其中 1M 上下文只有 `nvidia/nemotron-3.5-lightning:free`（1M，30B MoE / 3B 激活）与 `nvidia/nemotron-3-ultra-550b-a55b:free`（1M，550B / 55B 激活）；快速视觉候选为 `nemotron-nano-12b-v2-vl:free`、`dots-3-note-preview:free`（280B/16B 活跃，支持图像）、`gemma-4-26b-a4b:free`。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1157-614ca6bf
        weight: 0.85
  - id: claim.openrouter-free-scan.gaps-20260816
    text: "两个已知空缺（周报中如实标注「暂无」并给替代建议，不硬凑）：OpenRouter 当时没有任何免费 TTS 模型（audio 输出仅有 lyria 音乐生成与付费 gpt-audio），embedding 模型在整个模型列表中不存在。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1157-614ca6bf
        weight: 0.85
  - id: claim.openrouter-free-scan.popularity-field-missing
    text: "OpenRouter API 不返回 popularity/top_week 排名数据（字段全为 null，`order=top-weekly` 参数也不改变返回顺序），因此「近期热门」只能靠上线日期（新鲜度）近似判断，无法从 API 直接确认热门榜。2026-08-16 时点 413 个模型中同时满足免费且上下文 ≥1M 的只有 4 个，其中 2 个是 google/lyria 音乐生成模型（非聊天 LLM）。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1145-07d14764
        weight: 0.8
---

# OpenRouter 免费模型周扫（openrouter-free-model-scan）

## 任务定义

| 项 | 值 |
|----|----|
| 任务名 | `openrouter-free-model-scan` |
| 频率 | 每周五 18:00（北京时间 UTC+8） |
| 首次运行 | 2026-08-21 |
| 投递 | 飞书群 `oc_812b4a80dbf93832f71b6135ef6cb25a` |
| 完整报告 | `research/openrouter-free-models/日期.md` |

## 四类推荐维度

1. **1M 上下文推理模型**
2. **快速响应视觉模型**
3. **快速响应 TTS 模型**
4. **快速响应 embedding 模型**

## 2026-08-16 基线快照

- 总模型数 413，免费 19
- 免费 + 1M 上下文：仅 `nvidia/nemotron-3.5-lightning:free`、`nvidia/nemotron-3-ultra-550b-a55b:free`
- 快速视觉候选：`nemotron-nano-12b-v2-vl:free`、`dots-3-note-preview:free`、`gemma-4-26b-a4b:free`
- ⚠️ 免费 TTS：0 个；embedding：列表中不存在

## 已知限制

- OpenRouter API 的 popularity / top_week 字段恒为 null，`order=top-weekly` 无效 → 热门度只能用上线日期近似。
- 免费且 ≥1M 上下文的模型里混有 `google/lyria-3-pro-preview` / `lyria-3-clip-preview`（音乐生成，非聊天 LLM），筛选时要排除。

## 相关

- [[omniroute-combo-config]] — 选中模型后常接入 OmniRoute combo 使用
- [[clashman-skill]] — 网络/代理排查相关

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-16-1157](../sources/bridge-workspace-142ea9a2-memory-2026-08-16-1157-614ca6bf.md)
- [Memory Bridge (main): 2026-08-16-1145](../sources/bridge-workspace-142ea9a2-memory-2026-08-16-1145-07d14764.md)

### Related Pages

- [OmniRoute Combo（多模型路由配置）](omniroute-combo-config.md)
<!-- openclaw:wiki:related:end -->
