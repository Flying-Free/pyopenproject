import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.version.version_command import VersionCommand
from model.version import Version


class FindAll(VersionCommand):
    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.filters}").execute()
            for tEntry in json.loads(json_obj):
                yield Version(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all versions by filters: {self.filters}") from re
