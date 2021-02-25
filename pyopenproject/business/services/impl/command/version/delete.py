from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import DeleteRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import VersionCommand


class Delete(VersionCommand):

    def __init__(self, connection, version):
        super().__init__(connection)
        self.version = version

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.version.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting version: {self.version.id}") from re