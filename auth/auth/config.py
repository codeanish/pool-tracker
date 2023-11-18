from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    POSTGRES_HOST = os.environ.get('AUTH_DB_HOST')
    POSTGRES_USER = os.environ.get('AUTH_DB_USER')
    POSTGRES_PASSWORD = os.environ.get('AUTH_DB_PASSWORD')
    POSTGRES_DB = os.environ.get('AUTH_DB')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    SECRET_KEY = os.environ.get('SECRET_KEY', default="AAA")
    ACCESS_TOKEN_EXPIRE_MINUTES = float(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', default=30))
    ALGORITHM = os.environ.get('ALGORITHM', default="HS256")