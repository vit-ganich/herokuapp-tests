from api.base import Base


class Genre(Base):
    _url = Base._url + "/genres"
    id_list_to_delete = []
    current_id = ""

    def create(self, name):
        body = {
            "name": name
        }
        return Base.create(self, body)

    def update(self, genre_id: int, name: str):
        body = {
            "name": name
        }
        return Base.update(self, genre_id, body)