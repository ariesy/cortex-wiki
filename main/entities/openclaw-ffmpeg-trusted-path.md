---
pageType: entity
id: entity.bug.openclaw-ffmpeg-trusted-path
title: ffmpeg 不在 OpenClaw 可信路径导致 TTS 无法转码语音消息
entityType: bug
aliases:
  - ffmpeg not found in trusted system directories
  - TTS 转码失败
  - 飞书语音消息发送失败
updatedAt: 2026-09-04T13:14:57.370Z
status: active
claims:
  - id: claim.ffmpeg-path.symptom
    text: 症状：`ffmpeg not found in trusted system directories`。ffmpeg 实际装在
      `/home/linuxbrew/.linuxbrew/bin/`（Homebrew on Linux），但 OpenClaw 的可信目录只认
      `/usr/local/bin` 和 `/usr/bin`，导致 TTS 合成出的音频无法转码为飞书原生语音消息（Opus）格式。
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-03-ffmpeg-tts-config-38961c8a
        weight: 0.9
  - id: claim.ffmpeg-path.workaround
    text: 绕过方案：不走原生语音消息，用 `[[audio_as_voice]]` 指令以 MP3 音频文件方式发送，跳过 ffmpeg
      转码。2026-05-03 已验证可用（Xiaomi TTS 合成 98KB 音频，MP3 文件成功发到飞书群）。
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-03-ffmpeg-tts-config-38961c8a
        weight: 0.9
  - id: claim.ffmpeg-path.fix
    text: 根治方案：把 ffmpeg 软链接到 `/usr/local/bin/`（需要 sudo），或 `sudo apt install ffmpeg`
      安装到系统路径。TODO 项 TSK-3A8B 已从「配置 OpenClaw TTS 功能」改为「安装 ffmpeg 并完成 OpenClaw
      TTS 配置」。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-03-ffmpeg-tts-config-38961c8a
        weight: 0.85
  - id: claim.ffmpeg-path.tts-config
    text: 已生效的 TTS
      配置：auto=tagged（显式指令触发）、provider=xiaomi、model=mimo-v2.5-tts、voice=mimo_default、format=mp3、fallback=minimax，xiaomi
      与 minimax 均已配置。
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-03-ffmpeg-tts-config-38961c8a
        weight: 0.9
  - id: claim.ffmpeg-path.installed-2026-05-05
    text: 截至 2026-05-05，ffmpeg 已就位：Linuxbrew 版本 8.0.1，路径
      /home/linuxbrew/.linuxbrew/bin/ffmpeg。用户当日明确决定**不**把 TTS auto 从 `tagged`
      改成 `always`，即保留「只有显式 [[tts:...]] 指令才发语音」的行为——不要自作主张改成每条回复都发语音。
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-searxng-google-ead00353
        weight: 0.9
        note: 用户原话：不用修改配置，只需要更新 ToDo
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-03-ffmpeg-tts-config-38961c8a.md
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-searxng-google-ead00353.md
---

# ffmpeg 不在 OpenClaw 可信路径导致 TTS 无法转码语音消息

「TTS 合成成功了但发不出去」的排查要点：**合成**和**转码**是两件事，缺 ffmpeg 卡在后者。

## 症状

```
ffmpeg not found in trusted system directories
```

## 根因

| 项 | 值 |
|---|---|
| ffmpeg 实际路径 | `/home/linuxbrew/.linuxbrew/bin/`（Linuxbrew） |
| OpenClaw 可信目录 | 仅 `/usr/local/bin`、`/usr/bin` |
| 后果 | 合成出的 MP3 无法转成飞书原生语音消息（Opus） |

> 这不是 TTS provider 的问题。Xiaomi TTS 本身工作正常（合成出 98KB 音频）。

## 绕过方案（已验证）

用 `[[audio_as_voice]]` 指令 → 以 **MP3 音频文件**方式发送，跳过 ffmpeg 转码。

2026-05-03 验证通过：音频文件成功发到飞书群，可正常播放。
代价：收到的是音频文件，不是原生语音消息气泡。

## 根治方案

- 软链接：`sudo ln -s /home/linuxbrew/.linuxbrew/bin/ffmpeg /usr/local/bin/ffmpeg`
- 或系统安装：`sudo apt install ffmpeg`

TODO `TSK-3A8B` 已相应改为「安装 ffmpeg 并完成 OpenClaw TTS 配置」。

## 当时的 TTS 配置（已生效）

| 项目 | 值 |
|---|---|
| `auto` | `tagged`（显式指令触发） |
| `provider` | `xiaomi` |
| `model` | `mimo-v2.5-tts` |
| `voice` | `mimo_default` |
| `format` | `mp3` |
| `fallback` | `minimax` |
| xiaomi / minimax | 均已配置 |

## 排查顺序

1. TTS 合成成功了吗？（看有没有生成音频文件、文件大小）
2. 失败发生在合成还是发送环节？
3. 发送环节失败 → 检查 ffmpeg 是否在可信路径
4. 一时补不上 ffmpeg → 用 `[[audio_as_voice]]` 走文件方式

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [SearXNG 本地搜索实例](searxng.md)
<!-- openclaw:wiki:related:end -->
