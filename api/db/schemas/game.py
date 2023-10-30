import datetime
from typing import Optional
from pydantic import BaseModel

class GameBase(BaseModel):
    location: str


class GameCreate(GameBase):
    date: datetime.datetime
    player_1_id: int
    player_2_id: int


class Game(GameBase):
    id: int
    player_1_id: int
    player_2_id: int
    date: datetime.datetime
    breaking_player_id: Optional[int]
    winner_id: Optional[int]

    class Config:
        orm_mode = True