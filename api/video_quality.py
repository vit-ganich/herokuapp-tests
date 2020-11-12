from api.base import Base


class VideoQuality(Base):
    _url = Base._url + "/video_qualities"
    id_list_to_delete = []
    current_id = ""

    def create(self, name: str, abbr="AbbrVideoTest", position=1, default=False) -> dict:
        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        response = Base.create(self, body)
        return response

    def update(self, item_id, name: str, abbr="NewAbbrVideoTest", position=20, default=True):
        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        Base.update(self, item_id, body)
