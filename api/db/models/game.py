from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column
from ..database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    location = Column(String, index=True)
    
    player_1_id = mapped_column(ForeignKey("players.id"))
    player_2_id = mapped_column(ForeignKey("players.id"))
    breaking_player_id = mapped_column(ForeignKey("players.id"), nullable=True)
    winner_id = mapped_column(ForeignKey("players.id"), nullable=True)
