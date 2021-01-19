import requests
from requests.auth import HTTPBasicAuth

from api_connection.request import Request


class GetRequest(Request):

    def __init__(self, connection, context):
        super().__init__(connection, context)

    def _execute_request(self):
        return requests.get(
            self.connection.url_base + self.context,
            auth=HTTPBasicAuth(self.connection.api_user, self.connection.api_key)
        )
