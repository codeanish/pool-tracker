import datetime
from typing import Optional
from pydantic import BaseModel

class GameBase(BaseModel):
    location: str
    date: datetime.datetime
    player_1_id: int
    player_2_id: int


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    breaking_player_id: Optional[int]
    winner_id: Optional[int]

    class Config:
        orm_mode = True