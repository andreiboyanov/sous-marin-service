from typing import List
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    api_v1_path = "/api/v1"
    cors_origins: List[AnyHttpUrl] = []
    project_name: str = "Sous-marin service"
    access_token_ttl_minutes = 60
    secret_key = "big secret"
    db_url = "mongodb://sous-marin:sous-marin-password@:localhost:27017"


settings = Settings()