import json
import os


def load_movies(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


def save_movies(path: str, movies: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(movies, file, ensure_ascii=False, indent=2)


def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    if movies:
        max_id = max(movie['id'] for movie in movies)
        new_id = max_id + 1
    else:
        new_id = 1

    new_movie = {
        'id': new_id,
        'title': title.strip(),
        'year': year,
        'watched': False
    }
    return movies + [new_movie]


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    updated_movies = []
    for movie in movies:
        movie_copy = movie.copy()
        if movie_copy['id'] == movie_id:
            movie_copy['watched'] = True
        updated_movies.append(movie_copy)
    return updated_movies


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    """Поиск всех фильмов указанного года."""
    return [movie for movie in movies if movie.get('year') == year]
