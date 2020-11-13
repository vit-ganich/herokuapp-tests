"""Test configuration for all tests"""

from pytest import fixture

from api.audio_quality import AudioQuality
from api.genre import Genre
from api.movie import Movie
from api.video_quality import VideoQuality

movie = Movie()
audio_quality = AudioQuality()
video_quality = VideoQuality()
genre = Genre()


@fixture(scope="session", autouse=True)
def hook():
    """Setup and teardown hooks"""
    yield
    print("\nTeardown")

    for _id in movie.id_list_to_delete:
        movie.delete(_id)
        print(f"Movie {_id} deleted")

    for _id in audio_quality.id_list_to_delete:
        audio_quality.delete(_id)
        print(f"Audio Quality {_id} deleted")

    for _id in video_quality.id_list_to_delete:
        video_quality.delete(_id)
        print(f"Video Quality {_id} deleted")

    for _id in genre.id_list_to_delete:
        genre.delete(_id)
        print(f"Genre {_id} deleted")
