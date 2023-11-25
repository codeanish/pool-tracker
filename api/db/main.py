from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.routers import players, games
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(players.router)
app.include_router(games.router)
