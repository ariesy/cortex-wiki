---
pageType: entity
id: entity.bug.pptx-heading-level
title: gen_pptx_from_md.js 递归标题层级损坏 bug
entityType: bug
aliases:
  - gen_pptx_from_md 递归bug
  - PPTX 标题层级错乱
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.pptx-heading-level.symptom
    text: "`gen_pptx_from_md.js` 存在递归 bug，会把 Markdown 的标题层级错误转换/损坏（H1 被塞进代码块、章节层级塌陷），导致生成的 PPTX 结构不可用。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-heading-level-fix-pptx-6f8265b2
        weight: 0.9
  - id: claim.pptx-heading-level.workaround
    text: "绕过方案：改用现有的 `create_pptx.js` 生成 PPTX，不修 `gen_pptx_from_md.js`。create_pptx.js 行为稳定，是生成 PPTX 的可靠路径。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-heading-level-fix-pptx-6f8265b2
        weight: 0.9
  - id: claim.pptx-heading-level.expected-hierarchy
    text: "clawshare 系列文档的正确层级约定：H2 = Part 0~4，H3 = 章节编号（0. / 13.），H4 = 内容标题（一句话脉络、Step 1 等）；代码块里的 `# npm install...` 是 shell 注释不是 Markdown H1，转换时不能被当成一级标题。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-heading-level-fix-pptx-6f8265b2
        weight: 0.85
  - id: claim.pptx-heading-level.both-files
    text: "中英双语文档（clawshare_en.md 与 clawshare.md）存在完全相同的层级残留问题，修一个必须同步修另一个，否则两份产出的 PPTX 结构不一致。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-04-heading-level-fix-pptx-6f8265b2
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-04-heading-level-fix-pptx-6f8265b2.md

---
# gen_pptx_from_md.js 递归标题层级损坏 bug

Markdown → PPTX 转换链路上的坑：`gen_pptx_from_md.js` 有递归 bug，会破坏标题层级。

## 症状

- 标题层级被错误转换，`#` 出现在代码块里的内容被当成 H1
- 生成的 PPTX 大纲结构塌陷，Part/章节/内容三层关系丢失

## 解法

**不要修它** —— 直接用 `create_pptx.js` 生成。

## 正确层级约定（clawshare 文档）

| 层级 | 用途 |
|------|------|
| H2 | Part 0~4 |
| H3 | 章节编号（0. / 13.） |
| H4 | 内容标题（一句话脉络、Step 1: 等） |
| 代码块 `#` | shell 注释，**不是** Markdown 标题 |

## 双语同步

`clawshare.md` 和 `clawshare_en.md` 有同样的残留问题，必须成对修复，否则两份 PPTX 结构不一致。

## 产物去向

修复后生成的 PPTX 复制到 `/mnt/nas/ariesy/Drive/onedrive/HKEX/OpenClaw_Technical_...`

## 相关

- [[ppt-master-adapter]] — 同一 PPTX 生成链路上的另一项目
- [[pptx-skill-vs-clawhub]]

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
