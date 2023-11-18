from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routers import token, users
from auth.database import engine, Base

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
app.include_router(users.router)
app.include_router(token.router)