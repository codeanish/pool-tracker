from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    # disabled: bool | None = None

class UserCreate(UserBase):
    password: str

class UserEdit(UserBase):
    password: str | None = None

class User(UserBase):
    pass