from fastapi import FastAPI
from pikastro.app.routers import solar

app = FastAPI()

app.include_router(solar.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Pikastro is a Python-based API for solar panel data."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("pikastro.app.main:app", host="0.0.0.0", port=8080, reload=True)
