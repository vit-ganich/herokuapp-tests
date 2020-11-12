from random import randrange

from test.conftest import genre


def test_get_genres():
    genres_list = genre.get_all()
    assert len(genres_list) > 0


def test_create_genre():
    genre_name = f"Genre {randrange(0, 10000)}"
    actual_genre_created = genre.create(genre_name)
    genre_id = actual_genre_created["id"]

    expected_genre = {
        'id': genre_id,
        'name': genre_name
    }

    assert actual_genre_created == expected_genre

    actual_genre_get = genre.get(genre_id)
    assert actual_genre_get == expected_genre


def test_update_genre():
    name = f"New Genre {randrange(0, 10000)}"
    genre_id = genre.current_id
    genre.update(genre_id, name)

    exp_genre = {
        "id": genre_id,
        "name": name
    }

    actual_genre = genre.get(genre_id)
    assert actual_genre == exp_genre


def test_delete_genre():
    genre_id = genre.current_id
    genre.delete(genre_id)

    expected_genre = None
    try:
        expected_genre = genre.get(genre_id)
    except ConnectionRefusedError:
        pass

    assert expected_genre is None, f"Genre {genre_id} was not deleted"
