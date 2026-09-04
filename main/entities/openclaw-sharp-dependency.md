---
pageType: entity
id: entity.bug.openclaw-sharp-dependency
title: OpenClaw sharp 依赖缺失导致图片无法查看
entityType: bug
aliases:
  - sharp 安装
  - 图片看不了
  - gateway 图片依赖
updatedAt: 2026-09-04T13:00:00.000Z
status: resolved
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-05-golden-pheasant-ffb83352.md
---

# OpenClaw sharp 依赖缺失导致图片无法查看

Gateway 缺少 `sharp` 原生图片处理依赖时，用户发来的图片无法被读取/渲染。

## 事实

| 项 | 说明 |
|----|------|
| 现象 | Gateway 无法查看用户发送的图片 |
| 根因 | 缺少 `sharp` 依赖（Node 侧高性能图像处理库，含原生二进制） |
| 修复 | 安装 sharp 依赖 |
| 生效条件 | 安装后必须**重启 Gateway** 配置才生效 |
| 验证 | 2026-05-05 安装完成后确认「sharp 已正常工作」，图片可正常查看 |

## 处理要点

- 装完依赖不等于生效：`sharp` 在 Gateway 启动时加载，**必须重启 Gateway 进程**。
- 验证方式是让 Gateway 实际读一张图片，而不是只看安装命令是否返回 0。

## 相关

- [[openclaw-ffmpeg-trusted-path]] — 同类「外部二进制/原生依赖不在位导致 Gateway 功能不可用」问题
