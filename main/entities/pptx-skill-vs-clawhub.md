---
pageType: entity
id: entity.concept.pptx-skill-vs-clawhub
title: pptx 技能（内置）vs powerpoint-pptx（ClawHub）辨析
entityType: concept
aliases:
  - powerpoint-pptx
  - ClawHub PPT 技能
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.pptx-skill-vs-clawhub.builtin
    text: "workspace 内置的 `pptx` skill 是 OpenClaw 官方内置技能，没有上架 ClawHub，因此没有 ClawHub 评分——查不到分数不等于质量差。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-pptx-skill-analysis-537299db
        weight: 0.9
  - id: claim.pptx-skill-vs-clawhub.different
    text: "ClawHub 上评分最高的 PPT 相关技能是 `powerpoint-pptx`（3.831 分），与 workspace 内置的 `pptx` 是**两个不同的技能**：前者是社区提交的独立 skill，后者是 OpenClaw 出厂自带。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-pptx-skill-analysis-537299db
        weight: 0.9
  - id: claim.pptx-skill-vs-clawhub.positioning
    text: "两者功能定位不同：内置 `pptx` 偏向设计指南 + 生成，powerpoint-pptx 是社区方案，选型时应按定位而非评分决定。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-pptx-skill-analysis-537299db
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-04-pptx-skill-analysis-537299db.md

---
# pptx 技能（内置）vs powerpoint-pptx（ClawHub）辨析

容易混淆的两个同名概念，选型前先分清。

## 对比

| | 内置 `pptx` | ClawHub `powerpoint-pptx` |
|---|---|---|
| 来源 | OpenClaw 出厂自带 | 社区提交 |
| 位置 | `workspace/skills/pptx/` | ClawHub 市场 |
| ClawHub 评分 | **无**（未上架） | 3.831（PPT 类最高） |
| 定位 | 设计指南 + 生成 | 社区方案 |

## 结论

- 查不到评分 ≠ 质量差，内置技能根本不上架 ClawHub
- 按**功能定位**选型，不要被评分数字带偏

## 相关

- [[pptx-heading-level-bug]] — 内置 pptx 链路上的已知 bug
- [[ppt-master-adapter]]

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
