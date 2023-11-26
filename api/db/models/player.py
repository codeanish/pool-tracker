from sqlalchemy import Column, DateTime, String
from db.database import Base

class Player(Base):
    __tablename__ = "players"

    username = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    country = Column(String, nullable=True)
    location = Column(String, nullable=True)
    