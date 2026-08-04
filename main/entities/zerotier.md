---
pageType: entity
id: entity.tool.zerotier
entityType: tool
name: "ZeroTier"
sourceIds:
  - research/remote-networking/2026-08-03-openclaw-android-remote-connection.md
updatedAt: "2026-08-03"
---

# ZeroTier

开源 SD-WAN / 虚拟局域网组网工具，P2P 直连 + moon/planet 中继机制，免费版即可满足个人组网需求。

## 核心特性

- **P2P 组网**：通过 STUN 类技术穿透 NAT 直连，打洞失败时走中继。
- **Moon（卫星节点）/ Planet（行星节点）**：自建根服务器，原理同 Tailscale DERP；国内官方 planet 在海外，自建 moon/planet 是主流加速方案；甚至可完全自建 planet+controller，脱离官方账号。
- **DNS**：本体只提供"DNS 配置推送机制"（把 nameserver + 搜索域推给客户端），**不提供解析服务**；解析需自建 ZeroNSD（官方开源 beta 程序）或 dnsmasq/smartdns。
  - Central 配置位置：Network → Advanced → DNS 框；不接受顶级域名（需带点，如 `zt.internal`）。
  - 客户端需开启 Allow DNS：GUI 勾选或 `zerotier-cli set <nwid> allowDNS=1`。
  - **Linux 支持有限**（官方文档：managed DNS 完整支持 Windows/macOS/Android/iOS，Linux forthcoming）。

## 免费版限制

- 单网络约 25 节点上限（个人使用足够）。

## 与 Tailscale 共存

- 默认不冲突：独立虚拟网卡（`zt*` vs `tailscale0`）、不同 UDP 端口（9993 vs 41641）、独立网段。
- 冲突仅来自配置：双全隧道抢默认路由、网段重叠、DNS 抢占。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [OpenClaw Android 远程连接方案选型（Tailscale vs ZeroTier + 香港VPS加速）](../syntheses/openclaw-android-远程连接方案选型-tailscale-vs-zerotier-香港vps加速.md)
- [Tailscale](tailscale.md)
<!-- openclaw:wiki:related:end -->
