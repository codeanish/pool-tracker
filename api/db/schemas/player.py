from pydantic import BaseModel, EmailStr

class PlayerBase(BaseModel):
    name: str
    email: EmailStr


class PlayerCreate(PlayerBase):
    pass

class PlayerEdit(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True