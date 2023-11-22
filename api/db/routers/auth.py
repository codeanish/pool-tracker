from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db.auth import validate_auth


router = APIRouter(
    prefix="/games",
)

@router.get("/", response_model=JSONResponse)
def get_jwks():
    return validate_auth.get_public_jwks()