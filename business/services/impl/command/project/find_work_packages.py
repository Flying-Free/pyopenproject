import model.work_package as wp
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from util.Filter import Filter
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindWorkPackages(ProjectCommand):

    def __init__(self, connection, project, offset, page_size, filters, group_by, sort_by, show_sums, notify):
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
                                              Filters("filters", self.filters),
                                              URLParameter("groupBy", self.group_by),
                                              URLParameter("sortBy", self.sort_by),
                                              URLParameter("showSums", self.show_sums),
                                          ])
                                          )).execute()
            for wP in json_obj["_embedded"]["elements"]:
                yield wp.WorkPackage(wP)
        except RequestError as re:
            raise BusinessError(f"Error finding workpackage by id: {self.project.name}") from re
