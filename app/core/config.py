# app/core/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    DEFAULT_PORT: int = 5050

    class Config:
        env_file = ".env"

settings = Settings()
