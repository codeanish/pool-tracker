from sqlalchemy.orm import Session

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

