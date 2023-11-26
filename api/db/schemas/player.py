from datetime import datetime
from pydantic import BaseModel, EmailStr

class PlayerBase(BaseModel):
    username: str
    name: str
    email: EmailStr
    date_of_birth: datetime
    country: str
    location: str


class PlayerCreate(PlayerBase):
    pass

class PlayerEdit(PlayerBase):
    pass

class Player(PlayerBase):
    pass

    class Config:
        orm_mode = True