from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Section_Instructor(Base):
    __tablename__ = "section_instructor"

    section_id: Mapped[int] = mapped_column(primary_key=True)
    instructor_id: Mapped[int] = mapped_column(primary_key=True)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])