from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from ..database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    location = Column(String, index=True)
    
    # How does this work in ORM world?
    player_1_name = mapped_column(ForeignKey("players.name"))
    player_1 = relationship(back_populates="child")
    player_1_name = mapped_column(ForeignKey("players.name"))
    player_2 = Column(String, index=True)
    
    winner = Column(String, index=True)