from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.version.version_command import VersionCommand
import model.version as v


class Delete(VersionCommand):

    def __init__(self, connection, version):
        super().__init__(connection)
        self.version = version

    def execute(self):
        try:
            json_obj = DeleteRequest(self.connection, f"{self.CONTEXT}/{self.version._links['id']}").execute()
            return v.Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting version: {self.version.id}") from re
