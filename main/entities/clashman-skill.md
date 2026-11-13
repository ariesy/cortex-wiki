---
pageType: entity
id: entity.tool.clashman-skill
title: clashman 技能
entityType: tool
aliases:
  - clashman
updatedAt: 2026-08-13T15:19:26.140Z
status: active
claims:
  - id: claim.clashman.origin
    text: "clashman 技能于 2026-04-06 基于需求规划创建，属于 OpenClaw 运维/网络排查类技能。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-06-clashman-test-8c8c3a8c
        weight: 0.85
  - id: claim.clashman.relocated
    text: "clashman 后续已从 main workspace 迁移到 `workspace-ops-deck/skills/` 目录，与 cf-docker-registry、ob-man、gh-tracker、openclaw-upgrade-check 等运维技能同址。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-22-0733-11f918d9
        weight: 0.85
  - id: claim.clashman.provider-lookup
    text: "排查 clashman / opencode 模型流量走向时，配置中真正的 provider 对象在 `models.providers.<id>` 下（如 opencode / opencode-go / opencode-go-responses），不是顶层 `providers`——定位模型挂载位置必须看这一层。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-16-1627-c99c35d2
        weight: 0.85
  - id: claim.clashman.openclash-allow-lan
    text: "OpenClash 运行时配置 `/etc/openclash/config.yaml` 里 `allow-lan: false` 会导致 mihomo 拒绝所有局域网设备的显式代理连接（7893 端口返回 403）。改为 true 后局域网代理恢复正常；持久化做法是在 `/etc/openclash/custom/openclash_custom_overwrite.sh` 追加 `ruby_edit \"$CONFIG_FILE\" \"[\\'allow-lan\\']\" \"true\"`，避免重启/订阅更新后被还原。显式代理带认证（Clash 用户名 + secret，secret 存在 /etc/config/openclash），局域网设备需配认证信息。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1519-c14ad605
        weight: 0.85
  - id: claim.clashman.fakeip-ipcidr-priority
    text: "fake-ip 模式下 mihomo 用解析出的真实 IP 匹配 IPCIDR 规则，而 IPCIDR 规则的命中优先于域名规则：若 Cloudflare 段（104.16.0.0/12、172.64.0.0/13）被设为 DIRECT 且排在 chatgpt.com 域名规则之前，chatgpt.com 会被强制直连导致被墙。决定性证据是 Clash `/logs` 里的 `chatgpt.com:443 match IPCIDR(172.64.0.0/13) using DIRECT`；规则 hit 为 0 且流量为 0 时应优先查 `/logs` 流式日志。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1519-c14ad605
        weight: 0.9
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-ebfce2b7
        weight: 0.9
  - id: claim.clashman.hk-openai-region
    text: "香港节点访问 OpenAI/ChatGPT 受地区限制（返回 403 风控页），需切美国/日本/新加坡节点；某次切到新加坡节点后主人实测可正常访问 ChatGPT。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1519-c14ad605
        weight: 0.8
  - id: claim.clashman.remote-edit-gotchas
    text: "远程改 OpenClash 配置的坑：追加内容若落在 `exit 0` 之后永不执行；`ruby_edit` 行单引号被吞会导致 Ruby 解析报错（应为 `['allow-lan']`）；busybox sed 不支持 `\x27` 转义，稳妥做法是拉回本机用 GNU sed 改再推回。OpenClash 的 secret 可能因重载配置而变更，token 失效时从 `/etc/config/openclash` / `config.yaml` 重新取。"
    status: observed
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-13-1519-c14ad605
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-06-clashman-test-8c8c3a8c.md
  - sources/bridge-workspace-142ea9a2-memory-2026-08-22-0733-11f918d9.md
  - sources/bridge-workspace-142ea9a2-memory-2026-08-16-1627-c99c35d2.md
  - sources/bridge-workspace-142ea9a2-memory-2026-08-13-1519-c14ad605.md
  - sources/bridge-workspace-142ea9a2-memory-2026-08-13-ebfce2b7.md

---
# clashman 技能

OpenClaw 运维类技能，用于代理/网络流量相关排查。

## 位置变迁

| 阶段 | 位置 |
|------|------|
| 2026-04 创建 | main workspace skills |
| 2026-08 之后 | `workspace-ops-deck/skills/` |

与 `cf-docker-registry`、`ob-man`、`gh-tracker`、`openclaw-upgrade-check` 一起迁到 ops-deck。

## 排查要点

排查 clashman / opencode 模型的流量走向时：

- **真正的 provider 对象在 `models.providers.<id>`**，而非顶层 `providers`
- 已知 provider id：`opencode`、`opencode-go`、`opencode-go-responses`
- 要确认模型挂在哪个 provider、host 指向哪里，从这一层读

## OpenClash 排障要点（2026-08-13 实战）

| 现象 | 根因 | 处理 |
|------|------|------|
| 局域网显式代理（7893）全部 403 | 运行时 `config.yaml` 的 `allow-lan: false` | 改 true + 在 `custom_overwrite` 脚本里 `ruby_edit` 持久化 |
| chatgpt.com 走直连被墙 | Cloudflare IPCIDR 段 → DIRECT 且排在域名规则前，fake-ip 下按真实 IP 匹配 | 调整规则顺序 / 收窄 DIRECT 段 |
| HK 节点 ChatGPT 403 风控页 | OpenAI 地区限制 | 切美/日/新加坡节点 |

- 定位手段：`/logs` 流式 API 看 `match IPCIDR(...) using DIRECT`；「规则 hit 0 + 流量 0」是典型信号。
- 运行时配置路径 `/etc/openclash/config.yaml`（由 `-f` 参数指定）。
- 远程编辑坑：追加内容别落到 `exit 0` 之后；busybox sed 不支持 `\x27`，拉回本机用 GNU sed 改更稳。

## 相关

- [[git-clone-tls-issue]] — 同属 VM 网络/代理排查领域

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
