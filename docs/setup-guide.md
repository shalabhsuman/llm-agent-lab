# Setup Guide

This guide captures setup and operational references for this project, including runtime, environment configuration, integrations, and deployment.

## Current Stack

- Node.js
- OpenAI Agents SDK
- CrewAI
- Serper API
- Vercel
- Pushover
- SendGrid
- uv

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
- If you have questions about `uv`, refer to the official docs: https://docs.astral.sh/uv/

```bash
uv sync
```

## Node.js Setup

- Install the latest active LTS release from https://nodejs.org/
- Verify:

```bash
node -v
npm -v
```
