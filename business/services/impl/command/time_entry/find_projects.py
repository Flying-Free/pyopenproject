import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand


class FindAvailableProjects(TimeEntryCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/available_projects").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.context}") from re
