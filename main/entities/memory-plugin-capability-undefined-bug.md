---
pageType: entity
id: entity.bug.memory-plugin-capability-undefined
title: memory wiki bridge import 空数组 Bug（memoryPluginState.capability 未初始化）
entityType: bug
aliases:
  - bridge import 返回空
  - memoryPluginState.capability undefined
  - wiki.bridge.import 无导入
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.memory-plugin-capability.root-cause
    text: "OpenClaw memory wiki bridge 导入返回空数组的根因是 `memoryPluginState.capability` 在 CLI 进程中为 undefined——`registerMemoryCapability()` 只在 Gateway 进程里由 memory-core plugin 初始化时调用，而 `openclaw gateway call wiki.bridge.import` 会另起一个独立的 CLI 进程，该进程没有 plugin 初始化步骤。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-27-memory-plugin-debug-c65b9de6
        weight: 0.8
  - id: claim.memory-plugin-capability.not-file-discovery
    text: "该问题与文件发现无关：测试脚本证明 271 个 artifacts 本应被导入，故障点在于 gateway 进程调用 `listActiveMemoryPublicArtifacts({ cfg })` 时读到的 capability 为空，直接返回 []。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-27-memory-plugin-debug-c65b9de6
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-27-memory-plugin-debug-c65b9de6.md

---
# memory wiki bridge import 空数组 Bug

## 现象

`openclaw gateway call wiki.bridge.import` 执行成功但导入 0 条，wiki 里看不到任何 memory artifact。

## 排查结论

**不是**文件发现问题，**是**进程隔离导致的插件状态缺失。

调用链：

```
openclaw gateway call wiki.bridge.import
  ↓ CLI 进程启动（独立于 Gateway 进程）
  ↓ 加载 memory-state 模块
  ↓ 调用 listActiveMemoryPublicArtifacts({ cfg })
  ↓ memoryPluginState.capability === undefined   ← 故障点
  ↓ 返回空数组 []
```

对比正常路径：memory-core plugin 在 **Gateway 进程**中初始化时调用 `registerMemoryCapability()`，才把 capability 写进 `memoryPluginState`。CLI 进程没有这一步。

## 排查方法（可复用）

先用一个独立测试脚本直接调用 artifact 发现逻辑，确认文件层面能列出来（本次为 271 个）。
若测试脚本能列出而 bridge 导入为 0，故障必在 `listActiveMemoryPublicArtifacts` 的 capability 依赖上，不要再往文件/路径方向查。

## 相关

- [[active-memory-integration]] — memory wiki 与 active memory 的集成配置
- [[memory-search-config]] — 同为 memory 子系统，排查时曾怀疑过 memory search 配置

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
