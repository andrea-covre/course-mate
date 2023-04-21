from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Schedule(Base):
    __tablename__ = "schedule"

    account_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    section_id: Mapped[int] = mapped_column(primary_key=True)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])