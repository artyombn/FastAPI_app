import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    DOCKER: bool
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST_LOCAL: str
    DB_HOST_DOCKER: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"),
        extra="allow"
    )

    def get_db_url(self):
        if self.DOCKER:
            return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                    f"{self.DB_HOST_DOCKER}:{self.DB_PORT}/{self.DB_NAME}")
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST_LOCAL}:{self.DB_PORT}/{self.DB_NAME}")

settings = Settings()