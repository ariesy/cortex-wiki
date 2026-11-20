---
pageType: entity
id: entity.concept.omniroute-provider-cleanup
title: OmniRoute 失效 Provider 处理（disable 而非删除）
entityType: concept
aliases:
  - OmniRoute provider disable
  - mimocode cartesia 清理
updatedAt: "2026-08-16T06:08:26.421Z"
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-16-0608-2a08d241
claims:
  - id: claim.omniroute.provider.disable-not-delete
    text: "用户要求：失效的 provider 只做 disable（is_active=False / active=False），不删除记录。2026-08-16 对 cartesia 与 mimocode 执行该操作。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0608-2a08d241
        weight: 0.9
  - id: claim.omniroute.mimocode.invalid-by-design
    text: "mimocode 是 apikey 类型连接但 api_key 为 null，自 7/28 创建后从未成功，一直 test=error「Provider validation endpoint not supported」——本就是无效连接。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0608-2a08d241
        weight: 0.85
  - id: claim.omniroute.recovery-procedure
    text: "误删 provider 的恢复流程：先备份当前 SQLite 库，再用 better-sqlite3 从备份库取回完整记录直接 INSERT 回当前库并设 is_active=0；注意 `group` 是 SQL 保留字需加引号；改库后需重启 OmniRoute 使改动生效，再验证 active=False。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-0608-2a08d241
        weight: 0.85
---

# OmniRoute 失效 Provider 处理（disable 而非删除）

## 结论

OmniRoute 中失效的 provider 应 **disable（is_active=0）而非删除**，保留记录以便追溯或恢复。

## 2026-08-16 处理记录

| Provider | 状态 | 说明 |
|----------|------|------|
| cartesia | ✅ disabled（active=False） | 直接 PUT 更新成功 |
| mimocode | ✅ disabled（active=False） | 曾被误删，已从备份库恢复记录并设为 is_active=0 |

## 经验

- mimocode 本身无效：`api_key=null`，一直 test=error「Provider validation endpoint not supported」，从 7/28 创建起从未成功。
- 删除是破坏性操作：对用户未明确要求删除的对象，应默认 disable。
- SQLite 恢复步骤：备份当前库 → 从备份库读取完整记录 → better-sqlite3 直接 INSERT（`group` 需加引号，SQL 保留字）→ 重启 OmniRoute → 验证 active=False。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-16-0608](../sources/bridge-workspace-142ea9a2-memory-2026-08-16-0608-2a08d241.md)
<!-- openclaw:wiki:related:end -->
