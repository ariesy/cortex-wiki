---
pageType: entity
entityType: bug
id: entity.bug.stubzero-google-cloud
updatedAt: "2026-05-29"
relationships:
  - targetId: entity.project.stubzero-google-cloud
    targetTitle: "stubzero-google-cloud"
    kind: affects
    weight: 0.8---


# StubZero Google Cloud RCE漏洞

> CVE-2026-2031，Google Cloud protobuf调试端点泄漏内部monorepo，漏洞赏金$148,337

**类型:** Bug  
**ID:** `bug_stubzero_google_cloud`  
**CVE:** CVE-2026-2031  
**严重性:** critical  
**赏金:** $148,337  
**来源:** Karpathy RSS 2026-05-23

---

## 漏洞概述

研究者 Arvin Shivram 的自动化模糊测试工具发现了 `cloudcrmipfrontend-pa.googleapis.com` 上的调试端点。

### 利用路径

1. `/v1/integrationPlatform:getProtoDefinition` 返回 Google 内部 monorepo (google3) 中任意 protobuf 的完整定义
2. 攻击者枚举 gRPC 服务的请求/响应结构，等同于拿到 Google 内部 API 完整蓝图
3. 利用 `X-Goog-Encode-Response-If-Executable: base64` 头绕过浏览器安全限制
4. 解析出内部工作流队列，最终实现**远程代码执行(RCE)**

---

## 关键发现

1. **protobuf定义泄漏是最高危的信息泄露** — 在 Google，一切皆 proto，泄漏即全量
2. **同一漏洞三个月后重现** — 第一次或许可以归咎于疏漏，第二次说明 Google 的修复并不彻底

---

*来源: memory/2026-05-23-1101.md (Karpathy RSS日报)*