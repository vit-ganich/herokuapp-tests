"""Base CRUD API methods implementation"""

import traceback
import json

import requests
import utilities.logger as logger
import utilities.config as config

from utilities.custom_exceptions import RequestError

config = config.read()


class Base:
    """Parent class for all API's"""

    _url = f"{config['url']}"
    _headers = {'Content-Type': 'application/json'}
    id_list_to_delete = []
    current_id = None

    def read_all(self) -> list:
        """GET all items"""

        try:
            logger.info("\nGET: " + self._url)
            request = requests.get(self._url)

            if request.status_code != 200:
                raise RequestError(request)

            response = request.json()
            collection = response["collection"]
            return collection
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def read(self, item_id: str) -> dict:
        """GET one item by the id"""

        try:
            url = f"{self._url}/{item_id}"
            logger.info("\nGET: " + url)

            request = requests.get(url)

            if request.status_code != 200:
                raise RequestError(request)

            response = request.json()
            return response
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def create_item(self, body: dict) -> dict:
        """POST - create an item"""

        try:
            logger.info("\nPOST: " + self._url)

            request = requests.post(self._url, headers=self._headers, data=json.dumps(body))

            if request.status_code != 201:
                raise RequestError(request)

            response = request.json()
            self.id_list_to_delete.append(response["id"])
            self.current_id = response["id"]
            logger.info(self.current_id)

            return response
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def update_item(self, item_id: int, body: dict):
        """PUT - update an item"""

        try:
            url = f"{self._url}/{item_id}"
            logger.info("\nPUT: " + url)

            request = requests.put(url, headers=self._headers, data=json.dumps(body))

            if request.status_code != 204:
                raise RequestError(request)

            success = request.ok
            assert success is True
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def delete(self, item_id: int):
        """DELETE an item by id"""

        try:
            url = f"{self._url}/{item_id}"
            logger.info("\nDELETE: " + url)

            request = requests.delete(url)

            if request.status_code != 204:
                raise RequestError(request)

            success = request.ok
            assert success is True
            self.id_list_to_delete.remove(item_id)
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex
