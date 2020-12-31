import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.version.version_command import VersionCommand
from model.version import Version


class Update(VersionCommand):

    def __init__(self, version):
        self.version = version

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.version.id}", json.dumps(self.version.__dict__))
            return Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating version: {self.version.id}") from re
