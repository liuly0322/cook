from sqlalchemy import Column, Integer, String

from .database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    create_time = Column(String)
    description = Column(String)
