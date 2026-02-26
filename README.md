# LLM Agent Systems Portfolio

A collection of production-style LLM agent systems focused on conversational interfaces, tool integration, and deployment patterns.

---

## LLM Research Orchestrator

Multi-agent research system that plans web research, synthesizes long-form reports, and delivers final outputs via email.

**Highlights**
- Multi-agent workflow (planner, search, writer, email)
- Research orchestration with OpenAI Agents SDK
- Gradio interface with streamed progress updates
- SendGrid integration for report delivery
- Hugging Face Spaces deployment support

**Live Deployment**  
https://huggingface.co/spaces/snsh0327/LLM-Research-Orchestrator

**Implementation**  
[llm-research-orchestrator/README.md](./llm-research-orchestrator/README.md)

---

## Resume Conversation Agent

Conversational agent representing a structured candidate profile, designed for interactive career discussions and lead capture.

**Highlights**
- Persona-consistent conversational interface
- Structured tool invocation for user detail capture and logging
- Resume ingestion via PDF parsing
- Environment-based configuration and secret management
- Deployed with Gradio on Hugging Face Spaces

**Live Deployment**  
https://huggingface.co/spaces/snsh0327/Data-Science-Career-Talk

**Implementation**  
[`resume-agent/`](./resume-agent/)
