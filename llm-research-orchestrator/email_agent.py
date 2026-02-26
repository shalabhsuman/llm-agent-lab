import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool, ModelSettings

DEFAULT_RECIPIENT_EMAIL = ""
recipient_email = DEFAULT_RECIPIENT_EMAIL


def set_recipient_email(email: str) -> None:
    global recipient_email
    if email:
        recipient_email = email


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""
    sendgrid_api_key = os.environ.get("SENDGRID_API_KEY")
    from_address = os.environ.get("SENDGRID_FROM_EMAIL")
    if not sendgrid_api_key:
        raise RuntimeError("Missing SENDGRID_API_KEY in environment.")
    if not from_address:
        raise RuntimeError("Missing SENDGRID_FROM_EMAIL in environment.")
    if not recipient_email:
        raise RuntimeError("Recipient email is empty.")

    sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
    from_email = Email(from_address)
    to_email = To(recipient_email)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response", response.status_code)
    if response.status_code < 200 or response.status_code >= 300:
        body = response.body.decode("utf-8", errors="ignore") if response.body else ""
        raise RuntimeError(f"SendGrid send failed: status={response.status_code}, body={body}")

    return {
        "status": "success",
        "recipient": recipient_email,
        "status_code": str(response.status_code),
        "from_email": from_address,
    }


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)
