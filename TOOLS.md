# knowledge-navigator — Tools & Technology Decisions

> Full tool rationale documented at Phase 1 completion.
> Core dependencies listed below; detailed justifications added as each tool is evaluated during the build.

## Core Dependencies

| Tool | Purpose | Why Chosen |
|------|---------|------------|
| Anthropic SDK | LLM calls (Claude) | Native tool use, streaming, typed SDK |
| ChromaDB | Vector store for RAG | Via agent-core — see agent-core/TOOLS.md |
| Streamlit | Demo UI | Zero-boilerplate Python web UI, ideal for ML demos |
| python-dotenv | Environment config | Standard for managing API keys locally |

## Development Tools

Same as agent-core — uv, ruff, mypy, pytest. See [agent-core/TOOLS.md](https://github.com/Jlowpez/agent-core/blob/main/TOOLS.md).
