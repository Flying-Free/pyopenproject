import requests
from requests.auth import HTTPBasicAuth

from pyopenproject.api_connection.request import Request


class PostRequest(Request):
    def __init__(self, connection, context, json=None, files=None, headers=None, data=None):
        super().__init__(connection, context, json, files, headers, data)

    def _execute_request(self):
        with requests.Session() as s:
            s.auth = HTTPBasicAuth(self.connection.api_user, self.connection.api_key)
            if self.headers is not None:
                s.headers.update(self.headers)
            response = s.post(
                url=self.connection.url_base + self.context,
                json=self.json,
                files=self.files,
                data=self.data)
        return response
