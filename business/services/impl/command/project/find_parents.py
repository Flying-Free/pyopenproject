import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindParents(ProjectCommand):

    def __init__(self, connection, filters, of, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.of = of
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  str(URL(f"{self.CONTEXT}/available_parent_projects",
                                          [
                                              Filters("filters", self.filters),
                                              URLParameter("of", self.of),
                                              URLParameter("sortBy", self.sort_by)
                                          ])
                                      )).execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)

        except RequestError as re:
            raise BusinessError("Error finding parent project candidates") from re
