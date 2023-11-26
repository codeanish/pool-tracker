from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from db.auth.validate_auth import get_user_from_token
from db.auth.jwt_bearer import JWTBearer
from db.database import SessionLocal
from db.schemas.player import Player, PlayerCreate, PlayerEdit
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

# ***** /me needs to be before /{player_id} or else it will think "me" is a player_id

@router.get("/me", response_model=Player)
def get_current_player(creds: HTTPAuthorizationCredentials = Depends(JWTBearer()), db: Session = Depends(get_db)):
    user = get_user_from_token(creds.credentials)
    print(user)
    db_player = player_repository.get_player_by_username(db, username=user)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.get("/{username}", response_model=Player, dependencies=[Depends(JWTBearer())])
def get_player(username: str, db: Session = Depends(get_db)):
    db_player = player_repository.get_player_by_username(db, username=username)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.post("/", response_model=Player)
def create_player(new_player: PlayerCreate, db: Session = Depends(get_db)):
    return player_repository.new_player(db=db, new_player=new_player)

# TODO: Make sure that the player is the one who is updating their own profile
@router.put("/{username}", response_model=Player, dependencies=[Depends(JWTBearer())])
def update_player(username: str, player: PlayerEdit, db: Session = Depends(get_db)):
    db_player = player_repository.get_player_by_username(db, username=username)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player_repository.update_player(db=db, username=username, player=player)
