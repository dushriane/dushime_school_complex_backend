import smtplib
from email.message import EmailMessage
from ..config import settings


def send_contact_email(payload: dict):
    """Sends a simple email using smtplib. Runs in background."""
    try:
        msg = EmailMessage()
        msg["Subject"] = f"Contact form: {payload.get('subject')}"
        msg["From"] = settings.FROM_EMAIL
        msg["To"] = settings.ADMIN_EMAIL
        body = f"Name: {payload.get('name')}\nEmail: {payload.get('email')}\n\nMessage:\n{payload.get('message')}"
        msg.set_content(body)

        if settings.SMTP_HOST in (None, "localhost"):
            # attempt local send (may fail on some environments) — fallback: print
            try:
                with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as s:
                    if settings.SMTP_USER and settings.SMTP_PASS:
                        s.login(settings.SMTP_USER, settings.SMTP_PASS)
                    s.send_message(msg)
                return True
            except Exception:
                print("Could not send via SMTP; printing message instead:\n", body)
                return False
        else:
            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as s:
                if settings.SMTP_USER and settings.SMTP_PASS:
                    s.login(settings.SMTP_USER, settings.SMTP_PASS)
                s.send_message(msg)
            return True
    except Exception as e:
        print("email send error:", e)
        return False
