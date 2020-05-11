import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from sous_marin import __version__
from sous_marin.api.api_v1.api import api_router
from sous_marin.core.config import settings

print("Starting sous-marin-service")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=__version__,
    openapi_url=f"{settings.API_V1_STRING}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STRING)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)