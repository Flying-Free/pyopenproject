from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.find_list_command import FindListCommand
from src.business.services.command.project.project_command import ProjectCommand
from src.business.util.filters import Filters
from src.business.util.url import URL
from src.business.util.url_parameter import URLParameter
from src.model.project import Project


class FindParents(ProjectCommand):

    def __init__(self, connection, filters, of, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.of = of
        self.sort_by = sort_by

    def execute(self):
        try:
            request = GetRequest(self.connection,
                                 str(URL(f"{self.CONTEXT}/available_parent_projects",
                                         [
                                             Filters(
                                                 self.filters),
                                             URLParameter("of", self.of),
                                             URLParameter("sortBy", self.sort_by)
                                         ])))
            return FindListCommand(self.connection, request, Project).execute()
            # for tEntry in json_obj["_embedded"]["elements"]:
            #     yield p.Project(tEntry)

        except RequestError as re:
            raise BusinessError("Error finding parent project candidates") from re
