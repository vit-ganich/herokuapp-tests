"""Movies API"""

from api.base import Base


class Movie(Base):
    """Movie implementation of Base API class"""

    _url = Base._url + "/movies"
    id_list_to_delete = []
    current_id = ""

    def create(self, title: str, year=2020, plot="Lorem ipsum dolor sit amet", duration=120):
        """Create Movie"""

        body = {
            "title": title,
            "year": year,
            "plot": plot,
            "duration": duration,
            "audio_qualities": [],
            "video_qualities": [],
            "genres": []
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
