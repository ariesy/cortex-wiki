---
pageType: entity
id: entity.concept.skill-frontmatter-registration
title: SKILL.md frontmatter 与技能注册（product-req-assistant 案例）
entityType: concept
aliases:
  - product-req-assistant
  - SKILL.md frontmatter
updatedAt: 2026-08-05T15:11:28.000Z
status: active
claims:
  - id: claim.skill-frontmatter.registration-mechanism
    text: "OpenClaw 根据 SKILL.md 的 YAML front matter 中的 `name` 和 `description` 来注册技能；缺少 front matter 的技能无法被解析加载。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-skill-frontmatter-fix-a5772863
        weight: 0.9
  - id: claim.skill-frontmatter.product-req-assistant-fix
    text: "product-req-assistant 技能未正常加载的根因是 SKILL.md 缺少 YAML frontmatter（对比 blogtrottr-digest 的 SKILL.md 有 front matter）；在 SKILL.md 开头补上 name/description/user-invocable 后技能恢复正常。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-skill-frontmatter-fix-a5772863
        weight: 0.9
  - id: claim.skill-frontmatter.fix-result
    text: "修复后 product-req-assistant 进入 Eligible 与 Model Visible 列表（93 个），触发词为 `product-req-assistant`（或直接描述需求生成 PRD）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-06-skill-frontmatter-fix-a5772863
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-06-skill-frontmatter-fix-a5772863.md
---
# SKILL.md frontmatter 与技能注册

OpenClaw 技能注册机制与一个真实排障案例：`product-req-assistant` 技能无法加载。

## 根因

`product-req-assistant` 的 SKILL.md **缺少 YAML front matter**，而对比的 `blogtrottr-digest` 的 SKILL.md 有 front matter。

> OpenClaw 根据 front matter 的 `name` 和 `description` 来注册技能。缺了就无法解析、不会出现在技能列表中。

## 修复

在 `SKILL.md` 开头添加标准 frontmatter：

```yaml
---
name: product-req-assistant
description: >
  产品需求助理，帮助用户快速生成标准化的产品需求文档（PRD）和功能规格说明（Function Spec），支持全流程需求管理。
user-invocable: true
---
```

## 结果

- ✓ Eligible: 93 → 现在包含 product-req-assistant
- ✓ Model Visible: 93 → agent 可以看到此技能指令
- 可用触发词：`product-req-assistant`（或直接描述需求生成 PRD）

## 排查要点（可复用）

新建/自定义技能不被加载时，**先检查 SKILL.md 是否有 `name` + `description` frontmatter**，这是常见根因。

## 相关

- [[skills-dual-directory-discovery]] — 技能发现的双目录机制
- [[cangjie-skill]] / [[darwin-skill]] / [[nuwa-skill]] — 其他自定义技能

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
