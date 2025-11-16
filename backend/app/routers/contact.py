from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel, EmailStr
from ..database import get_session
from ..models.message import Message
from ..services.email_service import send_contact_email

router = APIRouter()

class ContactIn(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

@router.post("/send")
def send_contact(contact: ContactIn, background_tasks: BackgroundTasks):
    # store in DB
    with get_session() as session:
        msg = Message(name=contact.name, email=contact.email, subject=contact.subject, body=contact.message)
        session.add(msg)
        session.commit()
        session.refresh(msg)

    # send email in background
    background_tasks.add_task(send_contact_email, contact.dict())
    return {"status": "ok", "id": msg.id}
