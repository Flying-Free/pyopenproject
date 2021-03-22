import requests
from requests.auth import HTTPBasicAuth

from pyopenproject.api_connection.request import Request


class DeleteRequest(Request):

    def __init__(self, connection, context):
        super().__init__(connection, context)

    def _execute_request(self):
        with requests.Session() as s:
            s.auth = HTTPBasicAuth(self.connection.api_user, self.connection.api_key)
            s.headers.update({'Content-Type': 'application/json;charset=utf-8'})
            response = s.delete(url=self.connection.url_base + self.context)
        return response
