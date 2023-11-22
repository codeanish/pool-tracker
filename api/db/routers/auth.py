from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db.auth import validate_auth


router = APIRouter(
    prefix="/auth",
)

@router.get("/")
def get_jwks():
    return JSONResponse(validate_auth.get_public_jwks())