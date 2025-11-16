from fastapi import APIRouter

router = APIRouter()

@router.get("/requirements")
def admissions_requirements():
    # static mock data
    return {"requirements": [
        "Completed application form",
        "Birth certificate",
        "Previous school reports (if applicable)",
        "Immunization records"
    ]}

@router.get("/fees")
def admissions_fees():
    return {"fees": {
        "Nursery": "2000 RWF/month",
        "Primary": "3000 RWF/month",
        "Secondary": "4000 RWF/month"
    }}
