from datetime import timedelta
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from auth.config import Config
from auth.schemas.token import TokenClaims

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(claims: TokenClaims):
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    if access_token_expires:
        expire = datetime.utcnow() + access_token_expires
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    claims.exp = expire
    encoded_jwt = jwt.encode(claims.dict(), get_private_key(), algorithm=Config.ALGORITHM) # type: ignore
    return encoded_jwt

def get_private_key():
    with open(Config.PRIVATE_KEY_FILE) as pem_file:
        private_key = pem_file.read()
    return private_key

def get_public_key():
    with open(Config.PUBLIC_KEY_FILE) as pem_file:
        public_key = pem_file.read()
    return public_key
