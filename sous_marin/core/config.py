from typing import Union, List
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    API_V1_STRING = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Sous-marin service"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    SECRET_KEY = "big secret"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
