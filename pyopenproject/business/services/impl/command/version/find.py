from pyopenproject import model as p
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import VersionCommand


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
