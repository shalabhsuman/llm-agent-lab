from pathlib import Path
import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
ROOT_ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(dotenv_path=ROOT_ENV_PATH, override=True)


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def _read_pdf_text(path: Path) -> str:
    if not path.exists():
        return ""
    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        if text.strip():
            pages.append(text)
    return "\n".join(pages).strip()


class ResumeAgent:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.agent_name = os.getenv("AGENT_NAME", "Resume Assistant")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

        self.summary = _read_text(DATA_DIR / "summary.txt")
        self.resume_text = _read_text(DATA_DIR / "resume.txt")

        # Optional PDF support: if data/resume.pdf exists, it supplements/overrides text resume context.
        resume_pdf_text = _read_pdf_text(DATA_DIR / "resume.pdf")
        if resume_pdf_text:
            self.resume_text = resume_pdf_text

    def system_prompt(self) -> str:
        summary = self.summary or "No summary provided yet."
        resume = self.resume_text or "No resume content provided yet."
        return (
            f"You are {self.agent_name}. "
            "Answer questions using ONLY the provided summary and resume context. "
            "If information is missing, say you do not have that detail and ask the user to update summary.txt or resume.txt. "
            "Do not invent facts. Keep responses concise and professional.\n\n"
            f"## Summary\n{summary}\n\n"
            f"## Resume\n{resume}"
        )

    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_prompt()}]
        messages.extend(history)
        messages.append({"role": "user", "content": message})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    agent = ResumeAgent()
    gr.ChatInterface(agent.chat, type="messages").launch()
