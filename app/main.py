from mangum import Mangum
from fastapi import FastAPI

from app.routers import movies

app = FastAPI()

app.include_router(movies.router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}


handler = Mangum(app)
