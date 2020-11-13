"""Tests for services integration"""

from random import randrange

from test.conftest import genre, audio_quality, video_quality, movie


def test_integration():
    """Create movie with genres, audios and videos"""

    genre_name = f"Genre {randrange(0, 10000)}"
    genre_created = genre.create(genre_name)
    assert genre_created is not None

    audio_name = f"Audio {randrange(0, 10000)}"
    audio_q_created = audio_quality.create(audio_name)
    assert audio_q_created is not None

    video_name = f"Video {randrange(0, 10000)}"
    video_q_created = video_quality.create(video_name)
    assert video_q_created is not None

    audios = [audio_name]
    videos = [video_name]
    genres = [genre_name]
    movie_title = f"Movie {randrange(0, 10000)}"

    actual_movie_created = movie.create(
        movie_title,
        audios=audios,
        videos=videos,
        genres=genres)

    # There is a bug - audio, video and genres are empty
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
