---
pageType: entity
id: entity.project.clash-traffic-scripts-refactor
title: Clash 流量统计脚本重构
entityType: project
aliases:
  - clash scripts
  - traffic_poll.py
  - traffic_query.py
updatedAt: 2026-08-28T14:50:00.000Z
status: active
claims:
  - id: claim.clash-refactor.utils-module
    text: "重构抽出共享模块 `scripts/utils.py`，统一提供 `format_bytes()` 和 `get_db_path()`，消除 traffic_poll.py / traffic_query.py / clash.py 三处的重复实现（原本各有本地 `_format_bytes()` 等副本）。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-23-clash-scripts-refactor-90343969
        weight: 0.85
  - id: claim.clash-refactor.trafficdb-context-manager
    text: "用 `TrafficDB` 上下文管理器替代手动 `conn.close()`，解决连接未关闭与未使用变量问题。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-23-clash-scripts-refactor-90343969
        weight: 0.85
  - id: claim.clash-refactor.dead-code-fix
    text: "traffic_poll.py 的 `split_across_hours()` 存在死代码（103-127 行），原因是条件写成 `< 1.0` 使 else 分支永不可达，改为 `< 0.999` 后分支可达；同时时区统一为 UTC+8 与 traffic_query.py 对齐。"
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-23-clash-scripts-refactor-90343969
        weight: 0.85
  - id: claim.clash-refactor.skillmd-token-hardcode
    text: "SKILL.md 中存在 Token 硬编码问题，需手动把真实 Token 替换为占位符 `YOUR_TOKEN_HERE`，不要把真实凭证留在文档里——这一项自动化重构未覆盖，属于需人工处理的遗留项。"
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-23-clash-scripts-refactor-90343969
        weight: 0.8
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-23-clash-scripts-refactor-90343969.md

---
# Clash 流量统计脚本重构

Clash 流量统计相关 Python 脚本的代码质量重构（2026-04-23）。

## 涉及文件

| 文件 | 主要改动 |
|------|---------|
| `scripts/utils.py` | **新建** 共享工具模块：`format_bytes()`、`get_db_path()` |
| `traffic_poll.py` | 修死代码、时区改 UTC+8、`TrafficDB` 上下文管理器、改用共享 `get_db_path()` |
| `traffic_query.py` | `TrafficDB` 上下文管理器、移除本地 `format_bytes()`/`get_db_path()` |
| `clash.py` | 用 `ClashAPIError` 异常替代 `sys.exit()`、移除本地 `_format_bytes()`、参数 `format` 改名 `output_format`、去掉不必要的 `getattr`、硬编码路径改用共享函数 |

## 值得注意的细节

- **死代码判定**：`split_across_hours()` 的条件 `< 1.0` 让 else 分支不可达，改成 `< 0.999`。浮点数等值比较是这类 bug 的常见来源。
- **内置函数遮蔽**：`format` 作为参数是 Python 常见代码异味，改名为 `output_format`。
- **时区一致性**：traffic_poll 与 traffic_query 必须同为 UTC+8，否则跨小时统计会错位。

## 遗留项

- ⚠️ **SKILL.md 的 Token 硬编码**需要人工处理，替换为 `YOUR_TOKEN_HERE`。自动化重构不碰凭证类内容，提交前务必自行检查。

## 相关

- [[clashman-skill]] — 同属 Clash/代理运维领域

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
