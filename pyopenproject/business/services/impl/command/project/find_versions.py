from pyopenproject import model as v
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand


class FindVersions(ProjectCommand):

    def __init__(self, connection, project):
        """Constructor for class FindVersions, from ProjectCommand

        :param connection: The connection data
        :param project: The project to find its versions
        """
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/versions").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield v.Version(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding all time entries") from re
