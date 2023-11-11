from fastapi import FastAPI, Depends
from pikastro.app.routers import solar
from pikastro.app import config
from fastapi.openapi.utils import get_openapi
import os
from typing import Annotated, Union


app = FastAPI()

app.include_router(solar.router, prefix="/api/v1")


@app.get("/health")
async def health():
    return {"message": "OK"}


@app.get("/config")
def get_config():
    cfg = config.get_config_from_file(os.environ.get("ENVIRONMENT", "local"))
    return cfg


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Solar Panel API",
        version="2.5.0",
        openapi_version="3.0.0",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    cfg = config.get_config_from_file(os.environ.get("ENVIRONMENT", "local"))
    if cfg.x_google_backend:
        openapi_schema["x-google-backend"] = {}
        openapi_schema["x-google-backend"]["address"] = cfg.x_google_backend

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("pikastro.app.main:app", host="0.0.0.0", port=8080, reload=True)
