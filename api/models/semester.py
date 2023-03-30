import enum

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Enum

class Base(DeclarativeBase):
   pass

class Term(enum.Enum):
    fall = "Fall"
    spring = "Spring"
    summer = "Summer"

class Semester(Base):
    __tablename__ = "semester"

    id: Mapped[int] = mapped_column(primary_key=True)
    term: Mapped[Enum(Term)]
    semester_year: Mapped[int]

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])