---
pageType: entity
entityType: project
id: entity.project.cloudflare-serverless-registry-docker-mirror
title: Cloudflare Serverless Registry Docker 镜像加速
aliases:
  - Docker Registry Mirror
  - r2-registry
  - docker.zhu-kun.com
updatedAt: 2026-08-08T23:18:16.690Z
status: active
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-08-59069bf5
claims:
  - id: claim.docker-mirror.2026-08-08.deploy
    text: 2026-08-08 部署自建 Docker Registry Mirror：选型弃用已归档的 cmliu/CF-Workers-docker.io（9.2k star）与 ciiiii/cloudflare-docker-proxy（2k star），采用官方活跃维护的 cloudflare/serverless-registry（Workers + R2 完整 OCI registry，pull-through fallback，最后提交 2026-08-04）；备选 AinzRimuru/DockerProxyCF（D1 账号池抗 429）。成果：Worker `r2-registry` + R2 bucket `r2-registry`（REGISTRY binding），域名 `docker.zhu-kun.com`（DNS CNAME + Worker Route，workers.dev 被 GFW 污染不可用），USERNAME/PASSWORD secrets 认证，回源 REGISTRIES_JSON 覆盖 Docker Hub + ghcr.io + registry.k8s.io + quay.io + gcr.io；本地 nginx 容器 `docker-mirror-proxy` 监听 0.0.0.0:5000 注入 Basic Auth 转发（配置 /app/docker-mirror-proxy/nginx.conf），本机 daemon.json 使用 http://127.0.0.1:5000，局域网用 http://192.168.31.171:5000 + insecure-registries；sudoers 为 ariesy 配置 NOPASSWD 白名单（systemctl/install/docker）。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-08-59069bf5
        weight: 1.0
    updatedAt: 2026-08-08T23:18:16.690Z
  - id: claim.docker-mirror.2026-08-08.pitfalls
    text: 2026-08-08 Docker 镜像加速部署关键技术教训：①MCP OAuth 不能创建 API Token（POST /user/tokens → 9109），但 scope 含 workers-r2.write/workers-scripts.write/dns.write 足以直接完成部署；②Worker 上传必须用 Content-Type `application/javascript+module`，否则按 classic script 解析报 `Unexpected token 'export'`；③Docker registry-mirrors 不支持带认证的 mirror（moby issue #25681）——daemon 匿名探测 /v2/ 遇 401 即回退官方源（国内直连超时），解法是本地 nginx 反代注入 Basic Auth；④MCP token 刷新必须用 form-encoded（application/x-www-form-urlencoded），JSON 返回 400，且 `expires_in` 固定 3600 是生命周期非剩余时间；⑤ghcr.io token 端点拒绝 `:pull,push` 组合权限（403 DENIED），只接受单权限 `:pull`，Docker Hub 两者都接受。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-08-59069bf5
        weight: 1.0
    updatedAt: 2026-08-08T23:18:16.690Z
---

# Cloudflare Serverless Registry Docker 镜像加速

> 基于 Cloudflare Workers + R2 的自建 Docker Registry Mirror（docker.zhu-kun.com），配合本地 nginx 认证反代解决国内拉镜像问题

**类型:** Project
**状态:** 已部署（2026-08-08）
**ID:** `project.cloudflare-serverless-registry-docker-mirror`

## 架构

```
docker CLI → http://127.0.0.1:5000 (nginx: docker-mirror-proxy, 注入 Basic Auth)
           → https://docker.zhu-kun.com (Cloudflare Worker: r2-registry)
           → R2 bucket r2-registry (OCI 存储 + pull-through 缓存)
           → 回源: Docker Hub / ghcr.io / registry.k8s.io / quay.io / gcr.io
```

## 关键组件

| 组件 | 说明 |
|------|------|
| Worker | `r2-registry`（cloudflare/serverless-registry） |
| R2 bucket | `r2-registry`，REGISTRY binding |
| 域名 | `docker.zhu-kun.com`（CNAME + Worker Route） |
| 认证 | USERNAME/PASSWORD secrets（凭据 /app/serverless-registry/registry-credentials.txt） |
| 本地代理 | nginx 容器 `docker-mirror-proxy`，0.0.0.0:5000（/app/docker-mirror-proxy/nginx.conf） |
| 本机 docker | daemon.json: registry-mirrors ["http://127.0.0.1:5000"] + insecure-registries |
| 局域网 | `http://192.168.31.171:5000` |

## 选型对比

- ❌ cmliu/CF-Workers-docker.io（9.2k star，已归档，Docker Hub 429 限流 + CF ToS 风险）
- ❌ ciiiii/cloudflare-docker-proxy（2k star，已归档）
- ✅ cloudflare/serverless-registry（官方，活跃维护，Workers + R2 完整 OCI registry）
- 备选：AinzRimuru/DockerProxyCF（D1 账号池抗 429）

## 踩坑记录

1. MCP OAuth 不能创建 API Token（9109），但 scope 足以直接完成部署
2. Worker 上传必须 `application/javascript+module`
3. Docker registry-mirrors 不支持带认证的 mirror（moby #25681）→ 本地 nginx 反代注 Header
4. MCP token 刷新必须 form-encoded；`expires_in` 是生命周期不是剩余时间
5. ghcr.io token 端点只接受单权限 `:pull`，拒绝 `:pull,push`

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-08](../sources/bridge-workspace-142ea9a2-memory-2026-08-08-59069bf5.md)
<!-- openclaw:wiki:related:end -->
