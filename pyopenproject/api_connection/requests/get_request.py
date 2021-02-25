import requests
from requests.auth import HTTPBasicAuth

from pyopenproject.api_connection.request import Request


class GetRequest(Request):

    def __init__(self, connection, context):
        super().__init__(connection, context)

    def _execute_request(self):
        with requests.Session() as s:
            s.auth = HTTPBasicAuth(self.connection.api_user, self.connection.api_key)
            s.headers.update({"Content-Type": "application/hal+json"})
            response = s.get(self.connection.url_base + self.context)
        return response
