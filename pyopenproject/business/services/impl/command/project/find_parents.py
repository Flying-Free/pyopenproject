from pyopenproject import model as p
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand
from pyopenproject.business.util import Filters
from pyopenproject.business.util import URL
from pyopenproject.business.util import URLParameter


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
