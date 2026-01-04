# AI Services Training

A compact collection of guiding questions and exercises covering core AI concepts, inference techniques, and the operational tooling needed to package and run models in production. Materials are designed for short training sessions and self‑study.

Primary focus
- AI Foundation (primary)
  - Purpose: a practical, concept-first roadmap that builds from "What is AI?" through classic ML, deep learning, language modelling, LLM architechtures and into applied LLM systems (RAG, tool-calling, agents, MCP). See 04-AI Foundation/ai_foundations_roadmap.md for the full lesson plan, guided questions and exercises.
  - Structure: short conceptual sections + hands‑on labs. Key topics include:
    - What is AI and core paradigms (planning vs inductive AI)
    - Classic ML fundamentals: datasets, evaluation, regression/classification, overfitting
    - Deep learning basics: neurons, training loop, backprop, pretraining vs fine-tuning and practical lab.
    - Text modality: tokenization, embeddings
    - Transformers internals: Basic arcitechture, masked vs autoregressive models and practical labs.
    - Applied LLM systems: Retrieval‑Augmented Generation (RAG), tool/function calling, agentic workflows, and Model Context Protocol (MCP)
  - Outcome: develop conceptual fluency via guided questions, and complete small labs that connect theory to simple implementations.

- AI Inference (primary)
  - Purpose: how to serve, optimize and scale models for low‑latency, production inference.
  - Content: tradeoffs of inference runtimes and architectures, memory/KV‑cache and paged‑attention techniques, and practical deployment guidance. See 05-AI Inference/* for exercises and notes.
  - Outcome: evaluate inference engines, apply memory and latency optimizations, and prepare models for production deployment.

Supporting topics
- 01-Python — concise Python reference and exercises used across labs.
- 02-Docker — container patterns for packaging models and services.
- 03-Helm-Argo — Helm chart basics and GitOps (Argo) deployment workflows.
- 06-MLOps — basic concepts and tools
- 07-GPU — GPU very fundamentals.
- 08-Monitoring — observability for models and services in general using Prometheus and Grafana.

