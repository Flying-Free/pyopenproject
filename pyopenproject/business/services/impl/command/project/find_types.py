from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand
from pyopenproject.model import Type


class FindTypes(ProjectCommand):

    def __init__(self, connection, project):
        """Constructor for class FindTypes, from ProjectCommand

        :param connection: The connection data
        :param project: The project to get its types
        """
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/types").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield Type(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding work package types") from re
