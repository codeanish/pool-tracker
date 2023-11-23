import os

class Config:
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    PUBLIC_KEYS_URL = os.environ.get('PUBLIC_KEYS_URL') or "http://localhost:8000/.well-known/jwks.json"
    