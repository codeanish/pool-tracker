from sqlalchemy.orm import Session

from db.models import player
from db.schemas import player as player_schema

def get_player(db: Session, player_id: int):
    return db.query(player.Player).filter(player.Player.id == player_id).first()

def get_player_by_username(db: Session, username: str):
    return db.query(player.Player).filter(player.Player.name == username).first()

def get_all_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(player.Player).offset(skip).limit(limit).all()

def new_player(db: Session, new_player: player_schema.PlayerCreate):
    db_player = player.Player(name=new_player.name, email=new_player.email)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(db: Session, player_id: int, player: player_schema.PlayerEdit):
    db_player = get_player(db=db, player_id=player_id)
    
    if db_player is None:
        return None
    db_player.update(player)
    # db_player.name = player.name
    # db_player.email = player.email
    db.commit()
    db.refresh(db_player)
    return db_player

