from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Subject(Base):
   __tablename__ = "subject"

   code: Mapped[str] = mapped_column(String(4), primary_key=True)
   name: Mapped[str] = mapped_column(String(64))

   def as_dict(self):
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  
   def __init__(self, dict):
       for key in dict:
           setattr(self, key, dict[key])