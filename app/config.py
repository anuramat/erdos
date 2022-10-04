from pydantic import BaseSettings


class Settings(BaseSettings):
    BACKEND_PORT: int | None
    POSTGRES_HOST: str | None
    POSTGRES_PASSWORD: str | None
    POSTGRES_USER: str | None
    POSTGRES_DB: str | None


settings = Settings()
