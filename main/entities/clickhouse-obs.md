---
pageType: entity
id: entity.clickhouse-observability
title: ClickHouse 可观测性应用
entityType: concept
updatedAt: 2026-07-03T13:00:00Z
status: active
claims:
  - id: claim.clickhouse.winning-observability
    text: ClickHouse is winning the observability wars, replacing Elasticsearch in the observability stack
    status: supported
    confidence: 0.8
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-02-1322-d13a3e17
        weight: 0.8
  - id: claim.clickhouse.opentelemetry-support
    text: OpenTelemetry Collector natively supports ClickHouse exporter, and Grafana provides mature plugin support
    status: supported
    confidence: 0.85
    evidence:
      - kind: wiki-source
        sourceId: source.bridge.workspace-142ea9a2.memory-2026-07-02-1322-d13a3e17
        weight: 0.85
sourceIds:
  - sources/bridge-workspace-142ea9a2-memory-2026-07-02-1322-d13a3e17.md
  - sources/bridge-workspace-142ea9a2-memory-2026-07-02-1322-d13a3e17.md


---
# ClickHouse 可观测性应用

ClickHouse 正在成为可观测性领域事实标准的底层数据库，逐步吞噬 Elasticsearch 份额。关键优势：SQL 查询语言可及性高于 ES DSL 和 PromQL、高吞吐追加写入、时序聚合分析性能优异。

## Related
<!-- openclaw:wiki:related:start -->
### Related Pages

- [Claude Science](claude-science.md)
- [Claude Sonnet 5](claude-sonnet-5.md)
- [技术螃蟹化 (Technocarcinization)](technocarcinization.md)
<!-- openclaw:wiki:related:end -->
