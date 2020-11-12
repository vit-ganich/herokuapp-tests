from api.base import Base


class AudioQuality(Base):
    _url = Base._url + "/audio_qualities"
    id_list_to_delete = []
    current_id = ""

    def create(self, name: str, abbr="AbbrAudioTest", position=1, default=False) -> dict:
        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        response = Base.create(self, body)
        return response

    def update(self, item_id: int, name: str, abbr="NewAbbrAudioTest", position=20, default=True):
        body = {
            "name": name,
            "abbr": abbr,
            "position": position,
            "default": default
        }

        Base.update(self, item_id, body)

