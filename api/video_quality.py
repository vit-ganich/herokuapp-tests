"""Video Qualities API"""

from api.base import Base


class VideoQuality(Base):
    """Video Quality implementation of Base API class"""

    _url = Base._url + "/video_qualities"
    id_list_to_delete = []
    current_id = ""

    def create(self, name: str, abbr="AbbrVideoTest", position=1, default=False) -> dict:
        """Create Video Quality"""

        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        response = Base.create_item(self, body)
        return response

    def update(self, item_id, name: str, abbr="NewAbbrVideoTest", position=20, default=True):
        """Update Video Quality"""

        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        Base.update_item(self, item_id, body)
