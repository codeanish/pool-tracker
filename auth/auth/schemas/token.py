from datetime import datetime
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenClaims(BaseModel):
    sub: str
    exp: datetime | None = None