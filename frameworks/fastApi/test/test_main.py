#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..main import app, load_json, add_element_json

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_get_movie():
    response = client.get("/movies/1")
    expected_movie = load_json('./data/movies.json')[0]
    assert response.status_code == 200
    assert response.json()[0] == expected_movie
    assert response.json()[0]['title'] == 'Inception'

def test_get_movie_not_found():
    response = client.get("/movies/100")
    assert response.content.decode() == "Movie not found"
    assert response.status_code == 404

def test_add_movie():
    file_path = './data/movies.json'
    new_movie = {
        "id": 6,
        "title": "The Matrix Reload",
        "director": "Lana Wachowski, Lilly Wachowski",
        "release_year": 1999,
        "genre": "Action",
        "rating": 8.7
    }

    response = client.post('/movies', json=new_movie)
    assert response.status_code == 201
