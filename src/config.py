from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loading environments from the .env file"""

    BOT_TOKEN: str

    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str

    @property
    def get_sqlalchemy_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"
        )

    class Config:
        env_file = ".env"


# environment variables
settings = Settings()
