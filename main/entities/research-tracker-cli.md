---
pageType: entity
id: entity.tool.research-tracker-cli
title: research-tracker (julians-research-tracker)
entityType: tool
aliases:
  - julians-research-tracker
  - research-tracker
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.research-tracker-cli.stack
    text: "research-tracker 的 skill 包本身只包含文档，真正的可执行代码在外部——它是一个 Go 编写的 CLI 工具（julians-research-tracker），由 1645labs (Julian) 维护，最新版本 v0.1.0，安装源为 Homebrew tap 或 go install。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-26-research-tracker-analysis-62ef41ce
        weight: 0.9
  - id: claim.research-tracker-cli.storage
    text: "数据存储在 SQLite 数据库 ~/.config/research-tracker/research.db，不与 skill 目录同址，备份/迁移时需单独处理该路径。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-26-research-tracker-analysis-62ef41ce
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-03-26-research-tracker-analysis-62ef41ce.md

---
# research-tracker (julians-research-tracker)

Go 编写的研报/研究跟踪 CLI 工具。skill 包只是文档外壳，实际二进制需另外安装。

## 技术画像

| 项 | 值 |
|----|----|
| 名称 | julians-research-tracker |
| 语言 | Go |
| 维护者 | 1645labs (Julian) |
| 最新版本 | v0.1.0 |
| 安装源 | Homebrew tap / `go install` |
| 数据库 | SQLite `~/.config/research-tracker/research.db` |

## 注意点

- 卸载 skill **不会**删除 `~/.config/research-tracker/research.db`，历史追踪数据独立于 skill 目录存在
- skill 目录内看不到可执行代码，排查行为问题要去 Go 仓库而非 skill 包

## 相关

- [[research-tracker-4week]] — 由该工具产出的 4 周研究跟踪汇总
- [[stock-research-engine-analysis]]

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
