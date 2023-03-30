from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
   pass

class Section(Base):
    __tablename__ = "section"

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment = True)
    semester_id: Mapped[int]
    class_id: Mapped[int]
    crn: Mapped[int]
    section_name: Mapped[str] = mapped_column(String)
    instructors: Mapped[str] 
    times: Mapped[str] = mapped_column(String)
    location_id: Mapped[int]
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])