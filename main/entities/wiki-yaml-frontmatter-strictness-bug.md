---
pageType: entity
id: entity.bug.wiki-yaml-frontmatter-strictness
title: Wiki frontmatter 的 YAML 严格模式陷阱（js-yaml vs PyYAML）
entityType: bug
aliases:
  - "js-yaml Map keys must be unique"
  - "frontmatter 重复键 bug"
  - "frontmatter 缺闭合 ---"
  - "多行文本隐式键 bug"
updatedAt: "2026-07-31T22:59:29.136Z"
status: fixed
claims:
  - id: claim.yaml-strictness.parser-divergence
    text: "wiki lint 用的 YAML 解析器（js-yaml）比 PyYAML 严格，会报出 PyYAML 宽松模式漏掉的问题；定位此类问题必须用与 lint 同款的 js-yaml 严格模式复现，而不是靠 PyYAML 自检。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.9
  - id: claim.yaml-strictness.duplicate-key
    text: "「Map keys must be unique」的典型根因是 frontmatter 中同一键出现两次——例如 `updatedAt` 在 frontmatter 顶部有一个、在 relationships 之后又有一个（如医疗ETF.md 第 16 行与第 170 行）。PyYAML 宽松模式不报错，js-yaml 严格模式直接拒绝。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.9
  - id: claim.yaml-strictness.unclosed-frontmatter
    text: "frontmatter 只有开头 `---` 没有闭合标记时，YAML 会把整个文件当 frontmatter 解析，直到遇到 HTML 注释处才炸掉，表现为「id/pageType 找不到」（如泸州老窖_000568.md）。修法是在 sourceIds 后补上闭合 `---`。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.9
  - id: claim.yaml-strictness.multiline-scalar
    text: "多行普通文本写进 claims 的 `text:` 会被 YAML 解析为隐式键报错；单引号包多行文本（内容还含引号）同样会炸。正确写法是块标量 `text: |-`（claims）或 `current_view: |-`（多行正文）。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.9
  - id: claim.yaml-strictness.pagetype-mismatch
    text: "pageType 必须与目录及 id 前缀一致：放在 concepts/ 目录、id 用 concept 前缀的页面，pageType 写 `entity` 属类型不一致，应写 `concept`。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.85
  - id: claim.yaml-strictness.missing-standard-fields
    text: "source 页 frontmatter 若沿用大写键（Type/Title/Date）而缺标准 `id`/`pageType`，需补上标准字段（保留原有大写字段兼容）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.85
  - id: claim.yaml-strictness.outcome
    text: "2026-07-31 修复 5 个文件（concepts/deep-research-tools.md、entities/512690.SH_鹏华中证酒ETF.md、entities/医疗ETF.md、entities/泸州老窖_000568.md、sources/贵州茅台-600519-tradingagents-分析报告-2026-05-29.md）共 7 个 error，lint errors 清零（7 → 0），剩余 558 个 warnings 为非阻塞；compile 正常跑完（2230 pages）。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-31-2259-a6da728f
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-07-31-2259-a6da728f.md
---

# Wiki frontmatter 的 YAML 严格模式陷阱（js-yaml vs PyYAML）

2026-07-31 一轮 wiki lint 修复中沉淀的 frontmatter 写法陷阱：lint 用 js-yaml 严格模式，PyYAML 宽松模式会漏报，自检必须用同款解析器。

## 四类典型错误

| 错误 | 根因 | 修法 |
|------|------|------|
| `Map keys must be unique` | frontmatter 同一键出现两次（如 `updatedAt` 在顶部与 relationships 后各一个） | 删除冗余的那个 |
| id/pageType「找不到」 | frontmatter 只有开头 `---`，没有闭合标记，YAML 把整个文件当 frontmatter 解析 | 补闭合 `---` |
| claims `text:` 隐式键 | 多行普通文本写进 `text:`；或单引号包多行文本（内容还含引号） | 改用块标量 `text: \|-` |
| pageType 类型不一致 | 放在 concepts/ 目录、id 为 concept 前缀，pageType 却写 `entity` | 改为 `concept` |

另外：source 页若沿用大写键（Type/Title/Date）而缺标准字段，需补 `id`/`pageType`（保留原有大写字段兼容）。

## 修复结果（2026-07-31）

5 个文件、7 个 error 全部修复，lint errors 7 → 0（剩余 558 个 warnings 非阻塞），compile 正常（2230 pages）。

- `concepts/deep-research-tools.md` — pageType `entity` → `concept`
- `entities/512690.SH_鹏华中证酒ETF.md` — claims `text:` 改块标量
- `entities/医疗ETF.md` — `current_view` 改块标量 + 删除重复 `updatedAt`
- `entities/泸州老窖_000568.md` — 补 frontmatter 闭合 `---`
- `sources/贵州茅台-600519-tradingagents-分析报告-2026-05-29.md` — 补标准 `id`/`pageType`

**验证方式**：js-yaml 严格模式逐个复测（PyYAML 太宽松会漏报），全部通过后才跑完整 lint。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
