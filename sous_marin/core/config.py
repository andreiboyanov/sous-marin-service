from typing import Union, List
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    api_v1_path = "/api/v1"
    cors_origins: List[AnyHttpUrl] = []
    project_name: str = "Sous-marin service"
    access_token_ttl_minutes = 60
    secret_key = "big secret"
    db_url = "mongodb://sous-marin:sous-marin-password@:localhost:27017"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
