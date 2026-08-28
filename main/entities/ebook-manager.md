---
pageType: entity
id: entity.project.ebook-manager
title: ebook-manager（Calibre 管理工具）
entityType: project
aliases:
  - ebook-manager
  - calibre-library
updatedAt: 2026-08-28T16:05:00.000Z
status: active
claims:
  - id: claim.ebook-manager.v220
    text: "ebook-manager v2.2.0 于 2026-04-19 实现完成，纳入了智者委员会（Council of the Wise）的评审反馈；配套文档为 PRD.md v2.2.0、FUNCTION-SPEC.md v2.2.0 与 docs/plans/2026-04-19-ebook-manager-implementation.md。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-2a2c247d
        weight: 0.9
  - id: claim.ebook-manager.paths
    text: "存储三路径：主库 /app/calibre-library（vm002 本地 SSD，追求读写速度）、备份 /mnt/nas/ariesy/Drive/onedrive/电子书/calibre（NAS SMB）、快照目录另设（用于回滚）。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-2a2c247d
        weight: 0.9
  - id: claim.ebook-manager.location
    text: "项目路径 ~/.openclaw/workspace/skills/ebook-manager/。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-19-2a2c247d
        weight: 0.9
  - id: claim.ebook-manager.manual-importer
    text: "manual_importer 是 ebook-manager 的批量导入脚本，路径 ~/.openclaw/workspace/skills/ebook-manager/scripts/manual_importer.py，用于在技能目录内以模块方式运行：先 `python3 -m scripts.manual_importer scan` 扫描预览，确认无误后 `python3 -m scripts.manual_importer import` 正式导入。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-95ad15ec
        weight: 0.9
  - id: claim.ebook-manager.importer-pipeline
    text: "manual_importer 把 NAS download 目录的电子书批量导入 Calibre，流水线含四道关卡：SHA256 去重、文件稳定性检测、Calibre 书库去重、自动启停 Content Server。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-95ad15ec
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-19-2a2c247d.md
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-95ad15ec.md

---
# ebook-manager（Calibre 管理工具）

Calibre 书库的管理技能，与 [[ebook-downloader]] 是**两个独立项目**（一个管书库，一个负责下载）。

## 版本

| 版本 | 日期 | 说明 |
|------|------|------|
| v2.2.0 | 2026-04-19 | 纳入 Council of the Wise 评审反馈后实现完成 |

## 路径

| 用途 | 路径 |
|------|------|
| 项目 | `~/.openclaw/workspace/skills/ebook-manager/` |
| 主库（本地 SSD） | `/app/calibre-library` |
| 备份（NAS SMB） | `/mnt/nas/ariesy/Drive/onedrive/电子书/calibre` |
| 快照 | 独立目录，用于回滚 |
| 导入脚本 | `skills/ebook-manager/scripts/manual_importer.py` |

## manual_importer（批量导入）

从 NAS download 目录批量导入电子书到 Calibre。以模块方式在**技能目录内**运行：

```bash
cd ~/.openclaw/workspace/skills/ebook-manager
python3 -m scripts.manual_importer scan     # 扫描预览，先确认清单
python3 -m scripts.manual_importer import   # 确认无误后正式导入
```

导入流水线（四道关卡）：

1. **SHA256 去重** — 按内容哈希剔除重复文件
2. **文件稳定性检测** — 避免导入仍在写入/传输中的半成品
3. **Calibre 书库去重** — 与已有书库比对，防止重复入库
4. **自动启停 Content Server** — 导入期间自动关闭、完成后恢复

## 配套文档

- `PRD.md` v2.2.0
- `FUNCTION-SPEC.md` v2.2.0
- `docs/plans/2026-04-19-ebook-manager-implementation.md`

## 相关

- [[ebook-downloader]] — 下载侧项目（已暂停）
- [[ebook-mobi-font-limit]] — MOBI 字体限制相关的已知问题

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [ebook-downloader（Z-Library 下载器，已暂停）](ebook-downloader.md)
<!-- openclaw:wiki:related:end -->
