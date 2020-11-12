import traceback

import requests
import utilities.logger as logger
import utilities.config as config
import json

config = config.read()


class Base:

    _url = f"{config['url']}"
    _headers = {'Content-Type': 'application/json'}
    id_list_to_delete = []
    current_id = None

    def get_all(self) -> list:
        try:
            logger.info("\nGET: " + self._url)
            request = requests.get(self._url)

            if request.status_code != 200:
                raise ConnectionRefusedError(f"status: {request.status_code}. URL: {request.url}\n{request.text}")

            response = request.json()
            collection = response["collection"]
            return collection
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def get(self, item_id: str) -> dict:
        try:
            url = f"{self._url}/{item_id}"
            logger.info("\nGET: " + url)

            request = requests.get(url)

            if request.status_code != 200:
                raise ConnectionRefusedError(f"status: {request.status_code}. URL: {request.url}\n{request.text}")

            response = request.json()
            return response
        except Exception as ex:
            logger.debug(traceback.format_exc())

    def create(self, body: dict) -> dict:
        try:
            logger.info("\nPOST: " + self._url)

            request = requests.post(self._url, headers=self._headers, data=json.dumps(body))

            if request.status_code != 201:
                raise ConnectionRefusedError(f"status: {request.status_code}. URL: {request.url}\n{request.text}")

            response = request.json()
            self.id_list_to_delete.append(response["id"])
            self.current_id = response["id"]
            logger.info(self.current_id)

            return response
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def update(self, item_id: int, body: dict):
        try:
            url = f"{self._url}/{item_id}"
            logger.info("\nPUT: " + url)

            request = requests.put(url, headers=self._headers, data=json.dumps(body))

            if request.status_code != 204:
                raise ConnectionRefusedError(f"status: {request.status_code}. URL: {request.url}\n{request.text}")

            success = request.ok
            assert success is True
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex

    def delete(self, item_id: int):
        try:
            url = f"{self._url}/{item_id}"
            logger.info("\nDELETE: " + url)

            request = requests.delete(url)

            if request.status_code != 204:
                raise ConnectionRefusedError(f"status: {request.status_code}. URL: {request.url}\n{request.text}")

            success = request.ok
            assert success is True
            self.id_list_to_delete.remove(item_id)
        except Exception as ex:
            logger.debug(traceback.format_exc())
            raise ex