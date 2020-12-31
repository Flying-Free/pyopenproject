import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.version.version_command import VersionCommand
from model.version import Version


class FindAll(VersionCommand):
    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.filters}")
            for tEntry in json.loads(json_obj):
                yield Version(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all versions by filters: {self.filters}") from re
