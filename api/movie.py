"""Movies API"""

from api.base import Base


class Movie(Base):
    """Movie implementation of Base API class"""

    _url = Base._url + "/movies"
    id_list_to_delete = []
    current_id = ""

    def create(self, title: str, year=2020, plot="Lorem ipsum dolor sit amet",
               duration=120, audios=None, videos=None, genres=None):
        """Create Movie"""

        if genres is None:
            genres = []
        if videos is None:
            videos = []
        if audios is None:
            audios = []

        body = {
            "title": title,
            "year": year,
            "plot": plot,
            "duration": duration,
            "audio_qualities": audios,
            "video_qualities": videos,
            "genres": genres
        }
        response = Base.create_item(self, body)
        return response

    def update(self, item_id: int, title: str, year=2021,
               plot="New Lorem ipsum dolor sit amet", duration=200):
        """Update Movie"""

        body = {
            "title": title,
            "year": year,
            "plot": plot,
            "duration": duration,
            "audio_qualities": [],
            "video_qualities": [],
            "genres": []
        }
        Base.update_item(self, item_id, body)
