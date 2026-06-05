---
pageType: entity
entityType: project
id: entity.project.moneyprinter-turbo
canonicalId: github.harry0703.moneyprinter-turbo
aliases:
  - MoneyPrinterTurbo
  - Money Printer Turbo
privacyTier: public
updatedAt: "2026-06-05"
lastRefreshedAt: "2026-06-05T00:00:00.000Z"
bestUsedFor:
  - 批量短视频生产
  - 自媒体搬运号
  - YouTube/TikTok内容生产
notEnoughFor:
  - AI文生视频
  - 高质量原创视频
claims:
  - id: claim.moneyprinter.pipeline
    text: "MoneyPrinterTurbo使用LLM写文案+Pexels/Pixabay素材拼接+ffmpeg合成的流水线，非AI文生视频"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-05-1131-e6b85005
        weight: 0.9
  - id: claim.moneyprinter.no-video-api
    text: "项目不需要视频生成模型API（Sora/Kling/Vidu），核心依赖LLM+TTS+Pexels API+ffmpeg"
    status: confirmed
    confidence: 0.95
    evidence:
      - kind: memory-bridge
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-05-1131-e6b85005
        weight: 0.9
relationships:
  - targetId: entity.project.guardians-eye
    targetTitle: 守护眼公众号
    kind: potential-tool
    weight: 0.5
    note: "可用于守护眼批量生产短视频内容"
---

# MoneyPrinterTurbo

> GitHub: harry0703/MoneyPrinterTurbo — 用AI大模型写文案+拼接真实素材+ffmpeg合成的短视频批量生产工具

## 项目定位

一句话：**短视频批量生产流水线**，目标是做YouTube/TikTok搬运号、自媒体批量产出工具。

**不是**AI文生视频（Sora/Kling/Vidu那种），不需要视频生成模型API。

## 视频生成 Pipeline

| Step | 功能 | 依赖 |
|---|---|---|
| 1 | LLM生成短视频文案 | 必须配LLM（OpenAI/DeepSeek/Moonshot/Qwen/Gemini/智谱/豆包等17+） |
| 2 | LLM从文案抽关键词 | 复用LLM |
| 3 | TTS生成语音 | edge-tts（免费）/ Azure Speech |
| 4 | 生成字幕 | edge-tts时间戳 / Whisper |
| 5 | 用关键词搜素材 | Pexels / Pixabay API Key |
| 6 | ffmpeg拼接合成 | ffmpeg |

## 必需配置

- **LLM API**：任选一种（OpenAI/DeepSeek/Moonshot等）
- **素材API Key**：Pexels或Pixabay（二选一）
- **TTS**：edge-tts免费可用，无需Key

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
