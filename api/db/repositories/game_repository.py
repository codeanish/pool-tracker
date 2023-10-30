from sqlalchemy.orm import Session
from db.models import game
from db.schemas import game as game_schema

def get_game(db: Session, game_id: int):
    return db.query(game.Game).filter(game.Game.id == game_id).first()

def new_game(db: Session, new_game: game_schema.GameCreate):
    db_game = game.Game(
        location=new_game.location, 
        date=new_game.date, 
        player_1_id=new_game.player_1_id, 
        player_2_id=new_game.player_2_id,
        breaking_player_id=new_game.breaking_player_id
        )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def declare_winner(db: Session, game_id: int, winner_id: int):
    db_game = db.query(game.Game).filter(game.Game.id == game_id).first()
    if db_game is None:
        raise Exception("Game not found")
    db_game.winner_id = winner_id
    db.commit()
    db.refresh(db_game)
    return db_game