import os


from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(verbose=True)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Finance-manager-track"

    class Config:
        env_file = ".env"

    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')

    ORMAR_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"


settings = Settings()
