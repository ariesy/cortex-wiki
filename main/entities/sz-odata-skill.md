---
pageType: entity
id: entity.project.sz-odata-skill
title: 深圳政府开放数据平台技能 (sz-odata)
entityType: project
aliases:
  - sz-odata
  - sz-realestate-price-tracker
  - opendata.sz.gov.cn
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.sz-odata.auth
    text: "深圳政府开放数据平台 (https://opendata.sz.gov.cn) 登录需要图形验证码，无法自动化登录；但支持 AppKey 认证方式，应走 AppKey 而非模拟登录。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-28-d139ae86
        weight: 0.9
  - id: claim.sz-odata.appkey
    text: "已获取平台 AppKey `f7cff140c68643b28d2437d98192db1b`，API 基址形如 https://opendata.sz.gov.cn/... （AppKey 属凭据，轮换后需同步更新本页）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-28-d139ae86
        weight: 0.85
  - id: claim.sz-odata.manual
    text: "平台使用指南（注册登录、数据目录、API 接口）见 projects/sz-realestate-price-tracker/docs/深圳政府开放数据用户手册.pdf。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-03-28-d139ae86
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-03-28-d139ae86.md

---
# 深圳政府开放数据平台技能 (sz-odata)

为深圳房价追踪项目 (`sz-realestate-price-tracker`) 取数而建立的取数技能。

## 关键约束

- **不能自动化登录**：登录页有图形验证码，任何基于表单/Playwright 的登录方案都不可行
- **正确路径**：使用平台 AppKey 认证调用开放 API
- 平台手册：`projects/sz-realestate-price-tracker/docs/深圳政府开放数据用户手册.pdf`

## 接入信息

| 项 | 值 |
|----|----|
| 站点 | https://opendata.sz.gov.cn |
| 认证方式 | AppKey |
| AppKey | `f7cff140c68643b28d2437d98192db1b` |

## 相关

- [[深圳购房方案A-资金测算]] — 同一批深圳本地数据需求的下游消费方

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
