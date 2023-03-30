from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
   pass

class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment = True)
    building: Mapped[str] = mapped_column(String(80))
    room: Mapped[str] = mapped_column(String(50))
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])