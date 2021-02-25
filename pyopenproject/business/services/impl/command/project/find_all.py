from pyopenproject import model as p
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import ProjectCommand
from pyopenproject.business.util import Filters
from pyopenproject.business.util import URL
from pyopenproject.business.util import URLParameter


class FindAll(ProjectCommand):
    def __init__(self, connection, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters("filters", self.filters),
                                                               URLParameter("sortBy", self.sort_by)
                                                           ]))).execute()

            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)

        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.filters},{self.sort_by}") from re
