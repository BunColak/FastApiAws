from typing import List
from fastapi import APIRouter, HTTPException

from app.models import Movie

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/", response_model=List[Movie])
def read_movies():
    m1 = Movie(id=1, name="Test", rating=1.5)
    m2 = Movie(id=2, name="Test 2", rating=4.5)

    return [m1, m2]


@router.get(
    "/{movie_id}",
    response_model=Movie,
    responses={404: {"description": "Movie not found"}},
)
def read_movie(movie_id: int):
    if movie_id > 5:
        raise HTTPException(
            status_code=404,
        )
    m1 = Movie(id=movie_id, name="Test", rating=1.5)

    return m1
