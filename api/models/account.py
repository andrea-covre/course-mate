from typing import List
from typing import Optional
from sqlalchemy import String, BigInteger, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Account(Base):
    __tablename__ = "account"

    id: Mapped[str] = mapped_column(String(128), unique=True, primary_key=True)
    email_address: Mapped[str] = mapped_column(String(320), unique=True)
    edu_email_address: Mapped[str] = mapped_column(String(320), unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[int] = mapped_column(BigInteger(), unique=True)
    grad_year: Mapped[int]
    major_id: Mapped[int]
    
    __table_args__ = (UniqueConstraint('email_address', name='uq_email_address'),)
    __table_args__ = (UniqueConstraint('edu_email_address', name='uq_edu_email_address'),)
    __table_args__ = (UniqueConstraint('phone_number', name='phone_number'),)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])