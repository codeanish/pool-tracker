# from fastapi import HTTPException
# import jwt
from db.config import Config
import requests

# Needs to return a JWKS type
def get_public_jwks():
    response = requests.get(f"{Config.PUBLIC_KEYS_URL}/.well-known/jwks.json")
    return response.json()

# def validate_token(token: str):
    # credentials_exception = HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Could not validate credentials",
    #     headers={"WWW-Authenticate": "Bearer"},
    # )
    # jwks = get_public_jwks()
    # # jwt.decode(token, jwks.public_key, algorithms=jwks.algorithms)
    # response = requests.get('auth/.well-known/jwks.json')
    # jwt.PyJWKSet()
    # payload = jwt.decode(token, jwks.public_key, algorithms=jwks.algorithms)
    # username = payload.get("sub")
    # if username is None:
    #     raise credentials_exception
    # token_data = TokenData(username=username)
