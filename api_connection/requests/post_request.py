import requests
from requests.auth import HTTPBasicAuth

from api_connection.request import Request


class PostRequest(Request):
    def __init__(self, connection, context, json=None, files=None, headers=None, data=None):
        super().__init__(connection, context, json, files, headers, data)

    def _execute_request(self):
        return requests.post(
            self.connection.url_base + self.context,
            auth=HTTPBasicAuth(self.connection.api_user, self.connection.api_key),
            json=self.json,
            files=self.files,
            headers=self.headers,
            data=self.data
        )
