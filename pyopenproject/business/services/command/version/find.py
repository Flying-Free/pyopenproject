from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.version.version_command import VersionCommand
from pyopenproject.model import project as p


class Find(VersionCommand):

    def __init__(self, connection, version):
        super().__init__(connection)
        self.version = version

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.version.id}").execute()
            return p.Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding version by id: {self.version.name}") from re
