from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.version.version_command import VersionCommand
from pyopenproject.model import project as p


class FindProjects(VersionCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/available_projects").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding projects available for versions") from re
