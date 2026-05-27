#!/usr/bin/env python3
"""Add claims and relationships to entity wiki files."""

import os
import re
import yaml

ENTITIES_DIR = "/home/ariesy/.openclaw/wiki/main/entities/investments/"

ENTITIES_TO_PROCESS = [
    "161017.SZ_富国中证500增强",
    "1810.HK_小米集团",
    "300144.SZ_宋城演艺",
    "600030.SS_中信证券",
    "914.HK_海螺水泥",
    "中国神华",
    "中概互联网ETF",
    "中航沈飞",
    "中际旭创",
    "五粮液_000858",
    "京东集团",
    "储能电池ETF",
    "兆易创新",
    "兴森科技",
    "医疗ETF",
    "天孚通信",
    "招商银行",
    "民生银行_600016",
    "泡泡玛特",
    "深南电路",
    "湖北宜化",
    "生物科技ETF",
    "生益科技",
    "紫金矿业",
    "红利ETF",
    "芯片ETF",
    "阳煤化工",
]

RELATIONSHIPS_MAP = {
    "161017.SZ_富国中证500增强": [
        {"targetId": "中概互联网ETF", "targetTitle": "中概互联网ETF", "kind": "etf-component", "weight": 0.7, "note": "中证500与中概互联网指数成分有交叉，AI主题外溢"},
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.6, "note": "中小盘科技风格重叠"},
        {"targetId": "医疗ETF", "targetTitle": "医疗ETF", "kind": "etf-component", "weight": 0.5, "note": "中证500含医疗成分股"},
        {"targetId": "红利ETF", "targetTitle": "红利ETF", "kind": "etf-component", "weight": 0.5, "note": "高股息策略交叉覆盖"},
    ],
    "1810.HK_小米集团": [
        {"targetId": "中概互联网ETF", "targetTitle": "中概互联网ETF", "kind": "etf-component", "weight": 0.9, "note": "小米是港股中概互联网重要成分股"},
    ],
    "300144.SZ_宋城演艺": [
        {"targetId": "五粮液_000858", "targetTitle": "五粮液", "kind": "same-sector", "weight": 0.6, "note": "同为消费类，均受消费环境驱动"},
    ],
    "600030.SS_中信证券": [
        {"targetId": "招商银行", "targetTitle": "招商银行", "kind": "same-sector", "weight": 0.7, "note": "同为金融板块大型蓝筹"},
        {"targetId": "民生银行_600016", "targetTitle": "民生银行", "kind": "same-sector", "weight": 0.6, "note": "同为金融板块券商与银行"},
    ],
    "914.HK_海螺水泥": [
        {"targetId": "中国神华", "targetTitle": "中国神华", "kind": "same-sector", "weight": 0.5, "note": "建材与能源矿产同受宏观周期影响"},
    ],
    "中国神华": [
        {"targetId": "紫金矿业", "targetTitle": "紫金矿业", "kind": "same-sector", "weight": 0.7, "note": "能源矿业板块，高股息同类"},
        {"targetId": "红利ETF", "targetTitle": "红利ETF", "kind": "etf-component", "weight": 0.8, "note": "中国神华是红利ETF核心成分股"},
    ],
    "中概互联网ETF": [
        {"targetId": "1810.HK_小米集团", "targetTitle": "小米集团", "kind": "etf-component", "weight": 0.9, "note": "小米是港股中概互联网ETF成分股"},
        {"targetId": "京东集团", "targetTitle": "京东集团", "kind": "etf-component", "weight": 0.9, "note": "京东是港股中概互联网ETF核心成分股"},
    ],
    "中航沈飞": [
        {"targetId": "中际旭创", "targetTitle": "中际旭创", "kind": "same-sector", "weight": 0.4, "note": "同为A股军工/科技交叉概念"},
    ],
    "中际旭创": [
        {"targetId": "天孚通信", "targetTitle": "天孚通信", "kind": "supply-chain-upstream", "weight": 0.85, "note": "天孚是旭创的光器件上游供应商"},
        {"targetId": "深南电路", "targetTitle": "深南电路", "kind": "supply-chain-downstream", "weight": 0.6, "note": "深南PCB用于光模块配套"},
        {"targetId": "兴森科技", "targetTitle": "兴森科技", "kind": "supply-chain-downstream", "weight": 0.6, "note": "兴森封装基板用于光模块芯片封装"},
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.7, "note": "光模块与芯片产业链高度相关"},
    ],
    "五粮液_000858": [
        {"targetId": "招商银行", "targetTitle": "招商银行", "kind": "same-sector", "weight": 0.5, "note": "消费金融龙头，均有高股息属性"},
    ],
    "京东集团": [
        {"targetId": "中概互联网ETF", "targetTitle": "中概互联网ETF", "kind": "etf-component", "weight": 0.9, "note": "京东是港股中概互联网ETF核心成分"},
        {"targetId": "1810.HK_小米集团", "targetTitle": "小米集团", "kind": "competitor", "weight": 0.6, "note": "京东vs小米：电商与消费电子赛道重叠"},
    ],
    "储能电池ETF": [
        {"targetId": "兆易创新", "targetTitle": "兆易创新", "kind": "etf-component", "weight": 0.5, "note": "储能BMS芯片相关"},
        {"targetId": "生物科技ETF", "targetTitle": "生物科技ETF", "kind": "competitor", "weight": 0.4, "note": "同为新能源/生物科技主题ETF"},
    ],
    "兆易创新": [
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.9, "note": "兆易是芯片ETF核心成分股之一"},
        {"targetId": "深南电路", "targetTitle": "深南电路", "kind": "supply-chain-downstream", "weight": 0.5, "note": "存储芯片封装基板配套"},
        {"targetId": "兴森科技", "targetTitle": "兴森科技", "kind": "supply-chain-downstream", "weight": 0.5, "note": "封装基板用于存储芯片封装"},
    ],
    "兴森科技": [
        {"targetId": "深南电路", "targetTitle": "深南电路", "kind": "same-sector", "weight": 0.85, "note": "同为A股PCB/封装基板龙头，AI算力PCB链"},
        {"targetId": "生益科技", "targetTitle": "生益科技", "kind": "same-sector", "weight": 0.7, "note": "PCB/覆铜板产业链"},
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.8, "note": "兴森是芯片ETF成分股"},
    ],
    "医疗ETF": [
        {"targetId": "生物科技ETF", "targetTitle": "生物科技ETF", "kind": "same-sector", "weight": 0.7, "note": "医疗与生物科技主题高度重叠"},
    ],
    "天孚通信": [
        {"targetId": "中际旭创", "targetTitle": "中际旭创", "kind": "supply-chain-downstream", "weight": 0.85, "note": "天孚是旭创的光器件上游供应商"},
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.6, "note": "光器件与芯片产业链相关"},
    ],
    "招商银行": [
        {"targetId": "民生银行_600016", "targetTitle": "民生银行", "kind": "same-sector", "weight": 0.8, "note": "同为港股银行，资产质量对比"},
        {"targetId": "红利ETF", "targetTitle": "红利ETF", "kind": "etf-component", "weight": 0.8, "note": "招行是红利ETF高股息成分股"},
    ],
    "民生银行_600016": [
        {"targetId": "招商银行", "targetTitle": "招商银行", "kind": "same-sector", "weight": 0.8, "note": "同为港股银行，资产质量对比"},
        {"targetId": "红利ETF", "targetTitle": "红利ETF", "kind": "etf-component", "weight": 0.7, "note": "民生银行是高股息港股代表"},
    ],
    "泡泡玛特": [
        {"targetId": "五粮液_000858", "targetTitle": "五粮液", "kind": "same-sector", "weight": 0.5, "note": "同为消费类，高端化逻辑对比"},
    ],
    "深南电路": [
        {"targetId": "兴森科技", "targetTitle": "兴森科技", "kind": "same-sector", "weight": 0.85, "note": "AI算力PCB链核心成员，同为PCB/封装基板龙头"},
        {"targetId": "生益科技", "targetTitle": "生益科技", "kind": "same-sector", "weight": 0.7, "note": "PCB产业链上下游"},
        {"targetId": "中际旭创", "targetTitle": "中际旭创", "kind": "supply-chain-downstream", "weight": 0.6, "note": "深南PCB用于光模块配套"},
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.8, "note": "深南是芯片ETF成分股"},
    ],
    "湖北宜化": [
        {"targetId": "阳煤化工", "targetTitle": "阳煤化工", "kind": "same-sector", "weight": 0.8, "note": "同为煤化工/磷化工，周期联动强"},
    ],
    "生物科技ETF": [
        {"targetId": "医疗ETF", "targetTitle": "医疗ETF", "kind": "same-sector", "weight": 0.7, "note": "生物科技与医疗健康主题高度重叠"},
    ],
    "生益科技": [
        {"targetId": "深南电路", "targetTitle": "深南电路", "kind": "same-sector", "weight": 0.7, "note": "同为PCB/覆铜板产业链"},
        {"targetId": "兴森科技", "targetTitle": "兴森科技", "kind": "same-sector", "weight": 0.7, "note": "PCB/覆铜板产业链"},
        {"targetId": "芯片ETF", "targetTitle": "芯片ETF", "kind": "etf-component", "weight": 0.6, "note": "高频高速CCL用于芯片产业链"},
    ],
    "紫金矿业": [
        {"targetId": "中国神华", "targetTitle": "中国神华", "kind": "same-sector", "weight": 0.7, "note": "能源矿业板块，高股息同类"},
        {"targetId": "红利ETF", "targetTitle": "红利ETF", "kind": "etf-component", "weight": 0.8, "note": "紫金是红利ETF成分股（黄金铜业高股息）"},
    ],
    "红利ETF": [
        {"targetId": "招商银行", "targetTitle": "招商银行", "kind": "etf-component", "weight": 0.9, "note": "招行是红利ETF核心成分股"},
        {"targetId": "中国神华", "targetTitle": "中国神华", "kind": "etf-component", "weight": 0.9, "note": "中国神华是红利ETF核心成分股"},
        {"targetId": "紫金矿业", "targetTitle": "紫金矿业", "kind": "etf-component", "weight": 0.8, "note": "紫金矿业是红利ETF成分股"},
        {"targetId": "民生银行_600016", "targetTitle": "民生银行", "kind": "etf-component", "weight": 0.7, "note": "民生银行是高股息港股代表"},
    ],
    "芯片ETF": [
        {"targetId": "兆易创新", "targetTitle": "兆易创新", "kind": "etf-component", "weight": 0.9, "note": "兆易是芯片ETF核心成分股"},
        {"targetId": "深南电路", "targetTitle": "深南电路", "kind": "etf-component", "weight": 0.8, "note": "深南是芯片ETF成分股"},
        {"targetId": "兴森科技", "targetTitle": "兴森科技", "kind": "etf-component", "weight": 0.8, "note": "兴森是芯片ETF成分股"},
        {"targetId": "中际旭创", "targetTitle": "中际旭创", "kind": "etf-component", "weight": 0.7, "note": "光模块与芯片产业链高度相关"},
    ],
    "阳煤化工": [
        {"targetId": "湖北宜化", "targetTitle": "湖北宜化", "kind": "same-sector", "weight": 0.8, "note": "同为煤化工，周期联动强"},
    ],
}


def parse_file(file_path):
    """Parse a wiki entity file. Returns (fm_dict, body_text, end_of_fm_pos)."""
    with open(file_path, "rb") as f:
        raw = f.read()

    # The file may contain non-UTF-8 bytes or be UTF-8. Decode what we can.
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", errors="replace")

    # Find opening ---
    m = re.match(r"^---\n", text, re.MULTILINE)
    if not m:
        return None, text, 0
    start = m.start()  # 0
    end_of_start_marker = m.end()  # len("---\n")

    # Find closing --- by searching for \n---\n or end-of-file after a line that is just ---
    # Strategy: split by lines, find line index of closing ---
    lines = text.split("\n")
    closing_line_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "---" and i > 0:
            closing_line_idx = i
            break

    if closing_line_idx is None:
        return None, text, len(text)

    # frontmatter text: lines 1 to closing_line_idx-1
    fm_lines = lines[1:closing_line_idx]
    fm_text = "\n".join(fm_lines)

    # body text: everything after closing --- + newline
    body_start_char = sum(len(l) + 1 for l in lines[:closing_line_idx + 1])
    # handle \r\n vs \n
    body_text = text[body_start_char:]
    if body_text.startswith("\n"):
        body_text = body_text[1:]

    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        print(f"    YAML parse warning: {e}")
        fm = None

    return fm, body_text, body_start_char


def build_claims(ticker, entity_name, fm):
    claims = []
    claim_id_base = f"claim.{ticker}"

    entity_type = fm.get("entity_type", "")
    is_etf = entity_type == "investment_etf"

    # ---- ETF ----
    if is_etf:
        if "中概互联网ETF" in entity_name:
            claims.append({"id": f"{claim_id_base}.ai-infrastructure", "text": "中概互联网ETF持仓腾讯阿里等AI基础设施龙头，受益于中国AI重估", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "research-report", "sourceId": "source.research.中概互联网ETF", "path": "research/中概互联网ETF/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.valuation-low", "text": "当前较52周高点回撤30%，估值处于历史中低水位", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.中概互联网ETF", "path": "research/中概互联网ETF/", "lines": "current_view", "weight": 0.7}]})
        elif "红利ETF" in entity_name:
            claims.append({"id": f"{claim_id_base}.dividend-yield", "text": "跟踪中证红利指数，股息率约4.9%，显著优于无风险利率", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "financial-data", "sourceId": "source.research.红利ETF", "path": "research/红利ETF/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.macd-divergence", "text": "PE 8.85倍处于3年历史高位，MACD顶背离风险，上行空间受限", "status": "supported", "confidence": 0.75, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.红利ETF", "path": "research/红利ETF/", "lines": "current_view", "weight": 0.7}]})
        elif "芯片ETF" in entity_name:
            claims.append({"id": f"{claim_id_base}.localization", "text": "国产替代逻辑强劲，受益于政策支持半导体自主可控", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "industry-data", "sourceId": "source.research.芯片ETF", "path": "research/芯片ETF/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.rsi-overbought", "text": "RSI 71.88接近超买，短期回调风险高，建议减持锁定利润", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.芯片ETF", "path": "research/芯片ETF/", "lines": "current_view", "weight": 0.7}]})
        elif "储能电池ETF" in entity_name:
            claims.append({"id": f"{claim_id_base}.battery-demand", "text": "新能源电池产业链长期受益于储能需求爆发，赛道长期向好", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "industry-data", "sourceId": "source.research.储能电池ETF", "path": "research/储能电池ETF/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.risk-reward", "text": "MACD柱状图衰减超90%，RSI顶背离，上行空间仅2.6%但下行风险3.7%，风险回报比不利", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.储能电池ETF", "path": "research/储能电池ETF/", "lines": "current_view", "weight": 0.8}]})
        elif "医疗ETF" in entity_name:
            claims.append({"id": f"{claim_id_base}.valuation-low", "text": "跟踪中证医疗指数，估值处于历史低位，中长期配置价值显现", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.医疗ETF", "path": "research/医疗ETF/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.bear-market", "text": "200日均线压制明显，长期空头格局未改，短期技术面空方占优", "status": "supported", "confidence": 0.75, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.医疗ETF", "path": "research/医疗ETF/", "lines": "current_view", "weight": 0.7}]})
        elif "生物科技ETF" in entity_name:
            claims.append({"id": f"{claim_id_base}.valuation-low", "text": "跟踪中证生物科技主题指数，处于历史低位区域，长线吸引力显现", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.生物科技ETF", "path": "research/生物科技ETF/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.us-biotech-risk", "text": "美国生物安全法案是悬而未决的灰犀牛，对CXO/生物科技出口有潜在冲击", "status": "supported", "confidence": 0.7, "evidence": [{"kind": "industry-data", "sourceId": "source.research.生物科技ETF", "path": "research/生物科技ETF/", "lines": "current_view", "weight": 0.7}]})
        elif "富国中证500" in entity_name:
            claims.append({"id": f"{claim_id_base}.mid-cap-tech", "text": "中证500指数增强策略，长期超额收益稳定，指数估值合理，适合定投或分批配置", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.161017", "path": "research/ETF/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.ai-spillover", "text": "全球AI热潮外溢利好中盘科技股，指数增强策略历史年化超额收益3%-8%", "status": "supported", "confidence": 0.75, "evidence": [{"kind": "industry-data", "sourceId": "source.research.161017", "path": "research/ETF/", "lines": "current_view", "weight": 0.7}]})
    else:
        # ---- Individual Stocks ----
        if "小米" in entity_name:
            claims.append({"id": f"{claim_id_base}.su7-scaling", "text": "SU7订单突破7万辆，4月交付量环比增长，汽车业务规模化交付数据验证中", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.小米", "path": "research/小米/", "lines": "catalysts", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.oversold", "text": "从高点腰斩至30港元，技术面超卖但趋势极弱，等待右侧信号确认后再入场", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.小米", "path": "research/小米/", "lines": "current_view", "weight": 0.8}]})
        elif "宋城演艺" in entity_name:
            claims.append({"id": f"{claim_id_base}.trend-bearish", "text": "持续阶梯下跌，RSI深度超卖21.7但无底背离，下降通道清晰，趋势空头", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.宋城演艺", "path": "research/宋城演艺/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.summer-tourism", "text": "暑期旅游旺季预热，关注预订数据是核心催化剂", "status": "supported", "confidence": 0.7, "evidence": [{"kind": "industry-data", "sourceId": "source.research.宋城演艺", "path": "research/宋城演艺/", "lines": "catalysts", "weight": 0.7}]})
        elif "中信证券" in entity_name:
            claims.append({"id": f"{claim_id_base}.ymtc-ipo", "text": "长江存储IPO辅导启动，中信证券担任辅导机构，是重大催化剂", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "research-report", "sourceId": "source.research.中信证券", "path": "research/中信证券/", "lines": "catalysts", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.peg-undervalued", "text": "PEG仅0.17极度低估，Q1净利润暴增55%至102亿", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.中信证券", "path": "research/中信证券/", "lines": "current_view", "weight": 0.85}]})
        elif "海螺水泥" in entity_name:
            claims.append({"id": f"{claim_id_base}.net-cash", "text": "净现金600亿+，基本面优异但趋势未止跌，耐心等待技术面信号", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.海螺水泥", "path": "research/海螺水泥/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.real-estate-demand", "text": "水泥需求受房地产政策放松力度影响，是先行指标", "status": "supported", "confidence": 0.75, "evidence": [{"kind": "industry-data", "sourceId": "source.research.海螺水泥", "path": "research/海螺水泥/", "lines": "catalysts", "weight": 0.7}]})
        elif "中国神华" in entity_name:
            claims.append({"id": f"{claim_id_base}.global-top-coal", "text": "全球最大煤炭生产商，产量3.06亿吨，煤电路港航化一体化龙头，盈利稳定性强", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "financial-data", "sourceId": "source.research.中国神华", "path": "research/中国神华/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.high-dividend", "text": "高股息（~4.9%）显著优于无风险利率，防御属性突出，ROE约15%，PE约19倍", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "financial-data", "sourceId": "source.research.中国神华", "path": "research/中国神华/", "lines": "current_view", "weight": 0.9}]})
        elif "中航沈飞" in entity_name:
            claims.append({"id": f"{claim_id_base}.military-core", "text": "军工核心资产，J-35等型号预期提供长期增长逻辑，营收规模稳健", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "research-report", "sourceId": "source.research.中航沈飞", "path": "research/中航沈飞/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.pe-overvalued", "text": "营收增速3.7%无法支撑42倍PE，当前存在杀估值陷阱", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.中航沈飞", "path": "research/中航沈飞/", "lines": "current_view", "weight": 0.8}]})
        elif "中际旭创" in entity_name:
            claims.append({"id": f"{claim_id_base}.global-optical-leader", "text": "全球光模块绝对龙头，2025年全球市占率23.4%，1.6T市占率50%-70%绝对垄断", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "financial-data", "sourceId": "source.research.中际旭创", "path": "research/中际旭创/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.nvidia-supplier", "text": "英伟达Blackwell/NPO核心供应商，公募持仓32%创三年新高，A股最纯正AI算力基础设施标的", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "research-report", "sourceId": "source.research.中际旭创", "path": "research/中际旭创/", "lines": "current_view", "weight": 0.9}]})
        elif "五粮液" in entity_name:
            claims.append({"id": f"{claim_id_base}.oversold-dividend", "text": "超跌反弹+高股息价值（年度分红200亿+），但基本面右侧不清晰", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.五粮液", "path": "research/五粮液/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.price-inversion", "text": "价格倒挂+管理层空缺，基本面右侧信号不明确", "status": "supported", "confidence": 0.75, "evidence": [{"kind": "financial-data", "sourceId": "source.research.五粮液", "path": "research/五粮液/", "lines": "current_view", "weight": 0.7}]})
        elif "京东集团" in entity_name:
            claims.append({"id": f"{claim_id_base}.3c-market-loss", "text": "核心3C市场份额从60%降至不到50%，竞争优势面临侵蚀", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.京东", "path": "research/京东/", "lines": "current_view", "weight": 0.85}]})
            claims.append({"id": f"{claim_id_base}.q4-loss", "text": "Q4从盈利转为营业亏损45.46亿港元，FCF仅24.84亿港元，基本面恶化", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "financial-data", "sourceId": "source.research.京东", "path": "research/京东/", "lines": "tracking", "weight": 0.9}]})
        elif "兆易创新" in entity_name:
            claims.append({"id": f"{claim_id_base}.nor-flash-2nd", "text": "NOR Flash全球第二（18.5%），中国Fabless存储芯片龙头", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "financial-data", "sourceId": "source.research.兆易创新", "path": "research/兆易创新/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.q1-profit-523pct", "text": "2026Q1净利润暴增523%，受益于海外大厂退出利基市场", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "financial-data", "sourceId": "source.research.兆易创新", "path": "research/兆易创新/", "lines": "current_view", "weight": 0.9}]})
        elif "兴森科技" in entity_name:
            claims.append({"id": f"{claim_id_base}.fcbga-only", "text": "A股唯一具备FCBGA/ABF封装基板量产能力的厂商", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "research-report", "sourceId": "source.research.兴森科技", "path": "research/兴森科技/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.pe-extreme", "text": "PE 440x已严重透支2027-2028年乐观预期，估值泡沫明显", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.兴森科技", "path": "research/兴森科技/", "lines": "current_view", "weight": 0.8}]})
        elif "天孚通信" in entity_name:
            claims.append({"id": f"{claim_id_base}.optical-device-1st", "text": "全球光器件市占率第一（11.7%），英伟达CPO核心供应商，1.6T光引擎量产全球领先", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "financial-data", "sourceId": "source.research.天孚通信", "path": "research/天孚通信/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.pe-extreme", "text": "PE 140x+已严重透支未来2-3年增长预期，2026年中报是核心验证节点", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.天孚通信", "path": "research/天孚通信/", "lines": "current_view", "weight": 0.8}]})
        elif "招商银行" in entity_name:
            claims.append({"id": f"{claim_id_base}.dividend-support", "text": "股息率4.6%提供底部支撑，基本面无崩塌风险，可安心持有收息，等待零售不良率拐点", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.招商银行", "path": "research/招商银行/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.technical-weak", "text": "技术面死亡交叉确立，价值陷阱特征明显，需等待技术面企稳信号", "status": "supported", "confidence": 0.75, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.招商银行", "path": "research/招商银行/", "lines": "current_view", "weight": 0.7}]})
        elif "民生银行" in entity_name:
            claims.append({"id": f"{claim_id_base}.pb-extreme", "text": "PB 0.28极度低估值，股息率5%+，下跌空间有限", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "financial-data", "sourceId": "source.research.民生银行", "path": "research/民生银行/", "lines": "current_view", "weight": 0.85}]})
            claims.append({"id": f"{claim_id_base}.asset-quality", "text": "资产质量和拨备覆盖率令人担忧，信用卡不良率3.87%持续上行", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.民生银行", "path": "research/民生银行/", "lines": "tracking", "weight": 0.8}]})
        elif "泡泡玛特" in entity_name:
            claims.append({"id": f"{claim_id_base}.net-cash-strong", "text": "净现金110亿+港元，年现金流91亿，远期PE仅10倍，基本面顶级", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "financial-data", "sourceId": "source.research.泡泡玛特", "path": "research/泡泡玛特/", "lines": "tracking", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.technical-bearish", "text": "200日均线226港元压制，技术面极端弱势，与基本面形成背离，非对称机会", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.泡泡玛特", "path": "research/泡泡玛特/", "lines": "current_view", "weight": 0.8}]})
        elif "深南电路" in entity_name:
            claims.append({"id": f"{claim_id_base}.pcb-fcbga", "text": "中航工业旗下PCB+封装基板全栈能力，AI PCB量价齐升+FC-BGA国产替代", "status": "supported", "confidence": 0.9, "evidence": [{"kind": "financial-data", "sourceId": "source.research.深南电路", "path": "research/深南电路/", "lines": "current_view", "weight": 0.85}]})
            claims.append({"id": f"{claim_id_base}.profit-surge", "text": "净利润+74%超预期，但61x PE已定价较多乐观预期，2026年中报是关键验证节点", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "financial-data", "sourceId": "source.research.深南电路", "path": "research/深南电路/", "lines": "current_view", "weight": 0.8}]})
        elif "湖北宜化" in entity_name:
            claims.append({"id": f"{claim_id_base}.phosphate-top4", "text": "磷酸二铵产能126万吨全国第四，春耕旺季提供支撑", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "industry-data", "sourceId": "source.research.湖北宜化", "path": "research/湖北宜化/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.oversold", "text": "RSI 19.75严重超卖、KDJ J值-17.99，技术面反弹概率高", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.湖北宜化", "path": "research/湖北宜化/", "lines": "current_view", "weight": 0.8}]})
        elif "生益科技" in entity_name:
            claims.append({"id": f"{claim_id_base}.ccl-high-frequency", "text": "高频高速CCL（M6/M7/M8）产能释放是核心成长逻辑，AI驱动需求", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "research-report", "sourceId": "source.research.生益科技", "path": "research/生益科技/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.rsi-overbought", "text": "RSI持续80+，价格突破布林上轨，极度超买，短期回调风险高", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "technical-analysis", "sourceId": "source.research.生益科技", "path": "research/生益科技/", "lines": "current_view", "weight": 0.8}]})
        elif "紫金矿业" in entity_name:
            claims.append({"id": f"{claim_id_base}.top3-copper-gold", "text": "全球前三大铜企+最大黄金上市矿企，金铜价格高位震荡", "status": "supported", "confidence": 0.95, "evidence": [{"kind": "financial-data", "sourceId": "source.research.紫金矿业", "path": "research/紫金矿业/", "lines": "current_view", "weight": 0.9}]})
            claims.append({"id": f"{claim_id_base}.production-accel", "text": "2026-2028年铜+30%、金+50%产量加速释放周期", "status": "supported", "confidence": 0.85, "evidence": [{"kind": "industry-data", "sourceId": "source.research.紫金矿业", "path": "research/紫金矿业/", "lines": "current_view", "weight": 0.8}]})
        elif "阳煤化工" in entity_name:
            claims.append({"id": f"{claim_id_base}.loss-reduction", "text": "2024年大幅减亏60-86亿，周期底部复苏初期积极信号", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.阳煤化工", "path": "research/阳煤化工/", "lines": "current_view", "weight": 0.8}]})
            claims.append({"id": f"{claim_id_base}.pb-below1", "text": "破净严重（PB<1），战略转型进行中（氢能+绿色甲醇）", "status": "supported", "confidence": 0.8, "evidence": [{"kind": "financial-data", "sourceId": "source.research.阳煤化工", "path": "research/阳煤化工/", "lines": "current_view", "weight": 0.8}]})

    return claims


def process_entity(entity_name):
    file_path = os.path.join(ENTITIES_DIR, f"{entity_name}.md")
    if not os.path.exists(file_path):
        print(f"  SKIP (not found): {entity_name}")
        return False

    fm, body, body_pos = parse_file(file_path)
    if fm is None:
        print(f"  SKIP (no frontmatter): {entity_name}")
        return False

    ticker = str(fm.get("ticker", ""))
    entity_type = fm.get("entity_type", "")

    claims = build_claims(ticker, entity_name, fm)
    relationships = RELATIONSHIPS_MAP.get(entity_name, [])

    fm["claims"] = claims
    fm["relationships"] = relationships

    new_fm_text = yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).rstrip() + "\n"

    with open(file_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8", errors="replace")

    new_content = "---\n" + new_fm_text + "---\n" + body

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  OK: {entity_name} ({len(claims)} claims, {len(relationships)} relationships)")
    return True


def main():
    print("Processing entities...")
    count = 0
    for name in ENTITIES_TO_PROCESS:
        ok = process_entity(name)
        if ok:
            count += 1
    print(f"\nDone. Processed {count} files.")


if __name__ == "__main__":
    main()