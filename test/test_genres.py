"""Genres tests"""

from random import randrange

from test.conftest import genre
from utilities.custom_exceptions import RequestError


def test_get_genres():
    """Get all items, check that the response list is not empty"""

    genres_list = genre.read_all()
    assert len(genres_list) > 0


def test_create_genre():
    """Create an item, check it was created correctly"""

    genre_name = f"Genre {randrange(0, 10000)}"
    actual_genre_created = genre.create(genre_name)
    genre_id = actual_genre_created["id"]

    expected_genre = {
        'id': genre_id,
        'name': genre_name
    }

    assert actual_genre_created == expected_genre

    actual_genre_get = genre.read(genre_id)
    assert actual_genre_get == expected_genre


def test_update_genre():
    """Update the item, check it was updated correctly"""

    name = f"New Genre {randrange(0, 10000)}"
    genre_id = genre.current_id
    genre.update(genre_id, name)

    exp_genre = {
        "id": genre_id,
        "name": name
    }

    actual_genre = genre.read(genre_id)
    assert actual_genre == exp_genre


def test_delete_genre():
    """Delete the item, check it was deleted (not found)"""

    genre_id = genre.current_id
    genre.delete(genre_id)

    expected_genre = None
    try:
        expected_genre = genre.read(genre_id)
    except RequestError:
        # If the request failed - it means, that the item was deleted
        pass

    assert expected_genre is None, f"Genre {genre_id} was not deleted"
