from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import player_repository, game_repository
# from . import game_repository
from .schemas import player, game
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/players/", response_model=list[player.Player])
def get_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = player_repository.get_all_players(db, skip=skip, limit=limit)
    return players

@app.get("/players/{player_id}", response_model=player.Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    db_player = player_repository.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.post("/players/", response_model=player.Player)
def create_player(new_player: player.PlayerCreate, db: Session = Depends(get_db)):
    return player_repository.new_player(db=db, new_player=new_player)


@app.get("/games/{game_id}", response_model=game.Game)
def get_game(game_id: int, db: Session = Depends(get_db)):
    db_game = game_repository.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game

@app.post("/games/", response_model=game.Game)
def create_game(new_game: game.GameCreate, db: Session = Depends(get_db)):
    return game_repository.new_game(db=db, new_game=new_game)
