"""Audio Qualities API"""

from api.base import Base


class AudioQuality(Base):
    """Audio Quality implementation of Base API class"""

    _url = Base._url + "/audio_qualities"
    id_list_to_delete = []
    current_id = ""

    def create(self, name: str, abbr="AbbrAudioTest", position=1, default=False) -> dict:
        """Create Audio Quality"""

        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        response = Base.create_item(self, body)
        return response

    def update(self, item_id: int, name: str, abbr="NewAbbrAudioTest", position=20, default=True):
        """Update Audio Quality"""

        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        Base.update_item(self, item_id, body)
