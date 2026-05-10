from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    project_name: str = "payments-data-lake-foundations"
    data_raw_path: Path = Path("data/raw")
    data_bronze_path: Path = Path("data/bronze")
    data_silver_path: Path = Path("data/silver")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )

settings = Settings()