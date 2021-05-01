from magnum import Magnum
from fastapi import FastAPI

from app.routers import movies

app = FastAPI()

app.include_router(movies.router)

handler = Magnum(app)
