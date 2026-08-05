---
pageType: synthesis
id: synthesis.openclaw-android-远程连接方案选型-tailscale-vs-zerotier-香港vps加速
title: OpenClaw Android 远程连接方案选型（Tailscale vs ZeroTier + 香港VPS加速）
sourceIds:
  - research/remote-networking/2026-08-03-openclaw-android-remote-connection.md
status: active
updatedAt: 2026-08-03T03:21:38.907Z
---

# OpenClaw Android 远程连接方案选型（Tailscale vs ZeroTier + 香港VPS加速）

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Summary
<!-- openclaw:wiki:generated:start -->
# OpenClaw Android 远程连接方案选型（Tailscale vs ZeroTier + 香港VPS加速）

## Overview

2026-08-03 调研：主人计划在外网使用 OpenClaw Android 客户端连接 Gateway，已安装 ZeroTier，评估是否引入 Tailscale、是否自建中继加速（香港 VPS）。核心结论：局域网连接零外网依赖；远程连接需 wss:// 端点；Tailscale 因 MagicDNS 零配置更省心，但 ZeroTier 已装可用；自建中继放境外 VPS 无合规风险。

## 核心结论

### 1. OpenClaw Android 连接要求
- Android 是 companion node，必须连运行中的 Gateway（WebSocket）。
- **局域网**：mDNS 发现 + `ws://` 直连，不依赖外网。
- **远程**：需 Tailscale Serve/Funnel 或公网 TLS 的 `wss://` 端点；连接 best-effort（前台服务保活、断线自动重连、离线消息排队补发，不丢消息）。
- 不要求 gateway 固定公网 IP。

### 2. ZeroTier 与 Tailscale 共存
- 默认不冲突（独立网卡、端口 9993/41641、独立网段）。
- 冲突仅三种配置场景：双全隧道、网段重叠、DNS 抢占。

### 3. 中继机制（DERP / Moon）
- DERP（Tailscale）= P2P 打洞失败时的加密流量中继；官方无中国大陆节点，国内需自建。
- Moon/Planet（ZeroTier）= 同类机制；可完全自建 planet+controller 脱离官方账号。
- 一个香港 VPS 可同时跑 moon + derper。

### 4. 国内合规风险（账号封禁 vs 云厂商停机）
- 官方账号封禁风险 ≈ 无（DERP/moon 均为官方支持功能；Tailscale 加 `--verify-clients` 防滥用）。
- **真实风险最高的是境内 VPS 被云厂商停机**（ToS 禁代理服务）：derper（443+证书特征明显）高危，moon（UDP 9993 特征隐蔽）低危。
- 解法：中继放境外 VPS（香港/日本/新加坡），境内 VPS 只当客户端节点。

### 5. 香港 VPS 推荐（价格口径：$=美元 €=欧元 元=人民币）
- 最稳：DMIT HK CN2 GIA（$39.9/月≈287元，常缺货）
- 性价比：V.PS（€6.95/月≈54元）、VMISS、萤光云（49元/月，5天退款+免费换IP）、LightNode（$7.7/月≈55元，按小时计费）
- 省钱：vps.cat（$25/年≈15元/月）、onetechcloud（22元/月）
- 避坑：年付 $15-20 超低价多为推广小商家；先月付测晚高峰延迟再年付。

### 6. DNS 能力（关键差异）
- **Tailscale 免费版**：MagicDNS 默认开启、全平台（含 Linux）、零配置；自定义 nameserver/Split DNS 免费；限制 3 用户/100 设备、不可加任意记录（#1543）。
- **ZeroTier**：本体只推送 DNS 配置，不提供解析服务；需自建 ZeroNSD（官方 beta）或 dnsmasq；Central 不接受顶级域名；客户端需开 Allow DNS；**Linux 支持有限**。

## 决策建议

1. 优先 Tailscale：MagicDNS 零配置 + Serve 直接给 wss:// 端点，与 OpenClaw Android 官方文档契合。
2. 已有 ZeroTier 可继续用：组网能力同级，但 DNS 要自建、Linux 支持有限（gateway 为 Linux 时需手动配 resolv.conf）。
3. 无论选哪家，自建中继放香港 VPS（深圳延迟 10-30ms）。
<!-- openclaw:wiki:generated:end -->

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Tailscale](../entities/tailscale.md)
- [ZeroTier](../entities/zerotier.md)
<!-- openclaw:wiki:related:end -->
