---
pageType: entity
id: entity:headroom-context-engine
entityType: plugin
privacyTier: public
name: Headroom Context Engine
aliases:
  - headroom
  - headroom-openclaw
  - headroom plugin
  - headroom proxy
status: evaluated
last_updated: 2026-06-14
bestUsedFor:
  - context compression and token budget management
notEnoughFor:
  - latency-sensitive real-time chat without caching
  - short conversations with protect_recent defaults
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-06-14-headroom-true-rootcause-3ec6d942
  - source.bridge.workspace-142ea9a2.memory-2026-06-14-headroom-debug-report-7e5e08eb
relationships:
  - targetId: entity.guardians-eye
    targetTitle: guardians-eye
    kind: discovered-by
    weight: 0.8
    note: guardians-eye agent performed the headroom root cause analysis
  - targetId: entity.stock-research-engine
    targetTitle: Stock Research Engine
    kind: affected-by
    weight: 0.3
    note: Headroom's 2.4s blocking latency impacted all OpenClaw plugin hooks including SRE
claims:
  - id: claim.headroom.rootcause
    text: "Headroom plugin的assemble()钩子每次OpenClaw组装context时同步HTTP调用headroom proxy，默认protect_recent:4导致99%请求零压缩，6698次POST请求累计~16000秒阻塞，飞书响应延迟2.4秒（中位数）至63秒（峰值）"
    status: supported
    confidence: 0.95
    evidence:
      - kind: debugging-report
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-14-headroom-true-rootcause-3ec6d942
        weight: 1.0
  - id: claim.headroom.disabled
    text: "Headroom plugin已被完全卸载并清理残留（kill proxy进程+uninstall plugin+rm残留目录），用户决策不再使用"
    status: supported
    confidence: 0.95
    evidence:
      - kind: debugging-report
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-14-headroom-debug-report-7e5e08eb
        weight: 0.95
  - id: claim.headroom.design-flaw
    text: "Headroom plugin缺乏缓存机制：同样context每次都重新POST到proxy，6698次重复请求无去重无缓存。plugin没有fallback机制，assemble()是同步阻塞的await调用"
    status: supported
    confidence: 0.9
    evidence:
      - kind: debugging-report
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-06-14-headroom-true-rootcause-3ec6d942
        weight: 0.95
updatedAt: "2026-06-19T00:00:00.000Z"
---

# Headroom Context Engine Plugin

## 概述

Headroom是一个OpenClaw context engine插件，旨在压缩context窗口以管理token预算。2026-06-13安装启用后引发系统性性能问题，2026-06-14完成根因分析后卸载。

## 根因总结

**真正根因：Headroom plugin的assemble()钩子是同步HTTP阻塞调用。**

每个飞书消息进来后：
1. OpenClaw组装context
2. await contextEngine.assemble() → 同步等待2.4秒
3. await compress() → fetch POST /v1/compress
4. proxy内ContentRouter默认protect_recent:4 → 几乎所有内容都被"保护"→ 0 token节省
5. 返回tokens_saved=0 → 啥也没压缩

## 关键数据

- 6698次POST /v1/compress请求
- 平均延迟2,390ms（2.4秒），峰值63,080ms（63秒）
- tokens_saved=0（零压缩收益）
- 6次gateway.startup_failed（因非法配置字段）
- 飞书session的NO_REPLY事件

## 修复方案（已执行）

1. ✅ kill proxy进程（清理CPU消耗）
2. ✅ 完全卸载plugin：openclaw plugins uninstall headroom-openclaw
3. ✅ 清理残留配置

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-06-14-headroom-true-rootcause](../sources/bridge-workspace-142ea9a2-memory-2026-06-14-headroom-true-rootcause-3ec6d942.md)
- [Memory Bridge (main): 2026-06-14-headroom-debug-report](../sources/bridge-workspace-142ea9a2-memory-2026-06-14-headroom-debug-report-7e5e08eb.md)

### Related Pages

- [实体提取汇总 2026-06-19](../syntheses/实体提取汇总-2026-06-19.md)
<!-- openclaw:wiki:related:end -->
