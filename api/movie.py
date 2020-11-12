from api.base import Base


class Movie(Base):
    _url = Base._url + "/movies"
    id_list_to_delete = []
    current_id = ""

    def create(self, title: str, year=2020, plot="Lorem ipsum dolor sit amet", duration=120):
        body = {
            "title": title,
            "year": year,
            "plot": plot,
            "duration": duration,
            "audio_qualities": [],
            "video_qualities": [],
            "genres": []
        }
        response = Base.create(self, body)
        return response

    def update(self, item_id: int, title: str, year=2021, plot="New Lorem ipsum dolor sit amet", duration=200):
        body = {
            "title": title,
            "year": year,
            "plot": plot,
            "duration": duration,
            "audio_qualities": [],
            "video_qualities": [],
            "genres": []
        }
        response = Base.update(self, item_id, body)
        return response
