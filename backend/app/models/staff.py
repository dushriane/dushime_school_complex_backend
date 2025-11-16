from sqlmodel import SQLModel, Field
from typing import Optional

class Staff(SQLModel):
    id: Optional[int] = None
    name: str
    role: str
