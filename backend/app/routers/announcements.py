from fastapi import APIRouter
from typing import List
from sqlmodel import select
from ..database import get_session
from ..models.announcement import Announcement

router = APIRouter()

@router.get("/", response_model=List[Announcement])
def list_announcements():
    with get_session() as session:
        anns = session.exec(select(Announcement)).all()
        return anns
