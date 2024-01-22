from pydantic_settings import BaseSettings
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class DbSettings(BaseModel):
    HOST: str = os.getenv('DB_HOST', 'localhost')
    USER: str = os.getenv('DB_USER', 'root')
    PASSWORD: str = os.getenv('DB_PASSWORD', 'password')
    NAME: str = os.getenv('DB_NAME', 'db')
    PORT: str = os.getenv('DB_PORT', '5432')

    url: str = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
    echo: bool = False


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()

    hls_segment_time: int = 1
    hls_output_dir: str = "hls"


settings = Settings()
