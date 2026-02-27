# LLM Agent Systems Portfolio

A collection of production-style LLM agent systems focused on conversational interfaces, tool integration, and deployment patterns.

---

## Technology Stack

### AI and Agent Frameworks
- **[OpenAI Agents SDK](https://platform.openai.com/docs/libraries)** - LLM integration and API access
- **[CrewAI](https://www.crewai.com/)** - Multi-agent orchestration
- **[Serper API](https://serper.dev/)** - Fast Google SERP API for web research retrieval
- **[Gradio](https://www.gradio.app/)** - Interactive web UI for agent-based applications

### Deployment and Operations
- **[Vercel](https://vercel.com/)** - Hosting and production deployment
- **[Hugging Face Spaces](https://huggingface.co/spaces)** - Hosted app deployment for interactive demos
- **[Pushover](https://pushover.net/)** - Notification delivery
- **[SendGrid](https://sendgrid.com/)** - Transactional email delivery

### Core Runtime
- **[Node.js](https://nodejs.org/)** - JavaScript runtime for development and backend workflows
- **[uv](https://docs.astral.sh/uv/)** - Python package and project manager

**Setup and configuration guide:** [docs/setup-guide.md](./docs/setup-guide.md)

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
