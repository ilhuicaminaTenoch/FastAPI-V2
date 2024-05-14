from fastapi import FastAPI, Body
from starlette.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="Aprendiedo FastAPI",
    description="Una API en los primeros pasos",
    version="0.0.1"
)

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default='Titulo de la pelicula', min_length=5, max_length=60)
    overview: str = Field(default='Descripcion de la pelicula', min_length=15, max_length=60)
    year: int = Field(default=2023)
    rating: float = Field(g=1, le=10)
    category: str = Field(default='Movie', min_length=3, max_length=15)


movies = [
    {
        'id': 1,
        'title': 'El padrino',
        'overview': 'El padrino es una pelicula de 1972 dirigida por Francis Ford Coppola ...',
        'year': 1972,
        'rating': 9.2,
        'category': 'Crimen'
    }
]


@app.get("/", tags=["inicio"])
def read_root():
    #return HTMLResponse(content="<h1>Hello World</h1>")
    return {"Hello": "World"}


@app.get("/movies", tags=["Peliculas"])
def read_movies():
    return movies


@app.get("/movies/{id}", tags=["Peliculas"])
def read_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return []


@app.get("/movies/", tags=["Peliculas"])
def read_movie_by_category(category: str):
    return category


@app.post("/movies", tags=["Peliculas"])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies


@app.put("/movies/{id}", tags=["Peliculas"])
def update_movie(id: int, movie: Movie):
    print(movie)
    for item in movie:
        print(item.title)


@app.delete("/movies/{id}", tags=["Peliculas"])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movie
