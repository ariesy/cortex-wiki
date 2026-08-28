---
pageType: entity
id: entity.project.ppt-master-adapter
title: ppt-master-adapter
entityType: project
aliases:
  - ppt-master
  - ppt-master-adapter
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.ppt-master-adapter.init
    text: "ppt-master-adapter 项目于 2026-04-20 初始化完成，位置 ~/.openclaw/workspace/skills/ppt-master-adapter/，包含 ppt-master 核心代码（29 个 Python 文件 + 7 个 references）。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-20-ppt-master-adapter-init-60d2c52f
        weight: 0.9
  - id: claim.ppt-master-adapter.layout
    text: "项目目录结构：初始化产出 clawshare_ppt169_20260420/，源文档 clawshare.md 复制到 projects/sources/，另有独立的环境配置文件。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-20-ppt-master-adapter-init-60d2c52f
        weight: 0.85
  - id: claim.ppt-master-adapter.git-workaround
    text: "初始化时的取码方式：git 操作因网络不稳定失败，改用 curl 直接下载到目标路径——这是本机获取 GitHub 代码时的常用绕过手段（参见 VM git/TLS 问题）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-20-ppt-master-adapter-init-60d2c52f
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-20-ppt-master-adapter-init-60d2c52f.md

---
# ppt-master-adapter

PPTX 生成链路上的适配项目，2026-04-20 初始化。

## 项目信息

| 项 | 值 |
|----|-----|
| 路径 | `~/.openclaw/workspace/skills/ppt-master-adapter/` |
| 初始化日期 | 2026-04-20 |
| 代码规模 | 29 个 Python 文件 + 7 个 references |

## 目录结构

| 内容 | 位置 |
|------|------|
| 项目产出 | `clawshare_ppt169_20260420/` |
| 源文档 | `projects/sources/clawshare.md` |
| 环境配置 | 独立配置文件 |

## 初始化记录

- ppt-master 核心代码下载 ✅
- 项目目录初始化 ✅
- 源文档复制 ✅
- 环境配置 ✅

**取码方式**：git 操作网络不稳定 → 改用 `curl` 直接下载到正确路径。

## 相关

- [[pptx-heading-level-bug]] — 同链路的 Markdown→PPTX 转换 bug
- [[pptx-skill-vs-clawhub]] — PPTX 技能选型辨析
- [[git-clone-tls-issue]] — git 取码失败的根因

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [gen_pptx_from_md.js 递归标题层级损坏 bug](pptx-heading-level-bug.md)
- [pptx 技能（内置）vs powerpoint-pptx（ClawHub）辨析](pptx-skill-vs-clawhub.md)
- [VM git clone GitHub 间歇性 TLS 失败](git-clone-tls-issue.md)
<!-- openclaw:wiki:related:end -->
