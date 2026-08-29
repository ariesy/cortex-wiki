---
pageType: entity
id: entity.project.ebook-downloader
title: ebook-downloader（Z-Library 下载器，已暂停）
entityType: project
aliases:
  - ebook-downloader
  - Z-Library 下载器
updatedAt: 2026-08-28T14:00:00.000Z
status: paused
claims:
  - id: claim.ebook-downloader.overview
    text: "ebook-downloader 功能为通过 Z-Library 搜索并下载电子书，支持多格式，自动按作者整理到 NAS；存储路径 /mnt/nas/ariesy/Drive/onedrive/电子书，格式优先级 EPUB > PDF > Mobi > Azw3。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-ebook-downloader-council-review-ad5e8a2c
        weight: 0.9
  - id: claim.ebook-downloader.paused
    text: "项目状态为**暂停**（2026-04-19 评审后暂停，2026-05-05 记录确认、2026-07-26 再次确认仍在暂停）。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-ebook-downloader-council-review-ad5e8a2c
        weight: 0.9
        note: 评审当日标记暂停
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-95ad15ec
        weight: 0.85
        note: 后续确认仍暂停
  - id: claim.ebook-downloader.zlib-risk
    text: "Council of the Wise 评审的核心结论：SPEC v0.1.0 架构可扩展性良好，但 Z-Library 单点依赖是最大风险（该站已被美国政府查处两次），建议把域名变动作为一等公民处理，并将格式优先级移至配置层。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-ebook-downloader-council-review-ad5e8a2c
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-19-ebook-downloader-council-review-ad5e8a2c.md
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-95ad15ec.md

---
# ebook-downloader（Z-Library 下载器，已暂停）

> **状态：暂停**（2026-04-19 起，至 2026-07 仍未恢复）

## 项目概述

| 项 | 值 |
|----|-----|
| 功能 | 通过 Z-Library 搜索下载电子书，多格式，按作者自动整理到 NAS |
| 存储 | `/mnt/nas/ariesy/Drive/onedrive/电子书` |
| 格式优先级 | EPUB > PDF > Mobi > Azw3 |
| 状态 | ⏸ 暂停 |

## Council of the Wise 评审结论

**Synthesis（综合裁决）**：

- SPEC v0.1.0 整体设计扎实，架构可扩展性良好 ✅
- ⚠️ **Z-Library 单点依赖是最大风险** —— 该站已被美国政府查处两次
- 建议：把**域名变动作为一等公民**处理（硬编码域名必然失效）
- 建议：格式优先级**移至配置层**，不要写死在代码里

## 暂停原因

核心依赖 Z-Library 的可用性风险无法在架构层面消除，评审后决定暂停。

## 相关

- [[ebook-manager]] — 独立的书库管理项目，**仍在活跃**（勿与本项目混淆）
- [[council-of-the-wise技能]] — 本评审使用的评审框架

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [ebook-manager（Calibre 管理工具）](ebook-manager.md)
- [VM git clone GitHub 间歇性 TLS 失败](git-clone-tls-issue.md)
<!-- openclaw:wiki:related:end -->
