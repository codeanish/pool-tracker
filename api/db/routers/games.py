from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.schemas.game import Game, GameCreate
from db.repositories import game_repository


router = APIRouter(
    prefix="/games",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{game_id}", response_model=Game)
def get_game(game_id: int, db: Session = Depends(get_db)):
    db_game = game_repository.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game

@router.post("/", response_model=Game)
def create_game(new_game: GameCreate, db: Session = Depends(get_db)):
    return game_repository.new_game(db=db, new_game=new_game)

@router.post("/{game_id}/winner", response_model=Game)
def declare_winner(game_id: int, winner_id: int, db: Session = Depends(get_db)):
    db_game = game_repository.get_game(db, game_id=game_id)
    if db_game is None:
        raise Exception("Game not found")
    return game_repository.declare_winner(db, game_id, winner_id)
