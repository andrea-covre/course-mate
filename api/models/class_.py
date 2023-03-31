from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from api.models.base import Base

class Class(Base):
    __tablename__ = "class"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_code: Mapped[str] = mapped_column(String(4))
    class_code: Mapped[str] = mapped_column(String(5))
    title: Mapped[str] = mapped_column(String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])