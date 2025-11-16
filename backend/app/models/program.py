from sqlmodel import SQLModel, Field
from typing import Optional

class Program(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    level: Optional[str] = None
    duration: Optional[str] = None
