from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My app"
    debug: bool = False
    db_user: str = "admin"
    db_password: str = "admin"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "dbname"

    class Config:
        env_file = ".env"

settings = Settings()