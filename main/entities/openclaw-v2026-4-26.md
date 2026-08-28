---
pageType: entity
id: entity.release.openclaw-v2026-4-26
title: OpenClaw v2026.4.26 版本
entityType: release
aliases:
  - OpenClaw 4.26
  - v2026.4.26
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.openclaw-4-26.release-timing
    text: "OpenClaw v2026.4.26 于 2026-04-28 发布，为稳定版（非 beta）；当时的在用版本是 v2026.4.25 (aa36ee6)，发布于 4 月 27 日。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-28-openclaw-version-check-295c7d0d
        weight: 0.85
  - id: claim.openclaw-4-26.features
    text: "v2026.4.26 主要新功能：新增 Cerebras 提供商插件；Control UI/Talk 支持浏览器实时语音对话与 Google Live 会话；Memory 支持 OpenAI-compatible 非对称 embedding 配置、Ollama 增加 Nomic/Qwen3 查询前缀；配置变更 diff 面板（JSON5、敏感值遮盖）；`openclaw matrix encryption setup` 一站式开启 Matrix E2EE；Compaction 新增可选 `maxActiveTranscriptBytes` 阈值；新增 `openclaw migrate` 支持从 Claude Code/Claude Desktop 和 Hermes 导入配置。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-28-openclaw-version-check-295c7d0d
        weight: 0.8
  - id: claim.openclaw-4-26.regressions
    text: "v2026.4.26 包含 70+ 条 Bug 修复（覆盖 Gateway 启动、插件系统/索引/安装、Ollama 兼容性、Control UI/WebChat、Feishu 卡片、Telegram、WhatsApp、Discord、Mattermost、Matrix E2EE、Memory/QMD、日志系统、A/B 测试等），同时 GitHub Issues 显示该版本存在已知回归/严重 Bug，升级前需查阅 issue 列表确认。"
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-28-openclaw-version-check-295c7d0d
        weight: 0.75
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-28-openclaw-version-check-295c7d0d.md

---
# OpenClaw v2026.4.26

发布日期 2026-04-28，稳定版。前一版本 v2026.4.25 (aa36ee6) 发布于 4/27。

## 新功能

1. **Cerebras 提供商** — 新增内置插件，含 onboarding 与模型目录
2. **Control UI/Talk** — 浏览器实时语音对话、Google Live 会话支持
3. **Memory 改进** — OpenAI-compatible 内存搜索支持非对称 embedding 配置；Ollama 内存搜索增加 Nomic/Qwen3 等模型查询前缀
4. **Control UI 增强** — 配置变更 diff 面板（JSON5、敏感值遮盖）、快速设置面板布局优化
5. **Matrix E2EE** — `openclaw matrix encryption setup` 一站式开启加密
6. **Compaction 优化** — 新增可选的 `maxActiveTranscriptBytes` 触发阈值
7. **CLI 迁移工具** — `openclaw migrate` 支持从 Claude Code / Claude Desktop 和 Hermes 导入配置

## Bug 修复

70+ 条，涉及：Gateway 启动优化、插件系统/索引/安装、Ollama 提供商兼容性、Control UI/WebChat、Feishu 卡片、Telegram、WhatsApp、Discord、Mattermost、Matrix E2EE、Memory/QMD、日志系统、A/B 测试。

## ⚠️ 已知回归

GitHub Issues 显示 4.26 引入了新的回归/严重 Bug。**升级前应先查 issue 列表**，不要假定"稳定版 = 无风险"。

## 升级检查清单（可复用）

1. 确认当前版本（`openclaw` 版本输出）
2. 拉取最新 release，确认是否稳定版
3. **查 GitHub Issues 中的 regression 标签**，评估是否影响在用功能
4. 再决定是否升级

## 相关

- [[blockStreamingDefault-config]] — 同期的飞书流式输出配置排查
- [[feishu-cardkit-400-streaming]] — 同期的飞书卡片 API 问题

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
