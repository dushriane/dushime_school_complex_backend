from fastapi import FastAPI
from .database import init_db
from .routers import programs, announcements, admissions, contact, staff, school

app = FastAPI(title="Dushime School Complex API")

@app.on_event("startup")
def on_startup():
    # create sqlite DB + tables if needed
    init_db()

# include routers
app.include_router(programs.router, prefix="/programs", tags=["programs"])
app.include_router(announcements.router, prefix="/announcements", tags=["announcements"])
app.include_router(admissions.router, prefix="/admissions", tags=["admissions"])
app.include_router(contact.router, prefix="/contact", tags=["contact"])
app.include_router(staff.router, prefix="/staff", tags=["staff"])
app.include_router(school.router, prefix="/school", tags=["school"])
