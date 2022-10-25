from pydantic import BaseSettings


class Settings(BaseSettings):
    BACKEND_PORT: int
    POSTGRES_HOST: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    JWT_SECRET: str
    JWT_ALGO: str = "HS256"


settings = Settings()
