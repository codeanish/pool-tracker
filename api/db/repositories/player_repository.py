from sqlalchemy.orm import Session

from db.models.player import Player
from db.schemas import player as player_schema

# def get_player(db: Session, player_id: int):
#     return db.query(Player).filter(Player.id == player_id).first()

def get_player_by_username(db: Session, username: str):
    return db.query(Player).filter(Player.username == username).first()

def get_all_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Player).offset(skip).limit(limit).all()

def new_player(db: Session, new_player: player_schema.PlayerCreate):
    db_player = Player(
        username=new_player.username, 
        name=new_player.name, 
        email=new_player.email,
        date_od_birth=new_player.date_of_birth,
        country=new_player.country,
        location=new_player.location)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(db: Session, username: str, player: player_schema.PlayerEdit):
    db_player = get_player_by_username(db=db, username=username)
    if db_player is None:
        return None
    db_player.update(player)
    db.commit()
    db.refresh(db_player)
    return db_player

