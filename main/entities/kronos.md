---
pageType: entity
id: entity.project.kronos
title: Kronos 金融预测模型
entityType: project
aliases:
  - Kronos
  - 601088 微调
updatedAt: 2026-08-28T14:00:00.000Z
status: active
claims:
  - id: claim.kronos.predict-future-bug
    text: "预测功能存在 bug：原代码 `y_timestamp` 取的是已知数据（行 400-499），等于在拟合已有历史而非预测未来。修复方式是改用 `pd.bdate_range` 生成未来交易日，并用 `iloc[-LOOKBACK:]` 取最近数据作为输入。提交 bc64845 —— fix(kronos): predict future dates instead of fitting existing data。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-16-721ed7eb
        weight: 0.9
  - id: claim.kronos.finetune-exp1
    text: "601088（中国神华）微调实验1参数与结果：500 条数据、lookback=50、predict=10；Tokenizer 耗时 11.4 分钟 Val Loss 0.0086，Basemodel 耗时 18.14 分钟 Val Loss 3.2260。Tokenizer 损失极低而 Basemodel 损失很高，二者量级差异显著。"
    status: supported
    confidence: 0.9
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-04-16-721ed7eb
        weight: 0.9
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-04-16-721ed7eb.md

---
# Kronos 金融预测模型

时间序列金融预测模型项目，含预训练基座 + 个股微调路线。

## 关键 Bug 与修复（2026-04-16）

**症状**：预测输出的值域/时间戳不对，模型看似"预测"实则在拟合历史。

**根因**：`y_timestamp` 取了已知数据（行 400-499），目标序列来自训练集本身。

**修复**：

```python
# 用 pd.bdate_range 生成未来交易日，而非截取已有数据
future_idx = pd.bdate_range(start=last_date, periods=PREDICT)
X = df.iloc[-LOOKBACK:]   # 输入取最近 LOOKBACK 条
```

**提交**：`bc64845` — `fix(kronos): predict future dates instead of fitting existing data`

## 601088 微调实验

### 实验 1

| 参数 | 值 |
|------|-----|
| 数据量 | 500 条 |
| lookback | 50 |
| predict | 10 |

| 阶段 | 耗时 | Val Loss |
|------|------|----------|
| Tokenizer | 11.4 min | **0.0086** |
| Basemodel | 18.14 min | **3.2260** |

**观察**：Tokenizer 侧损失极低（0.0086）而 Basemodel 侧高达 3.2260，量级差 ~375 倍。调参与效果评估应以 Basemodel 的 Val Loss 为准。

## 相关

- [[中国神华]] — 601088，本轮微调标的
- [[tdx-chronos]] — 同领域的行情数据项目

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
