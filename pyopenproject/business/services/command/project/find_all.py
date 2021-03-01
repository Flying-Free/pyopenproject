from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import project as p


class FindAll(ProjectCommand):
    def __init__(self, connection, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters(
                                                                   self.filters),
                                                               URLParameter
                                                               ("sortBy", self.sort_by)
                                                           ]))).execute()

            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)

        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.filters},{self.sort_by}") from re
