from fastapi import FastAPI
from db.routers import players, games
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(players.router)
app.include_router(games.router)
