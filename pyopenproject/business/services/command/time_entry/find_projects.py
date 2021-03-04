from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from pyopenproject.model.project import Project


class FindAvailableProjects(TimeEntryCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}/available_projects")
            return FindListCommand(self.connection, request, Project).execute()
            # for tEntry in json_obj["_embedded"]["elements"]:
            #     yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding all available projects") from re
