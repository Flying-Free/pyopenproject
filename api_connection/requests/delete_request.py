import requests
from requests.auth import HTTPBasicAuth

from api_connection.request import Request


class DeleteRequest(Request):

    def __init__(self, connection, context):
        super(connection, context)

    def _execute_request(self):
        return requests.delete(
            self.connection.url_base + self.context,
            auth=HTTPBasicAuth(self.connection.api_user, self.connection.api_key)
        )
