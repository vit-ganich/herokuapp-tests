"""Movies tests"""

from random import randrange

from test.conftest import movie
from utilities.custom_exceptions import RequestError


def test_get_movies():
    """Get all items, check that the response list is not empty"""

    movies_list = movie.read_all()
    assert len(movies_list) > 0


def test_create_movie():
    """Create an item, check it was created correctly"""

    movie_title = f"Movie {randrange(0, 10000)}"
    actual_movie_created = movie.create(movie_title)

    expected_movie = {
        'id': movie.current_id,
        'title': movie_title,
        'year': 2020,
        'plot': 'Lorem ipsum dolor sit amet',
        'duration': 120,
        'audio_qualities': [],
        'video_qualities': [],
        'genres': []
    }

    assert actual_movie_created == expected_movie

    actual_movie_get = movie.read(movie.current_id)
    assert actual_movie_get == expected_movie


def test_negative_verify_error_message():
    """Verify the error message if parameter missing"""
    name = ""
    actual_msg = ""
    exp_msg = "Validation failed: Title can't be blank"

    try:
        movie.create(name)
    except RequestError as err:
        actual_msg = err.message

    assert exp_msg in actual_msg


def test_update_movie():
    """Update the item, check it was updated correctly"""

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

    actual_movie = movie.read(movie_id)
    assert actual_movie == exp_movie


def test_delete_movie():
    """Delete the item, check it was deleted (not found)"""

    movie_id = movie.current_id
    movie.delete(movie_id)

    expected_movie = None
    try:
        expected_movie = movie.read(movie_id)
    except RequestError:
        # If the request failed - it means, that the item was deleted
        pass

    assert expected_movie is None, f"Movie {movie_id} was not deleted"
