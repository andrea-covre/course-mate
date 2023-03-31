from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Semester(Base):
    __tablename__ = "semester"

    id: Mapped[int] = mapped_column(primary_key=True)
    term: Mapped[str] = mapped_column(String(6))
    year: Mapped[int]

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])