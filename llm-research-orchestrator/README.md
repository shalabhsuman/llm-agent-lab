---
title: LLM Research Orchestrator
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---
# LLM Research Orchestrator (OpenAI SDK + Gradio)

This app takes a research prompt, plans web searches, synthesizes a long-form report, and emails the final write-up to a recipient you enter in the UI.

It is built as a small multi-agent workflow:
- Planner agent: decides what to search
- Search agent: runs web research
- Writer agent: compiles the final report
- Email agent: formats and sends the report via SendGrid

## Stack
- OpenAI Agents SDK (`openai-agents`)
- OpenAI models
- Gradio (UI)
- SendGrid (email delivery)
- `uv` (local environment + dependency management)

## Run Locally (uv)

From this folder:

```bash
uv sync
uv run python app.py
```

Then open the Gradio link shown in terminal.

### Local environment variables

Create a shared repository-level `.env` file at the project root (copy from `../.env.example`):

```env
OPENAI_API_KEY=your_openai_key
SENDGRID_API_KEY=your_sendgrid_key
SENDGRID_FROM_EMAIL=verified-sender@yourdomain.com
```

`SENDGRID_FROM_EMAIL` must be a verified sender in SendGrid.

## Deploy to Hugging Face Spaces

1. Go to Hugging Face and create a new **Gradio** Space.
2. From this folder, run:

```bash
uv run gradio deploy
```

3. When prompted:
- Space name/title: use your target Space
- Gradio app file: `app.py`

4. In Space settings, add Secrets:
- `OPENAI_API_KEY`
- `SENDGRID_API_KEY`
- `SENDGRID_FROM_EMAIL`

5. Rebuild/restart Space after secret or dependency changes.
For dependency changes (`requirements.txt`), use **Factory Reboot**.

## Example

Prompt:
`Compare top agent orchestration frameworks for production AI systems in 2026, with trade-offs and recommendations.`

Recipient:
`name@example.com`

The app will stream progress updates, generate a detailed markdown report, and send the formatted report by email.
