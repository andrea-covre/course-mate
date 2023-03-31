from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base

class Major(Base):
   __tablename__ = "major"

   id: Mapped[int] = mapped_column(primary_key=True)
   level: Mapped[str] = mapped_column(String(3))
   name: Mapped[str] = mapped_column(String(64))


   def as_dict(self):
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  
   def __init__(self, dict):
       for key in dict:
           setattr(self, key, dict[key])