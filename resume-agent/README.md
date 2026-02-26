# Resume Agent

## Overview

Resume Agent is a lightweight conversational assistant that answers questions about a candidate profile using curated resume context.

## Architecture

This project follows a simple application structure centered around an entrypoint (`app.py`) and local context files in `data/`.

- `app.py`: Gradio chat app and LLM interaction loop
- `data/summary.txt`: high-level profile summary (safe, non-sensitive)
- `data/resume.txt` or `data/resume.pdf`: resume content used as context
- `../.env`: shared repository-level secrets/config (not committed)

## Tech Stack

- Python
- OpenAI API
- Gradio UI
- Supporting libraries listed in `requirements.txt`

## How to Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Copy `../.env.example` to `../.env` and set at least `OPENAI_API_KEY`.
4. Add safe, non-sensitive placeholder content in `data/summary.txt` and `data/resume.txt` (or provide `data/resume.pdf`).
5. Run the application:

```bash
python app.py
```

## Deployment

Deploy target: Hugging Face Spaces (Gradio).

1. Create/login to your Hugging Face account: [https://huggingface.co](https://huggingface.co)
2. Create a token with `WRITE` permission (Avatar -> Access Tokens).
3. Install CLI tooling:

```bash
uv tool install "huggingface_hub[cli]"
```

4. Authenticate:

```bash
hf auth login --token hf_xxx
hf auth whoami
```

5. Save token locally in `../.env`:

```env
HF_TOKEN=hf_xxx
```

6. From `resume-agent/`, run deployment:

```bash
uv run gradio deploy
```

7. When prompted:
- Space name: choose your own (for example `resume-agent`)
- App file: `app.py`
- Hardware: `cpu-basic`
- Secrets: `Yes`
- Add at least `OPENAI_API_KEY`
- GitHub Actions: `No` (unless you explicitly want CI deploys)

### Secrets In Spaces

In Hugging Face Space settings, add keys in Variables and Secrets.
For this current app, only `OPENAI_API_KEY` is required.
Other keys in `.env.example` are optional for future integrations.

### Redeploy Notes

- If deployment prompts behave unexpectedly, remove any auto-generated local README in the deploy folder and rerun `uv run gradio deploy`.
- You can always edit Space secrets later in Space Settings -> Variables and Secrets.
