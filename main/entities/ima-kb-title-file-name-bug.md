---
pageType: entity
id: entity.bug.ima-kb-title-file-name
entityType: bug
title: IMA 知识库标题使用 create_media.file_name 而非 add_knowledge.title
aliases:
  - IMA KB 标题 bug
  - create_media file_name bug
  - 目录笔记纯图片不创建 bug
updatedAt: 2026-08-05T15:11:28.000Z
status: fixed
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4.md
claims:
  - id: claim.ima-kb-title.root-cause
    text: "根因：IMA 知识库（KB）使用 create_media 的 file_name 作为条目标题，而不是 add_knowledge 的 title；传入 add_knowledge 的 title 不生效。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.9
  - id: claim.ima-kb-title.fix
    text: "Bug 1 修复：改用 custom_name = f\"{dir_name}_{index}{ext}\" 作为 create_media 的 file_name，KB 标题即为「文件夹名_序号.扩展名」。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.9
  - id: claim.ima-kb-title.dir-note-gate
    text: "Bug 2：目录笔记创建条件为 if non_image_files:，纯图片目录（无非图片文件）不会创建目录笔记。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.9
  - id: claim.ima-kb-title.dir-note-fix
    text: "Bug 2 修复：条件改为 if non_image_files or image_files:，只要有图片或非图片文件就创建目录笔记。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.9
  - id: claim.ima-kb-title.dir-note-content
    text: "目录笔记内容包含图片媒体索引表：编号、文件名、原始路径、媒体ID，并以目录名为标题。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.85
  - id: claim.ima-kb-title.verification
    text: "修复验证：67 个测试全部通过；重新扫描 14 成功（1 目录笔记 + 9 图片 + 4 目录笔记）、0 失败；KB 标题显示为自定义名称（如 华为AI音响2_1.jpg、除螨仪uwant小精灵_3.jpg）；提交 91b066a。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.85
  - id: claim.ima-kb-title.pdf-followup
    text: "图片类型修复成功后，PDF 类型仍存在问题；后续方案是让 PDF 也走与图片相同的路径——直接上传到知识库并按「文件夹名 + 序号」命名。"
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-07-pdf-knowledge-base-fix-013ac7a4
        weight: 0.75
---

# IMA 知识库标题使用 create_media.file_name 而非 add_knowledge.title

> IMA 文件扫描上传链路中的两个 bug 与修复记录（提交 `91b066a`），影响 [IMA 文件监控扫描系统](ima-scan-system.md)。

## 根因

IMA 的 KB 使用 **`create_media` 的 `file_name`** 作为显示标题，而不是 `add_knowledge` 的 `title`。

## 两个 Bug 与修复

| Bug | 根因 | 修复 |
|-----|------|------|
| KB 标题显示原文件名 | `create_media` 的 `file_name` 用原始文件名 `file_meta.name` | 改用 `custom_name = f"{dir_name}_{index}{ext}"` 作为 `file_name` |
| 纯图片目录不创建目录笔记 | 条件 `if non_image_files:`，无非图片文件时跳过 | 改为 `if non_image_files or image_files:` |

## 验证结果

- **67 个测试全部通过** ✅
- 重新扫描：**14 成功**（1 目录笔记 + 9 图片 + 4 目录笔记），0 失败
- KB 标题自定义名生效：`华为AI音响2_1.jpg`、`除螨仪uwant小精灵_3.jpg`
- 目录笔记含图片索引表（编号 / 文件名 / 原始路径 / 媒体ID）
- 提交：`91b066a`

## 后续

图片类型修好后 PDF 类型仍有问题，计划让 PDF 同样直接上传知识库并按「文件夹名 + 序号」命名。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
