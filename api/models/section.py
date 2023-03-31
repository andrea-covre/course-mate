from typing import Optional
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.location import Location

from api.models.base import Base

class Section(Base):
    __tablename__ = "section"

    section_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    semester_id: Mapped[int]
    class_id: Mapped[int]
    crn: Mapped[int]
    location_id: Mapped[int]
    section_code: Mapped[str] = mapped_column(String(3))
    days: Mapped[str] = mapped_column(String(10), nullable=True)
    times: Mapped[str] = mapped_column(String(20), nullable=True)
    credits: Mapped[int]
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    levels: Mapped[str] = mapped_column(String(50))
    grade_basis: Mapped[str] = mapped_column(String(5))
    attributes: Mapped[str] = mapped_column(String(200), nullable=True)
    campus: Mapped[str] = mapped_column(String(40))
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])