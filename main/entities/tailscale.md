---
pageType: entity
id: entity.tool.tailscale
entityType: tool
name: "Tailscale"
sourceIds:
  - research/remote-networking/2026-08-03-openclaw-android-remote-connection.md
updatedAt: "2026-08-03"
---

# Tailscale

基于 WireGuard 的商用组网服务（SaaS 控制平面 + 开源客户端），免费版即可满足个人远程组网需求，是 OpenClaw Android 客户端远程连接 Gateway 的官方推荐方案之一。

## 核心特性

- **MagicDNS（内部 DNS）**：免费且默认开启，设备自动获得 `机器名.tailnet名.ts.net` 域名，全平台（含 Linux）支持，零配置。
- **Tailscale Serve / Funnel**：为节点提供 `wss://` / `https://` 安全端点，是 OpenClaw Android 远程配对（非局域网）的推荐方式。
- **DERP 中继**：P2P 打洞失败时走中继（Detoured Encrypted Routing Protocol），只搬运加密流量，看不到内容；官方无中国大陆节点，国内需自建 derper 降延迟。
- **自定义 DNS**：支持自定义 nameserver / Split DNS（免费）。

## 免费版限制

- 3 用户 / 100 设备
- 不能手动添加任意 MagicDNS 记录（官方 issue #1543，付费版同样不支持）

## 国内使用要点

- 自建 DERP 属官方文档支持功能，个人自用无封号风险；加 `--verify-clients` 防止被白嫖。
- 中继服务建议放境外 VPS（香港首选），境内 VPS 跑 derper 有被云厂商停机风险（ToS 禁代理服务）。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [OpenClaw Android 远程连接方案选型（Tailscale vs ZeroTier + 香港VPS加速）](../syntheses/openclaw-android-远程连接方案选型-tailscale-vs-zerotier-香港vps加速.md)
- [ZeroTier](zerotier.md)
<!-- openclaw:wiki:related:end -->
