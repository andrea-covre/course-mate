from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
   pass

class Schedule(Base):
    __tablename__ = "schedule"

    account_id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(primary_key=True)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])