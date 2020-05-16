import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from sous_marin import __version__
from sous_marin.api.api_v1.api import api_router
from sous_marin.core.config import settings

print("Starting sous-marin-service")


app = FastAPI(
    title=settings.project_name,
    version=__version__,
    openapi_url=f"{settings.api_v1_path}/openapi.json",
)

if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.api_v1_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
