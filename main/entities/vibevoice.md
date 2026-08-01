---
pageType: entity
id: entity.tool.vibevoice
entityType: tool
name: "VibeVoice"
updatedAt: "2026-08-01"
sourceIds:
  - github.com/microsoft/VibeVoice
---

# VibeVoice

微软官方开源的「前沿语音 AI 全家桶」（GitHub ⭐51.7k），涵盖 TTS（语音合成）与 ASR（语音识别）两条产品线。核心价值是「超长上下文 + 低帧率连续语音表征」的统一技术框架，而非单个模型。

## 核心技术

- **7.5Hz 超低帧率连续语音 tokenizer**（声学 + 语义双通道）：帧率远低于传统方案（12.5~25Hz），在保持音频保真度的同时大幅降低长序列计算成本——这是能单次处理 60~90 分钟长音频的关键。
- **Next-Token Diffusion 框架**（arXiv:2412.08635）：LLM 负责理解文本上下文与对话流，diffusion head 负责生成高保真声学细节。
- 基座模型：Qwen2.5-1.5B。

## 模型家族

| 模型 | 定位 | 关键指标 |
|------|------|----------|
| VibeVoice-ASR-7B | 统一语音转写（2026-01 开源） | 单次处理 60 分钟音频（64K token），输出 Who/When/What 结构化转写，支持自定义热词，50+ 语言，支持 vLLM 与微调，已集成 HF Transformers 与 Azure AI Foundry Labs |
| VibeVoice-ASR-BitNet (CPU) | 边缘推理引擎（2026-07 发布） | 异构量化 I8_S+I2_S：4.62GB→1.58GB，3+ CPU 线程实时推理（RTF<1），无需 GPU，配套 VibeASR.cpp |
| VibeVoice-TTS-1.5B | 长文本多说话人 TTS（ICLR 2026 Oral） | 单次合成最长 90 分钟，最多 4 说话人对话，英/中多语言。⚠️ 代码已于 2025-09 移除（滥用风险），权重仍在 HF |
| VibeVoice-Realtime-0.5B | 轻量实时 TTS（2025-12 开源） | ~300ms 首字延迟，流式文本输入，稳健生成约 10 分钟语音，实验性多语音色（9 语言 + 11 种英文风格） |

## 关键事件时间线

- 2025-08-25：开源 VibeVoice-TTS（ICLR 2026 Oral）
- 2025-09-05：因滥用（深度伪造风险）移除 VibeVoice-TTS 代码
- 2025-12-03：开源 VibeVoice-Realtime-0.5B
- 2026-01-21：开源 VibeVoice-ASR（技术报告 arXiv:2601.18184）
- 2026-03-06：ASR 集成 HuggingFace Transformers
- 2026-03-12：ASR 集成 Azure AI Foundry Labs
- 2026-07-23：发布 VibeASR.cpp（BitNet CPU 推理引擎）

## 风险与限制

- 官方声明仅限研究用途，不建议未经充分测试用于商业/真实场景。
- 存在深度伪造与虚假信息滥用风险；TTS 代码下架事件即是前车之鉴。
- 基座模型可能继承 Qwen2.5 的偏差与错误。

## 实用价值判断

差异化优势：长音频单次处理 + 说话人分离（对比 Whisper 切片 + 单独 diarization 方案会丢失全局上下文）。实用价值排序：ASR-BitNet（CPU 端到端转写）> Realtime-0.5B（低延迟 TTS）> ASR-7B（长音频会议转写）。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
