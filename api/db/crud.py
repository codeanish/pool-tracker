from sqlalchemy.orm import Session

# from . import models, schemas
from .models import player
from .schemas import player as player_schema

def get_player(db: Session, player_id: int):
    return db.query(player.Player).filter(player.Player.id == player_id).first()


def get_all_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(player.Player).offset(skip).limit(limit).all()

def new_player(db: Session, new_player: player_schema.PlayerCreate):
    db_player = player.Player(name=new_player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.model_dump(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
