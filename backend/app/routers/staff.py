from fastapi import APIRouter
from typing import List
from ..models.staff import Staff

router = APIRouter()

# static list for demo
@router.get("/", response_model=List[Staff])
def list_staff():
    data = [
        {"id": 1, "name": "Dr. Jane Dushime", "role": "Principal"},
        {"id": 2, "name": "Mr. John Doe", "role": "Head of Primary"},
        {"id": 3, "name": "Ms. Alice Mwiza", "role": "Cambridge Coordinator"}
    ]
    return data
