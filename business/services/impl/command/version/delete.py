from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.version.version_command import VersionCommand
from model.version import Version


class Delete(VersionCommand):

    def __init__(self, version):
        self.version = version

    def execute(self):
        try:
            json_obj = Connection().delete(f"{self.CONTEXT}/{self.version.id}")
            return Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting version: {self.version.id}") from re
