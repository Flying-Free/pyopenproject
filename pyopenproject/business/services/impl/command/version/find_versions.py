from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TypeCommand
from pyopenproject.model import Version


class FindVersions(TypeCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/versions").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield Version(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding all time entries") from re
