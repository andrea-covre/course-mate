from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(320))
    edu_email_address: Mapped[str] = mapped_column(String(320))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15))
    grad_year: Mapped[int]
    major_id: Mapped[int]

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])