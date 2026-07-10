---
pageType: entity
id: entity.sub-agent-test-result-verification
title: 子 Agent 测试结果验证规则
entityType: concept
aliases:
  - Lesson A sub-agent test verification
updatedAt: 2026-07-08T14:54:13.000Z
status: active
claims:
  - id: claim.sub-agent-test-verification.rule
    text: "子 agent 自报测试结果必须父 agent 重跑验证。T6-fix 子 agent 报 27/27 unit PASS，但 7 unit fixture 仍用旧 column 名导致 pytest fail。永久规则：子 agent 完成事件包含 'tests pass' 时父 agent 必须自己跑一次 pytest 验证。"
    status: supported
    confidence: 0.98
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-08-62bf2505
        weight: 0.98
---
# 子 Agent 测试结果验证规则 (Lesson A)

Sprint 10 v1.4.0 收官期间沉淀的永久工程规则。

**规则**：子 agent 包含 "tests pass" 等完成事件时，父 agent **必须**自己跑一次 `pytest` 验证，不能只信子 agent 自报。

**案例**：T6-fix 子 agent 报 "27/27 unit PASS"，但父 agent 发现 7 unit fixture 仍用旧 column 名（symbol/index_code）导致 pytest fail → 派 T8 子 agent 一次性修完。

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
