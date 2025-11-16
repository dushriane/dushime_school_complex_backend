from fastapi import APIRouter

router = APIRouter()

@router.get("/info")
def school_info():
    return {
        "name": "Dushime School Complex",
        "mission": "Provide world-class Cambridge education in Kigali, Rwanda.",
        "vision": "Nurturing global citizens with strong character and academic excellence."}

@router.get("/stats")
def school_stats():
    return {"students": 650, "teachers": 45, "classes": 24}
