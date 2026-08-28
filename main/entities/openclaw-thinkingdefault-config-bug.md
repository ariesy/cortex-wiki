---
pageType: entity
id: entity.bug.openclaw-thinkingdefault-config
title: thinkingDefault 配置无效导致 cron 周报发送失败
entityType: bug
aliases:
  - thinkingDefault Invalid input
  - agents.defaults.thinkingDefault
  - cron 周报发送失败
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.thinkingdefault.symptom
    text: "周报内容生成成功（`report_20260407_080243.md` 已落盘），但飞书发送阶段失败，报错 `agents.defaults.thinkingDefault: Invalid input`。生成与发送是两个独立阶段，生成成功不代表整条链路通过。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-openclaw-version-fix-7ae2027f
        weight: 0.9
  - id: claim.thinkingdefault.rootcause
    text: "根因是配置项 `agents.defaults.thinkingDefault` 的值不合法被 schema 拒绝；修复方式是直接从配置里删除 `thinkingDefault` 键。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-openclaw-version-fix-7ae2027f
        weight: 0.9
  - id: claim.thinkingdefault.timing-trap
    text: "时序陷阱：cron 在 08:02 CST 就已跑完并失败，而配置修复发生在 03:17 CST 之后——即修复时 cron 早已执行。排查「已修复但仍报错」时必须核对 cron 实际执行时刻与配置修改时刻的先后。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-openclaw-version-fix-7ae2027f
        weight: 0.85
  - id: claim.thinkingdefault.stale-config
    text: "删除 `thinkingDefault` 后脚本仍报同样错误，需进一步核对配置文件的实际内容——存在配置未真正生效（缓存/多份配置文件）的可能，改完配置必须回读验证。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-07-openclaw-version-fix-7ae2027f
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-07-openclaw-version-fix-7ae2027f.md

---
# thinkingDefault 配置无效导致 cron 周报发送失败

一次典型的「改了配置却以为没生效」排查。

## 故障链

```
周报生成成功 (report_20260407_080243.md)
        ↓
飞书发送失败：agents.defaults.thinkingDefault: Invalid input
```

## 根因

配置项 `agents.defaults.thinkingDefault` 的值不被 schema 接受 → **删除该键**即可。

## 排查要点

1. **分开看阶段**：生成成功 ≠ 发送成功，报错信息在发送阶段，别去查生成逻辑
2. **核对时序**：cron 08:02 CST 跑完，配置 03:17 CST 才修 → cron 跑的时候配置还是坏的，「修完还报错」是错觉
3. **回读配置**：删掉键之后脚本仍报错，要确认配置文件实际内容是否真的变了（缓存 / 多份配置）

## 修复后动作

配置修好后需要**手动重发**周报，cron 不会自动补偿已失败的那一轮。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
