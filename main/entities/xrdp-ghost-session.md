---
pageType: entity
id: entity:xrdp-ghost-session
entityType: concept
entity_type: technical_issue
privacyTier: public
name: xrdp 幽灵会话（孤儿会话进程）
aliases:
  - xrdp ghost session
  - xrdp orphan session
  - xrdp-sesman 孤儿会话
category: 系统 / 远程桌面 / Bug-根因分析
last_updated: 2026-08-10
updatedAt: 2026-11-06T13:15:51.755Z
status: diagnosed
summary: >
  xrdp 的 KillDisconnected=false（默认）+ sesman 收到终止信号时不杀会话进程，导致每次 xrdp-sesman
  重启都会把「断开但保留」的会话变成永久孤儿；孤儿进程逃逸 systemd cgroup 且占住 D-Bus 上的
  org.xfce.SessionManager，使后续登录的新会话秒退。
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-10-0019-ea1165ad
claims:
  - id: claim.entity.xrdp-ghost-session.symptom-20260810
    text: 症状：RDP 用户登录后 xfce4-session 秒退、登录失败；系统中存在一个不属于当前 xrdp-sesman 的旧
      Xorg/xfce4-session 进程（本例为 display :10，会话进程 2549933），它一直占用 D-Bus 上的
      org.xfce.SessionManager，新会话检测到已被占用即自杀。
    status: supported
    confidence: 0.85
    evidence:
      - kind: log-analysis
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-10-0019-ea1165ad
        weight: 0.9
    updatedAt: 2026-08-10T00:19:19.130Z
  - id: claim.entity.xrdp-ghost-session.root-cause-20260810
    text: 根因三层：①配置 KillDisconnected=false（xrdp 默认的断线续连），但 xrdp-sesman 0.9.x
      收到终止信号退出时不会清理其管理的会话进程，两者叠加使任何一次 sesman 重启都把「断开保留」的会话变成孤儿（本例由 Jun16 06:47
      连续 6 次 sesman 重启触发，:10 会话挂到 PID 1）；②孤儿已逃逸 systemd cgroup 管辖，后续 systemctl
      restart 杀不到；③ExecStop 用 `xrdp-sesman --kill` 依赖 pid 文件，但 pid 文件随
      RuntimeDirectory 在停止时被清空，优雅停止反复报 pid file not found，清理机制全部失效。
    status: supported
    confidence: 0.85
    evidence:
      - kind: log-analysis
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-10-0019-ea1165ad
        weight: 0.9
    updatedAt: 2026-08-10T00:19:19.130Z
  - id: claim.entity.xrdp-ghost-session.fix-20260810
    text: 处理方案（2026-08-10 给出，待用户拍板）：A（推荐，治本）在 /etc/xrdp/sesman.ini 的 [Sessions] 段设
      KillDisconnected=true + DisconnectedTimeLimit=3600（0.9.24 支持，最小 60 秒），既保留
      1 小时内断线续连又避免永久残留；B 加 cron 每小时巡检父进程非当前 sesman 的 xrdp 会话进程并清理（兜底）；C 可选修复
      ExecStop 的 pid 文件被清空问题。建议 A+B 组合；改 sesman.ini 需 root（走 docker 提权，改前备份）。
    status: proposed
    confidence: 0.75
    evidence:
      - kind: analysis
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-10-0019-ea1165ad
        weight: 0.8
    updatedAt: 2026-08-10T00:19:19.130Z
---

# xrdp 幽灵会话（孤儿会话进程）

## 一句话

`KillDisconnected=false` 的断线续连特性 + `xrdp-sesman` 退出时不杀会话进程 = 每次 sesman 重启都会留下永久孤儿会话，占住 `org.xfce.SessionManager`，导致后续 RDP 登录秒退。

## 时间线（本例，全部有日志证据）

| 时间 | 事件 |
|------|------|
| Jun12 07:10 | 系统重启，`xrdp-sesman(1456)` 随系统启动 |
| Jun13 02:12 | 从 192.168.31.86 RDP 登录 → 创建 display `:10` 会话（进程 2549933 + Xorg + xfce4-session） |
| Jun13 02:32 / 13:20 | 两次「重连到 `:10` 会话」（xrdp 会话复用），之后断开未再重连 |
| Jun16 06:47 | `xrdp-sesman` 被连续重启 6 次（06:47:26~53）→ sesman 1456 退出，会话进程 2549933 成孤儿（挂到 PID 1） |
| Jun18 / Aug01 / Aug07 | 后续多次重启 sesman 均「看不见」该孤儿 |
| Aug09 11:21 | 再次登录 → 新 xfce4-session 发现 `org.xfce.SessionManager` 被幽灵会话占用 → 秒退 → 登录失败 |

## 根因

1. **设计行为叠加**：`KillDisconnected=false`（断开保留，用于断线续连）+ sesman 0.9.x 收到终止信号不杀会话进程（意图是"服务重启别打断用户桌面"）。
2. **触发点**：任一次 sesman 重启，所有「断开但保留」的会话变无主孤儿。
3. **放大因素**：
   - 孤儿逃逸 systemd cgroup → `systemctl restart` 杀不到；
   - ExecStop 的 `xrdp-sesman --kill` 依赖 pid 文件，而 pid 文件在停止时被 systemd RuntimeDirectory 清空 → 优雅停止反复失败。

## 方案

- **A（推荐，治本）**：`/etc/xrdp/sesman.ini` `[Sessions]` 段
  ```ini
  KillDisconnected=true
  DisconnectedTimeLimit=3600   ; 断开超 1 小时自动清理（最小 60 秒）
  ```
- **B（兜底）**：cron 每小时巡检，父进程不是当前 sesman 的 xrdp 会话进程 → 清理。
- **C（可选）**：修复 ExecStop 的 pid 文件被清空问题。

建议 **A + B**；改 `sesman.ini` 需 root（docker 提权，先备份）。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-10-0019](../sources/bridge-workspace-142ea9a2-memory-2026-08-10-0019-ea1165ad.md)

### Related Pages

- [XFCE 会话冲突导致 xrdp 登录后立刻断开](xfce-xrdp-session-conflict.md)
<!-- openclaw:wiki:related:end -->
