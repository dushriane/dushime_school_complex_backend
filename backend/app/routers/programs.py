from fastapi import APIRouter, HTTPException
from typing import List
from sqlmodel import select
from ..database import get_session
from ..models.program import Program

router = APIRouter()

@router.get("/", response_model=List[Program])
def list_programs():
    with get_session() as session:
        programs = session.exec(select(Program)).all()
        return programs

@router.get("/{program_id}", response_model=Program)
def get_program(program_id: int):
    with get_session() as session:
        program = session.get(Program, program_id)
        if not program:
            raise HTTPException(status_code=404, detail="Program not found")
        return program
