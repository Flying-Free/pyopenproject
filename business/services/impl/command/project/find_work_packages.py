import model.work_package as wp
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class FindWorkPackages(ProjectCommand):

    def __init__(self, connection, project, offset, pageSize, filters, sortBy, groupBy, showSums, notify):
        super().__init__(connection)
        self.project = project
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy
        self.groupBy = groupBy
        self.showSums = showSums
        self.notify = notify

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}/{self.project.id}/work_packages?{self.offset},"
                                  f"{self.pageSize},{self.filters},{self.sortBy},{self.groupBy},"
                                  f"{self.showSums},{self.notify}").execute()
            for wP in json_obj["_embedded"]["elements"]:
                yield wp.WorkPackage(wP)
        except RequestError as re:
            raise BusinessError(f"Error finding workpackage by id: {self.project.name}") from re
