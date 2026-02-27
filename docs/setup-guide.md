# Setup Guide

This guide captures setup and operational references for this project, including runtime, environment configuration, integrations, and deployment.

## Current Stack

- [OpenAI Agents SDK](https://platform.openai.com/docs/libraries)
- [CrewAI](https://www.crewai.com/)
- [Serper API](https://serper.dev/)
- [Gradio](https://www.gradio.app/)
- [Vercel](https://vercel.com/)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Pushover](https://pushover.net/)
- [SendGrid](https://sendgrid.com/)
- [uv](https://docs.astral.sh/uv/)
- [Node.js](https://nodejs.org/)

## Environment Configuration

- Use the repository environment template as the source of truth: [`.env.example`](../.env.example)
- Create your local environment file from the template:

```bash
cp .env.example .env
```

- Add your API keys and service tokens in `.env` for all integrations listed in the template (OpenAI, Serper, SendGrid, Pushover, and related services).

## uv Environment Setup

- From the repository root, sync the Python environment from [`pyproject.toml`](../pyproject.toml) and [`uv.lock`](../uv.lock):
- This creates a local virtual environment at `./.venv` in the project root (by default).
- If you have questions about `uv`, refer to the official docs: [uv Documentation](https://docs.astral.sh/uv/)

```bash
uv sync
```

## Gradio Deployment (Hugging Face Spaces)

- In the app directory (for example, `llm-research-orchestrator`), deploy with:

```bash
uv run gradio deploy
```

- Use the prompts to select your target Hugging Face Space and app file.

## Node.js Setup

- Install the latest active LTS release from [nodejs.org](https://nodejs.org/)
- Verify:

```bash
node -v
npm -v
```
