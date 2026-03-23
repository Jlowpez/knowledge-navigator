"""
knowledge-navigator — RAG Agent Tests

Phase 1 starting point. These tests are skipped until Phase 1 implementation
begins in Week 5. When Phase 1 starts:
1. Delete the pytest.skip() calls
2. Import the real RagAgent class
3. Implement the test bodies

This file exists now to:
- Signal that tests are planned (not forgotten)
- Keep CI green during scaffold phase
- Define the acceptance criteria before writing code (TDD intent)
"""
import pytest


def test_rag_agent_answers_question():
    """Agent must return a non-empty answer string."""
    pytest.skip("Phase 1 not started — skeleton test")


def test_rag_agent_cites_source_section():
    """Every answer must include at least one source citation."""
    pytest.skip("Phase 1 not started — skeleton test")


def test_rag_agent_response_under_8_seconds():
    """Response time must be under 8 seconds (eval target)."""
    pytest.skip("Phase 1 not started — skeleton test")


def test_retrieval_accuracy_on_eval_set():
    """Retrieval accuracy must be ≥85% on 25 curated Q&A pairs."""
    pytest.skip("Phase 1 not started — skeleton test")
