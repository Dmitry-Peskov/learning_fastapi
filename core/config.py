from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_dsn: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = True

settings = Settings()

