---
pageType: entity
id: wiki-lint-batch-fix-2026-08-05
title: "Wiki lint 批量修复（613 → 7 警告）"
tags: [wiki, lint, 数据治理, claims, sourceIds, wikilink, 批量修复]
updatedAt: "2026-08-05"
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-05-1524-00a64718
claims:
  - id: claim.wiki-lint-batch.conclusion
    text: "2026-08-05 wiki lint 批量修复完成：613 条警告降至 7 条、0 错误；剩余 7 条均为内容性标记（contradictions / open questions），属知识管理标注而非格式错误，保留合理。"
    status: supported
    confidence: 0.85
  - id: claim.wiki-lint-batch.broken-wikilink
    text: "断链 Broken wikilink 41 → 0：修正路径错误（`entities/syntheses/` ↔ `syntheses/entities/` 互指）、按标题匹配改为文件路径（如中宠/乖宝）、不存在的目标改为纯文本。"
    status: supported
    confidence: 0.85
  - id: claim.wiki-lint-batch.sourceid
    text: "缺 sourceIds 119 → 0：通过映射 AI Berkshire 报告路径、并从 claims evidence 中的 sourceId 反查 sources/ 补齐。"
    status: supported
    confidence: 0.8
  - id: claim.wiki-lint-batch.claims
    text: "约 40 条 claim 缺证据（`evidence: []`）已补 evidence；12 条 claim 竞争变体（两页同 id 不同文本，如小米 death-cross）与 1 条低置信度 claim 一并处理。"
    status: supported
    confidence: 0.8
  - id: claim.wiki-lint-batch.yaml-errors
    text: "最终 2 个 YAML 解析错误根因：ai-berkshire 框架文件删除 claim 后留下残留块；上证50AH 的 sourceId 值不合法。修复后错误归零。"
    status: supported
    confidence: 0.8
---

# Wiki lint 批量修复（613 → 7）

## 结果

- 修复前：613 条警告 → 修复后：**7 条警告，0 错误**
- 剩余 7 条为 contradictions / open questions 内容标记（知识管理标注，非格式问题），保留

## 分类修复明细

| 类别 | 修复前 | 修复后 | 处理方式 |
|------|--------|--------|---------|
| 断链 Broken wikilink | 41 | **0** | 修正路径错误（`entities/syntheses/` ↔ `syntheses/entities/` 互指）；标题匹配改为文件路径（中宠/乖宝）；不存在的目标改纯文本 |
| 缺 sourceIds | 119 | **0** | 映射 AI Berkshire 报告路径；从 claims evidence 的 sourceId 反查 sources/ |
| claim 缺 evidence | ~40 | 0 | 批量补 `evidence` |
| claim 竞争变体（id 冲突） | 12 | 0 | 统一 id 冲突：两页同 id 不同文本（如小米 death-cross） |
| 低置信度 claim | 1 | 0 | 复核后处理 |
| YAML 解析错误 | 2 | 0 | ai-berkshire 框架文件删 claim 残留块；上证50AH 的 sourceId 值不合法 |

## 教训

- 删除 claim 时要清理整个 YAML 块，避免残留缩进导致解析错误
- sourceId 值必须可解析，不能塞入任意文本
- claim id 需全局唯一，跨页同名会产生竞争变体

## 相关实体

- [[wiki-yaml-frontmatter-strictness-bug]]
- [[ai-berkshire-价值投资研究框架]]

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-05-1524](../sources/bridge-workspace-142ea9a2-memory-2026-08-05-1524-00a64718.md)
<!-- openclaw:wiki:related:end -->
