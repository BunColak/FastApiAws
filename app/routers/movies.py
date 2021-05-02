from typing import List
from fastapi import APIRouter, HTTPException

from app.models.movies import Movie
from app.db.dynamo import get_movies_table

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/", response_model=List[Movie])
def read_movies():
    return get_movies_table().scan()["Items"]


@router.get(
    "/{movie_id}",
    response_model=Movie,
    responses={404: {"description": "Movie not found"}},
)
def read_movie(movie_id: int):
    movie = get_movies_table().get_item(Key={"id": movie_id})
    if "Item" in movie:
        return movie["Item"]
    else:
        raise HTTPException(status_code=404)


@router.post("/", status_code=201, response_model=Movie)
def add_movie(movie: Movie):
    movie = Movie(**movie.dict())

    table = get_movies_table()
    table.put_item(Item={**movie.dict()})

    return movie


@router.put("/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    return movie


@router.delete("/{movie_id}", response_model=int)
def delete_movie(movie_id):
    return 1
