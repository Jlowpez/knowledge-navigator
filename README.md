# knowledge-navigator

> A RAG agent that answers questions against any document corpus with citations.

![CI](https://github.com/Jlowpez/knowledge-navigator/actions/workflows/ci.yml/badge.svg)
![Phase](https://img.shields.io/badge/phase-1__active-8b5cf6)
![Python](https://img.shields.io/badge/python-3.11+-blue)

## Problem Statement

Organizations with large document libraries (quality manuals, standards, procedures) spend significant time manually searching for policy answers. This agent provides instant, cited answers to natural-language questions — reducing lookup time and ensuring answers are traceable to source documents.

## Architecture

> Architecture diagram added Week 4 of Phase 1. See [ARCHITECTURE.md](ARCHITECTURE.md) for component breakdown.

## Agentic Pattern: RAG (Retrieval-Augmented Generation)

Rather than relying on an LLM's training data (which may be outdated or hallucinated), RAG agents retrieve relevant document chunks first, then generate answers grounded in those retrieved sources. Every answer includes citations showing exactly which document sections were used.

## Evaluation Targets

| Metric | Target | Method |
|--------|--------|--------|
| Retrieval Accuracy | ≥85% | 25 curated Q&A pairs |
| Citation Correctness | ≥90% | 50 spot-check citations |
| Response Time | <8s | Automated timing |

## Quick Start

> Active development begins Week 4 (Phase 1). Full demo available at Phase 1 completion.

```bash
git clone https://github.com/Jlowpez/knowledge-navigator
cd knowledge-navigator
pip install uv && uv pip install -e ".[dev]"
pytest tests/ -v
```

## Production Path

Replace the document corpus in `data/synthetic/` with your organization's documents. The ingestion pipeline and agent logic are unchanged — only the source files differ. The data access layer (`src/dal/`) abstracts all backend calls, enabling a data source swap via config change only.

## Part of a Larger System

→ [ops-orchestrator](https://github.com/Jlowpez/ops-orchestrator) — full platform view

| Agent | Pattern | Status |
|-------|---------|--------|
| **knowledge-navigator** | RAG Agent | 🔄 Active |
| [intake-agent](https://github.com/Jlowpez/intake-agent) | Structured Output | ⏳ Phase 2 |
| [compliance-checker](https://github.com/Jlowpez/compliance-checker) | Multi-Agent Pipeline | ⏳ Phase 3 |
| [workload-scheduler](https://github.com/Jlowpez/workload-scheduler) | Planner-Executor | ⏳ Phase 4 |
| [ops-orchestrator](https://github.com/Jlowpez/ops-orchestrator) | Orchestrator | ⏳ Phase 5 |

## See Also

- [ARCHITECTURE.md](ARCHITECTURE.md) — System design and data flow
- [TOOLS.md](TOOLS.md) — Tool selection rationale
