#!/usr/bin/env python3
from fastapi import FastAPI, Response
import json


app = FastAPI()




def load_json(file_path):
    with open(file_path, 'r') as filejson:
        return json.load(filejson)

def add_element_json(file_path, new_element):
    elements = load_json(file_path)
    with open(file_path, 'w') as filejson:
        elements.append(new_element)
        json.dump(elements, filejson, indent=4)

def del_element_json(file_path, element_id):
    elements = load_json(file_path)
    keep_elements = [
        element for element in elements if element.get('id') != element_id]

    with open(file_path, 'w') as filejson:
        json.dump(keep_elements, filejson, indent=4)


_movies = 'data/movies.json'

@app.get("/")
async def root():
    "Root"
    return {"message": "Hello World"}

@app.get("/movies/{movie_id:int}")
async def get_movie(movie_id: int):
    movies = load_json(_movies)
    movie = list(filter(lambda movie: movie.get('id') == movie_id, movies))

    if not movie:
        return Response(content="Movie not found", status_code=404)
    return movie

@app.post("/movies", status_code=201)
async def create_movie(movie: dict):
    try:
        add_element_json(_movies, movie)
        return load_json(_movies)
    except ValueError as error:
        raise Exception(error)

@app.delete("/movies/{movie_id:int}", status_code=200)
async def delete_movie(movie_id: int):
    try:
        del_element_json(_movies, movie_id)
    except ValueError as error:
        raise Exception(error)
