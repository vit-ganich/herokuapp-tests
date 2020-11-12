# from test.test_base import TestBase
from random import randrange

from test.conftest import movie


def test_get_movies():
    movies_list = movie.get_all()
    assert len(movies_list) > 0


def test_create_movie():
    movie_title = f"Movie {randrange(0, 10000)}"
    actual_movie_created = movie.create(movie_title)
    movie_id = actual_movie_created["id"]

    expected_movie = {
        'id': movie_id,
        'title': movie_title,
        'year': 2020,
        'plot': 'Lorem ipsum dolor sit amet',
        'duration': 120,
        'audio_qualities': [],
        'video_qualities': [],
        'genres': []
    }

    assert actual_movie_created == expected_movie

    actual_movie_get = movie.get(movie_id)
    assert actual_movie_get == expected_movie


def test_update_movie():
    movie_title = f"New Movie {randrange(0, 10000)}"
    movie_id = movie.current_id
    movie.update(movie_id, movie_title)

    exp_movie = {
        'id': movie_id,
        'title': movie_title,
        'year': 2021,
        'plot': 'New Lorem ipsum dolor sit amet',
        'duration': 200,
        'audio_qualities': [],
        'video_qualities': [],
        'genres': []
    }

    actual_movie = movie.get(movie_id)
    assert actual_movie == exp_movie


def test_delete_movie():
    movie_id = movie.current_id
    movie.delete(movie_id)

    expected_movie = None
    try:
        expected_movie = movie.get(movie_id)
    except ConnectionRefusedError:
        pass

    assert expected_movie is None, f"Movie {movie_id} was not deleted"
