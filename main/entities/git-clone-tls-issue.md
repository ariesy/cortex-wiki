---
pageType: entity
id: entity.bug.git-clone-tls-issue
title: VM git clone GitHub 间歇性 TLS 失败
entityType: bug
aliases:
  - gnutls_handshake failure
  - fetch-pack unexpected disconnect
  - SSL_ERROR_SYSCALL
  - git clone 大仓库失败
updatedAt: 2026-08-28T16:17:25.458Z
status: investigating
claims:
  - id: claim.git-tls.symptoms
    text: VM 中 git clone github.com 仓库间歇性失败，错误信息混杂且不固定：gnutls_handshake failure /
      fetch-pack unexpected disconnect / SSL_ERROR_SYSCALL——多种错误并存说明不是单一故障点。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-22-43569df6
        weight: 0.9
  - id: claim.git-tls.proxy-dead
    text: 代理 192.168.31.254:7890 本身无外网访问（curl 测试 Google 与 GitHub API 均返回
      000），所以走代理不是可行解——排查时不要把「配了代理」当成「网络能通」。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-22-43569df6
        weight: 0.9
  - id: claim.git-tls.size-threshold
    text: tcpdump 证明直连的 TLS 握手本身没问题，但大仓库传输到约 10MB 时会被服务器主动关闭连接——故障与传输体积相关，而非握手阶段。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-22-43569df6
        weight: 0.85
  - id: claim.git-tls.openssl-vs-gnutls
    text: curl/wget 直连 github.com 大部分正常，与 git 的表现不同，差异可能来自 OpenSSL 与 GnuTLS
      的实现区别——这是定位方向之一。
    status: supported
    confidence: 0.75
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-22-43569df6
        weight: 0.75
  - id: claim.git-tls.workaround
    text: 实用绕过：不用 git clone，改用 curl/wget 直接下载归档或单文件到目标路径（ppt-master-adapter
      初始化即采用此法）。
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-20-ppt-master-adapter-init-60d2c52f
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-22-43569df6.md
  - sources/bridge-workspace-142ea9a2-memory-2026-04-20-ppt-master-adapter-init-60d2c52f.md
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-95ad15ec.md
---

# VM git clone GitHub 间歇性 TLS 失败

> **状态：未完全解决**（大仓库直连传输中断问题仍在）

## 症状

`git clone` github.com 仓库间歇性失败，错误信息混杂：

```
gnutls_handshake failure
fetch-pack: unexpected disconnect
SSL_ERROR_SYSCALL
```

多种错误并存 → 不是单一故障点。

## 排查结论

| 假设 | 结论 |
|------|------|
| 走代理能通 | ❌ 代理 `192.168.31.254:7890` 本身无外网（curl Google/GitHub API 均返回 000） |
| TLS 握手有问题 | ❌ tcpdump 证明直连 TLS 握手正常 |
| 大仓库传输 | ✅ **传输到 ~10MB 时被服务器主动关闭连接** |
| 客户端 TLS 库差异 | 🤔 curl/wget（OpenSSL）直连大部分正常，git（GnuTLS）异常 |

## 未解决

直连**大仓库**传输中断的根本原因未定位。

## 绕过方案

不要用 `git clone`，改用 `curl` / `wget` 直接下载到目标路径：

```bash
curl -L <archive-url> -o /path/to/target
```

`ppt-master-adapter` 初始化即采用此法成功。

## 排查教训

- 「配了代理」≠「网络能通」，先单独验证代理本身的外网连通性
- 错误混杂时按**触发条件**（此处是传输体积）而非错误信息分类
- 对比 curl/wget 与 git 的表现差异可缩小到 TLS 实现层

## 相关

- [[ppt-master-adapter]] — 用 curl 绕过该问题完成初始化
- [[clashman-skill]] — 同属 VM 网络/代理排查领域

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [ebook-downloader（Z-Library 下载器，已暂停）](ebook-downloader.md)
- [ebook-manager（Calibre 管理工具）](ebook-manager.md)
- [ppt-master-adapter](ppt-master-adapter.md)
<!-- openclaw:wiki:related:end -->
