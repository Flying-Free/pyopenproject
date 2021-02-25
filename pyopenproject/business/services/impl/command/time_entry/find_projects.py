from pyopenproject import model as p
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TimeEntryCommand


class FindAvailableProjects(TimeEntryCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/available_projects").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding all available projects") from re
