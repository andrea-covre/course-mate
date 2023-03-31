import enum

from typing import List
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Status(enum.Enum):
    pending = "Pending"
    accepted = "Accepted"

class Friendship(Base):
    __tablename__ = "friendship"

    account_id_1: Mapped[int] = mapped_column(primary_key=True)
    account_id_2: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[Status]

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])