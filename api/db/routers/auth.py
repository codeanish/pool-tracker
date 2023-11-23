from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from db.auth import validate_auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter(
    prefix="/auth",
)

@router.get("/")
def validate_token():
    return JSONResponse(validate_auth.validate_token(""))