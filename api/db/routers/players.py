from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.schemas.player import Player, PlayerCreate
from db.repositories import player_repository

router = APIRouter(
    prefix="/players",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Player])
def get_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = player_repository.get_all_players(db, skip=skip, limit=limit)
    return players

@router.get("/{player_id}", response_model=Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    db_player = player_repository.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.post("/", response_model=Player)
def create_player(new_player: PlayerCreate, db: Session = Depends(get_db)):
    return player_repository.new_player(db=db, new_player=new_player)