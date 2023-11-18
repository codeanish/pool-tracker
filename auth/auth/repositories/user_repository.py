from sqlalchemy.orm import Session
from auth.exceptions.database_exceptions import UserNotFoundError
from auth.helpers.auth import get_password_hash
from auth.models.user import User

from auth.schemas.user import UserCreate

def new_user(db: Session, new_user: UserCreate) -> User:
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

def get_hashed_password_for_user(db: Session, username: str) -> str:
    user = db.query(User.hashed_password).filter(User.username == username).one_or_none()
    if user:
        return user.hashed_password
    raise UserNotFoundError(username)
