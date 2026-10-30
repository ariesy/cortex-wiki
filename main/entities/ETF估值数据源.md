---
pageType: entity
entityType: concept
id: entity.concept.etf-valuation-data-sources
title: ETF估值数据源
category: 投资研究/数据源
updatedAt: 2026-08-06T23:48:38.625Z
sourceIds:
  - source.bridge.workspace-142ea9a2.memory-2026-08-06-2348-dddf5f61
claims:
  - id: claim.concept.etf-valuation-data-sources.2026-08-06
    text: 2026-08-06 核查 /app/ai-berkshire 项目的 ETF 估值取数链路：项目内没有专门的 ETF 估值取数脚本，估值数据并非自动拉取，而是研究时从公开网站手动/半自动抓取后交叉验证写入报告，属自动化缺口。核心估值来源：①理杏仁 lixinger.com（主力，指数 PE-TTM/PB/股息率及历史分位）；②中证指数公司 csindex.com.cn（官方口径，股息率 4.47% 与理杏仁 4.51% 交叉验证，误差 0.9%）；③乐咕乐股 legulegu.com（历史分位辅助）；④ETF.run / baifenwei（第二口径，白酒报告理杏仁 PE 19.38 vs baifenwei 19.72，误差 1.7%，标记为口径差异可接受）。行情/基金要素：东方财富、腾讯行情 API（tools/ashare_data.py，qt.gtimg.cn，含 PE/PB）、新浪财经/新浪基金（规模、份额）、天天基金（基金要素）。美股：tools/morningstar_fair_value.py 走 Morningstar screener API（lt.morningstar.com），仅覆盖美股个股公允价值，不涉及 ETF。A股个股财务按 skills/financial-data.md 优先级：TDX 离线数据（tdx-chronos）→ 东方财富 → 巨潮资讯，该链路仅用于个股、ETF 报告未使用。
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-08-06-2348-dddf5f61
        weight: 1.0
    updatedAt: 2026-08-06T23:48:38.625Z
---

# ETF估值数据源

> ai-berkshire 项目 ETF/指数估值数据的来源与交叉验证方法（2026-08-06 核查结论）

**类型:** Concept
**ID:** `entity.concept.etf-valuation-data-sources`

## 核心结论

项目里**没有专门的 ETF 估值取数脚本**。ETF 估值数据不是自动拉取的，而是研究时从公开网站手动/半自动抓取、交叉验证后写入报告。若要自动化，目前是明确缺口。

## 估值数据源

| 来源 | 定位 | 说明 |
|------|------|------|
| 理杏仁 lixinger.com | **主力** | 指数 PE-TTM、PB、股息率及历史分位 |
| 中证指数公司 csindex.com.cn | 官方口径交叉验证 | 例：股息率 4.47% vs 理杏仁 4.51%，误差 0.9% |
| 乐咕乐股 legulegu.com | 历史分位辅助 | — |
| ETF.run / baifenwei | 第二口径 | 例：白酒 理杏仁 19.38 vs baifenwei 19.72，误差 1.7%，口径差异可接受 |

## 行情 / 基金要素

- **东方财富**、**腾讯行情 API**（`tools/ashare_data.py`，qt.gtimg.cn，含 PE/PB）
- **新浪财经 / 新浪基金**：基金规模、份额
- **天天基金**：基金要素

## 美股

- `tools/morningstar_fair_value.py` → Morningstar screener API（lt.morningstar.com）
- 仅覆盖美股个股公允价值的计算，**不涉及 ETF**

## A股个股财务（与 ETF 链路区分）

按 `skills/financial-data.md` 优先级：**TDX 离线数据（tdx-chronos）→ 东方财富 → 巨潮资讯**。该链路仅供个股使用，ETF 报告未使用。

## 一句话

**ETF 估值 = 理杏仁为主 + 中证指数公司 / 乐咕乐股 / ETF.run 交叉验证**，无自动化脚本。

## Related
<!-- openclaw:wiki:related:start -->
### Sources

- [Memory Bridge (main): 2026-08-06-2348](../sources/bridge-workspace-142ea9a2-memory-2026-08-06-2348-dddf5f61.md)
<!-- openclaw:wiki:related:end -->
