from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.work_package import WorkPackage


class FindAll(WorkPackageCommand):
    def __init__(self, connection, offset, pageSize, filters, sortBy, groupBy, showSums):
        super().__init__(connection)
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy
        self.groupBy = groupBy
        self.showSums = showSums

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}?,{self.offset},{self.pageSize},"
                                  f"{self.filters},{self.sortBy},{self.groupBy},{self.showSums}").execute()
            for work_package in json_obj._embedded.elements:
                yield WorkPackage(work_package)
        except RequestError as re:
            raise BusinessError(f"Error finding all work packages") from re
