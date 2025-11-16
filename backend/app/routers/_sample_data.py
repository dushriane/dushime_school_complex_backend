# helper to seed sample data (optional)
from ..database import get_session
from ..models.program import Program
from ..models.announcement import Announcement


def seed():
    with get_session() as session:
        if not session.exec(select(Program)).first():
            session.add(Program(title="Cambridge Primary", description="International curriculum for primary students", level="Primary", duration="6 years"))
            session.add(Program(title="Cambridge Secondary", description="Secondary education preparing for IGCSE", level="Secondary", duration="5 years"))
            session.commit()
