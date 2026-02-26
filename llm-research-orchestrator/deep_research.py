import gradio as gr
from pathlib import Path
from dotenv import load_dotenv
from research_manager import ResearchManager

BASE_DIR = Path(__file__).parent
ROOT_ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(dotenv_path=ROOT_ENV_PATH, override=True)


async def run(query: str, recipient_email: str):
    if not recipient_email or "@" not in recipient_email:
        yield "Please provide a valid recipient email."
        return
    try:
        async for chunk in ResearchManager().run(query, recipient_email.strip()):
            yield chunk
    except Exception as exc:
        yield f"Email step failed: {exc}"


theme = gr.themes.Soft(
    primary_hue="sky",
    neutral_hue="slate",
    radius_size="lg",
).set(
    block_title_text_weight="700",
    block_label_text_weight="600",
    button_primary_background_fill="*primary_500",
    button_primary_background_fill_hover="*primary_600",
)

with gr.Blocks(theme=theme, title="LLM Research Orchestrator") as ui:
    gr.Markdown(
        """
# LLM Research Orchestrator
Generate a detailed research report and email it automatically.
        """
    )
    with gr.Group():
        query_textbox = gr.Textbox(
            label="What topic would you like to research?",
            lines=4,
            placeholder="Example: Compare top ML evaluation frameworks in 2026",
        )
        recipient_email = gr.Textbox(
            label="Recipient email",
            placeholder="name@example.com",
        )
        run_button = gr.Button("Run Research", variant="primary")
    report = gr.Markdown(label="Progress and report")

    run_button.click(fn=run, inputs=[query_textbox, recipient_email], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, recipient_email], outputs=report)
    recipient_email.submit(fn=run, inputs=[query_textbox, recipient_email], outputs=report)

if __name__ == "__main__":
    ui.launch(inbrowser=True)
