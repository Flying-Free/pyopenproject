from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.project.project_command import ProjectCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import work_package as wp


class FindWorkPackages(ProjectCommand):

    def __init__(self, connection, project, offset, page_size, filters, group_by, sort_by, show_sums):
        super().__init__(connection)
        self.project = project
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.group_by = group_by
        self.sort_by = sort_by
        self.show_sums = show_sums

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  str(URL(f"{self.CONTEXT}/{self.project.id}/work_packages",
                                          [
                                              URLParameter("offset", self.offset),
                                              URLParameter("pageSize", self.page_size),
                                              Filters(
                                                  self.filters),
                                              URLParameter("groupBy", self.group_by),
                                              URLParameter("sortBy", self.sort_by),
                                              URLParameter("showSums", self.show_sums),
                                          ])
                                      )).execute()
            for wP in json_obj["_embedded"]["elements"]:
                yield wp.WorkPackage(wP)
        except RequestError as re:
            raise BusinessError(f"Error finding work packages for project: {self.project.name}") from re
