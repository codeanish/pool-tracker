from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    # SECRET_KEY = os.environ.get('SECRET_KEY', default="AAA")
    ACCESS_TOKEN_EXPIRE_MINUTES = float(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', default=30))
    ALGORITHM = os.environ.get('ALGORITHM', default="HS256")
    PRIVATE_KEY_FILE = os.environ.get('PRIVATE_KEY_FILE', default="./auth/certs/privateKey.pem")
    PUBLIC_KEY_FILE = os.environ.get('PUBLIC_KEY_FILE', default="./auth/certs/publicKey.pem")