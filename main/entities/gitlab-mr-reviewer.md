---
pageType: entity
entityType: project
id: entity.project.gitlab-mr-reviewer
title: GitLab MR Reviewer
updatedAt: 2026-11-06T13:06:36.223Z
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-07-7db58692
  - source.bridge.workspace-142ea9a2.memory-2026-08-07-1328-bc187455
claims:
  - id: claim.gitlab-mr-reviewer.2026-08-07.startup-and-arch
    text: 2026-08-07 启动 GitLab MR Reviewer 项目（agent tools 群讨论）：目标是对公司自托管
      GitLab（他部门管理）实现 AI 自动 MR review。因跨部门 webhook 协调困难，定为轮询模式（仅出站请求）。范围为组级扫描新开
      MR，并通过 SHA 变化检测新 push 后重新 review；多轮讨论能力明确后置；以 Python 包形式分发。引擎为
      pr-agent（pip
      包），以子进程方式调用并通过环境变量透传配置（OPENAI.KEY/OPENAI.BASE_URL、CONFIG.MODEL、GITLAB.URL/GITLAB.TOKEN
      等）。项目目录 projects/gitlab-mr-reviewer/，含 PROJECT.md / DESIGN.md / TODO.md /
      DECISIONS.md。待确认事项：GitLab 版本、group_id、LLM 端点类型、pr-agent 版本、部署形态、token 来源（见
      DESIGN.md §12）。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-07-7db58692
        weight: 1
    updatedAt: 2026-08-07T00:33:31.685Z
  - id: claim.gitlab-mr-reviewer.2026-08-07.pr-agent-install
    text: 2026-08-07 确认 pr-agent（Qodo/PR-Agent）安装与分发方式：① pip 安装 `pip install
      pr-agent`，PyPI 上包存在并提供 `pr-agent` 命令行入口，亦可用 `python -m pr_agent.cli
      --pr_url=... review`；② Docker 官方最推荐（webhook 模式用），镜像命名空间自 0.34.2 起由
      `codiumai/pr-agent` 迁移到 `pragent/pr-agent`，旧教程仍用旧名，升级需注意；③ 源码安装 `git clone
      https://github.com/qodo-ai/pr-agent && pip install -e .`。pr-agent
      现为社区维护项目（Qodo 的开源遗产），Qodo 主推自家 SaaS，但自托管场景使用开源版无问题、API 均可用。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-07-1328-bc187455
        weight: 1
    updatedAt: 2026-08-07T13:28:26.991Z
  - id: claim.gitlab-mr-reviewer.2026-08-07.similar-tools-and-group-scan
    text: 2026-08-07 对比同类 pip 包与 GitLab 组级扫描方案：①semgrep（pip install
      semgrep）为最值得看的替代——自托管 SAST、规则可自写、GitLab CI 跑完可将结果 comment 贴到 MR，纯静态分析不吃
      LLM API，适合硬门禁；gitlint（commit message 规范）、pre-commit（钩子框架）、ruff/mypy/bandit
      等 linter 均可 pip 安装并配合 reviewdog 或 GitLab Code Quality 贴 MR 评论；注意 reviewdog
      是 Go 二进制、danger 是 Ruby gem，都不是 pip 包。②pr-agent CLI 本身是单 MR 维度工具（一次处理一个
      --mr_url），无“扫描 group 下所有项目”的内置能力；实现组级自动化有两条成熟路径——路径 A：webhook 模式 + GitLab
      组级 webhook（零代码，推荐）；路径 B：自建轮询（本项目采用）。
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-07-1328-bc187455
        weight: 1
    updatedAt: 2026-08-07T13:28:26.991Z
---

# GitLab MR Reviewer

> 基于 pr-agent 的自托管 GitLab AI 自动 MR Review 工具（轮询模式，仅出站）

**类型:** Project
**状态:** 设计/启动阶段（2026-08-07）
**ID:** `project.gitlab-mr-reviewer`

## 背景

- 公司使用自托管 GitLab，由他部门管理
- 希望实现 AI 自动 MR review，减少人工评审负担
- 跨部门 webhook 协调难度大 → 放弃 webhook，采用**轮询模式**（仅出站请求，无需对方开放入口）

## 架构要点

| 项 | 决策 |
|---|---|
| 触发方式 | 轮询（仅出站），组级扫描新开 MR |
| 增量机制 | 检测 HEAD SHA 变化，新 push 重新 review |
| 多轮讨论 | 明确后置 |
| 分发形式 | Python 包 |
| 审查引擎 | pr-agent（pip 包），子进程调用 |
| 配置方式 | 环境变量透传（`OPENAI.KEY` / `OPENAI.BASE_URL` / `CONFIG.MODEL` / `GITLAB.URL` / `GITLAB.TOKEN`） |
| 目录 | `projects/gitlab-mr-reviewer/`（PROJECT.md / DESIGN.md / TODO.md / DECISIONS.md） |

## pr-agent 安装方式

1. **pip**：`pip install pr-agent` → 提供 `pr-agent` CLI；等价 `python -m pr_agent.cli --pr_url=... review`
2. **Docker**（官方最推荐，webhook 模式）：`pragent/pr-agent`（≥0.34.2）；≤0.31 为 `codiumai/pr-agent`
3. **源码**：`git clone https://github.com/qodo-ai/pr-agent && pip install -e .`

> 注意：pr-agent 已由 Qodo 转为社区维护项目；Qodo 主推 SaaS，但自托管用开源版可正常使用。

## 待确认事项（DESIGN.md §12）

- GitLab 版本
- group_id
- LLM 端点类型
- pr-agent 版本
- 部署形态
- token 来源

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-07](../sources/bridge-workspace-142ea9a2-memory-2026-08-07-7db58692.md)
- [Memory Bridge (main): 2026-08-07-1328](../sources/bridge-workspace-142ea9a2-memory-2026-08-07-1328-bc187455.md)
<!-- openclaw:wiki:related:end -->
