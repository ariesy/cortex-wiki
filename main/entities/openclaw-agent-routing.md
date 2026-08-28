---
pageType: entity
id: entity.concept.openclaw-agent-routing
title: OpenClaw 多 Agent 路由（bindings）配置
entityType: concept
aliases:
  - agent 路由
  - bindings
  - agents.list
updatedAt: 2026-08-28T16:05:00.000Z
status: active
claims:
  - id: claim.agent-routing.two-parts
    text: "多 Agent 路由由两部分组成：`agents.list`（定义各 agent 的 id、default 标记与独立 workspace）和 `bindings`（定义 agentId 与 match 条件的映射），两者缺一不可。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-inbox-zero-feishu-1a7a06f2
        weight: 0.9
  - id: claim.agent-routing.match-priority
    text: "binding 的 match 字段按固定优先级生效，从高到低依次为：`match.peer`（指定对话对象 kind=direct/group/channel + id）> `match.guildId`（Discord 服务器）> `match.teamId`（团队）> `match.accountId`（精确账号）> `match.accountId: \"*\"`（该渠道任意账号）> 默认 Agent 兜底。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-inbox-zero-feishu-1a7a06f2
        weight: 0.9
  - id: claim.agent-routing.feishu-example
    text: "飞书场景的典型拆分方式是按群聊/私聊路由：群聊用 `match.peer: { kind: \"group\", id: \"oc_xxx\" }` 绑到家庭/群组 agent，私聊用 `match.peer: { kind: \"direct\" }` 绑到 main agent。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-inbox-zero-feishu-1a7a06f2
        weight: 0.85
  - id: claim.agent-routing.per-agent-sandbox
    text: "单个 agent 可独立限制沙箱与工具权限：`sandbox.mode/scope/workspaceAccess`（如 all / agent / ro）配合 `tools.allow` 与 `tools.deny`，用于把受限 agent 关成只读、禁 exec。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-inbox-zero-feishu-1a7a06f2
        weight: 0.85
  - id: claim.agent-routing.doc-path
    text: "官方配置文档位于 `/home/linuxbrew/.linuxbrew/lib/node_modules/openclaw/docs/gateway/config-agents.md`，配置落地文件为 `~/.openclaw/openclaw.json`。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-05-inbox-zero-feishu-1a7a06f2
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-inbox-zero-feishu-1a7a06f2.md
---

# OpenClaw 多 Agent 路由（bindings）配置

把不同渠道/账号/会话路由到不同 agent 的机制。每个 agent 可以有自己的 workspace、沙箱等级和工具白/黑名单。

## 两块配置

```jsonc
{
  agents: {
    list: [
      { id: "home", default: true, workspace: "~/.openclaw/workspace-home" },
      { id: "work", workspace: "~/.openclaw/workspace-work" },
    ],
  },
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
  ],
}
```

## match 优先级

| 优先级 | 字段 | 说明 |
|--------|------|------|
| 1 | `match.peer` | 指定对话对象 `{ kind: direct\|group\|channel, id }` |
| 2 | `match.guildId` | Discord 服务器 ID |
| 3 | `match.teamId` | 团队 ID |
| 4 | `match.accountId` | 精确匹配账号 |
| 5 | `match.accountId: "*"` | 匹配该渠道下任意账号 |
| 6 | 默认 Agent | 兜底 |

## 飞书典型写法

```jsonc
bindings: [
  { agentId: "family", match: { channel: "feishu", peer: { kind: "group", id: "oc_xxx" } } },
  { agentId: "main", match: { channel: "feishu", peer: { kind: "direct" } } },
]
```

## Per-Agent 访问控制

```jsonc
{
  id: "restricted",
  sandbox: { mode: "all", scope: "agent", workspaceAccess: "ro" },
  tools: { allow: ["read", "sessions_list", "sessions_history"], deny: ["write", "exec", "browser"] },
}
```

## 落地注意

- 配置写入 `~/.openclaw/openclaw.json`；改前先备份（已有先例：`openclaw.json.bak-20260823-binding`），改后做 JSON 校验。
- 文档：`/home/linuxbrew/.linuxbrew/lib/node_modules/openclaw/docs/gateway/config-agents.md`

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
