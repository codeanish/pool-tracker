from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from auth.database import SessionLocal
from auth.helpers.auth import  create_access_token, verify_password
from auth.schemas.token import Token, TokenClaims
from auth.repositories import user_repository
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
):
    user_authenticated = authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if(user_authenticated == False):
        raise HTTPException(
            status_code=401, 
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
            )
    access_token = create_access_token(
        claims=TokenClaims(sub=form_data.username)
    )
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_user(db: Session, username: str, password: str) -> bool:
    hashed_password = user_repository.get_hashed_password_for_user(db=db, username=username)
    return verify_password(password, hashed_password)




