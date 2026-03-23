# knowledge-navigator — Architecture

## System Overview

`knowledge-navigator` is a RAG (Retrieval-Augmented Generation) agent that answers natural-language questions against any document corpus, returning grounded answers with citations. It depends on `agent-core` for its vector store and data access layer.

## Architecture Diagram

> Diagram added Phase 1, Week 4. Source: `docs/architecture.excalidraw`. Exported: `docs/architecture.png`.

## Components

| Component | Responsibility | Key Files |
|-----------|---------------|----------|
| Ingestion Pipeline | Chunk documents, generate embeddings, store in ChromaDB | `src/tools/retrieval_tool.py` |
| RAG Agent | Query reformulation, retrieval, answer generation with citations | `src/agent/rag_agent.py` |
| Streamlit UI | Question input, source selector, citation display | `src/ui/app.py` |
| DAL | Data access via agent-core SQLiteDAL | `src/dal/__init__.py` |

## Data Flow

1. User submits a natural-language question via Streamlit UI
2. Agent reformulates query for better retrieval
3. Retrieval tool queries ChromaDB for top-k relevant document chunks
4. Agent sends question + retrieved chunks to LLM
5. LLM generates a grounded answer with section citations
6. UI displays answer with expandable source references

## Agentic Pattern: RAG

RAG is chosen here because:
- Document corpus changes frequently (new standards, updated procedures)
- Answers must be traceable to source documents for audit purposes
- Hallucination is unacceptable in a compliance context

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| ChromaDB via agent-core | Shared infrastructure, consistent across all RAG agents |
| Query reformulation step | Improves retrieval accuracy for ambiguous natural-language questions |
| Citations mandatory | Every answer references source sections — no ungrounded claims |

## Production Swap

Replace `data/synthetic/` document files with your organization's documents. Re-run the ingestion pipeline. All agent logic unchanged.

## Known Limitations

> Filled in at Phase 1 completion after evaluation.
