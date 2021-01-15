import requests
from requests.auth import HTTPBasicAuth

from api_connection.request import Request


class PatchRequest(Request):
    def _execute_request(self):
        return requests.patch(
            self.url_base + self.context,
            auth=HTTPBasicAuth(self.api_user, self.api_key),
            json=self.json
        )
