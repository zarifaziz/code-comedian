from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class FastAPISettings(BaseModel):
    """FastAPI settings"""

    port: int = 8000
    prefix: str = "/joke-judge-ai"
    host: str = "0.0.0.0"
    api_dir: Path = Path(__file__).absolute().parent / "api"
    reload: bool = False


class Settings(BaseSettings):
    """
    This class is used to manage settings for the application.
    """

    OPENAI_API_KEY: str
    fastapi: FastAPISettings = FastAPISettings()

    class Config:
        """
        This class is used to manage environmnt configuration for the application
        """

        env_file = Path(__file__).parents[2] / ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


settings = Settings()
