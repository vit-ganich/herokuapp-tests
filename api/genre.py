"""Genres API"""

from api.base import Base


class Genre(Base):
    """Genre implementation of Base API class"""

    _url = Base._url + "/genres"
    id_list_to_delete = []
    current_id = ""

    def create(self, name):
        """Create Genre"""

        body = {
            "name": name
        }
        return Base.create_item(self, body)

    def update(self, genre_id: int, name: str):
        """Update Genre"""

        body = {
            "name": name
        }
        return Base.update_item(self, genre_id, body)
