
from fastapi import APIRouter, Depends
from auth.database import SessionLocal
from auth.repositories import user_repository
from auth.schemas.user import User, UserCreate
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=User)
async def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    return user_repository.new_user(db=db, new_user=new_user)