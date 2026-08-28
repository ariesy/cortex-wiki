---
pageType: entity
id: entity.bug.xfce-xrdp-session-conflict
title: XFCE 会话冲突导致 xrdp 登录后立刻断开
entityType: bug
aliases:
  - xrdp 连接中断
  - mstsc 远程桌面断开
  - Window manager exited quickly
updatedAt: 2026-08-28T16:10:00.000Z
status: active
claims:
  - id: claim.xfce-xrdp.symptom
    text: "症状：用 mstsc / RDP 连接服务器，输入用户名密码后登录成功但连接立刻中断。日志特征为 `Window manager (pid <N>, display 10) exited quickly (0 secs). This could indicate a window manager config problem`。"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-02-xfce-session-conflict-15de5130
        weight: 0.9
  - id: claim.xfce-xrdp.root-cause
    text: "根因不是 Window manager 配置损坏，而是 XFCE 会话冲突：机器上已有一个通过 LightDM 启动的 XFCE 会话（display :0，长期运行），xrdp 在 display :10 启动新的 xfce4-session，新会话通过 D-Bus 检测到已有会话（`discover_other_daemon: 1`）后立即退出，窗口管理器退出导致 xrdp 断连。"
    status: confirmed
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-02-xfce-session-conflict-15de5130
        weight: 0.9
  - id: claim.xfce-xrdp.fix
    text: "修复方案 A（推荐）：停掉 LightDM 让 xrdp 独占 —— `sudo systemctl stop lightdm` 然后 kill 掉旧 xfce4-session 进程。方案 B：配置在 xrdp 连接前自动清理旧会话（更优雅但需额外配置）。执行前需确认旧会话确实无人使用。"
    status: confirmed
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-05-02-xfce-session-conflict-15de5130
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-05-02-xfce-session-conflict-15de5130.md

---
# XFCE 会话冲突导致 xrdp 登录后立刻断开

远程桌面「连上就掉」的经典误判：日志说是 window manager 配置问题，实际是**两个 XFCE 会话打架**。

## 症状

mstsc / RDP 连接 → 输入账号密码 → 认证成功 → 连接立刻中断。

日志关键行：

```
Window manager (pid 2229134, display 10) exited quickly (0 secs).
This could indicate a window manager config problem
```

## 真实根因

```
LightDM 已启动 XFCE 会话（display :0，已运行多日）  ← 元凶
        ↓
xrdp 在 display :10 启动新的 xfce4-session
        ↓
新会话通过 D-Bus 检测到已有会话（discover_other_daemon: 1）
        ↓
新 xfce4-session 立即退出 → Window manager 退出
        ↓
xrdp 断开连接
```

**注意**：`window manager config problem` 是误导性提示，不要去翻 XFCE 配置文件。

## 修复

**方案 A（推荐）** — 停掉 LightDM，让 xrdp 独占：

```bash
sudo systemctl stop lightdm
kill <旧 xfce4-session pid>   # 如 4475
```

**方案 B** — 配置在 xrdp 连接前自动清理旧会话（更优雅，需额外配置）。

⚠️ 执行方案 A 前必须确认旧会话确实没人在用（本例中旧会话已空跑 9 天，用户一直在用 xrdp）。

## 排查路径

1. 看 xrdp / xrdp-sesman 日志，定位 `exited quickly`
2. 检查是否已有残留 display :0 的 XFCE 会话（`ps` + 检查启动时间）
3. 确认 `discover_other_daemon: 1` 出现在 D-Bus 日志中
4. 停旧会话前先向用户确认

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
