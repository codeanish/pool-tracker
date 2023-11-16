from sqlalchemy.orm import Session
from auth.models.user import User

from auth.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def new_user(db: Session, new_user: UserCreate):
    db_user = User(
        username=new_user.username,
        email=new_user.email,
        full_name=new_user.full_name,
        hashed_password=get_password_hash(new_user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user