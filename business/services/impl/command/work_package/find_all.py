from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.work_package import WorkPackage


class FindAll(WorkPackageCommand):
    def __init__(self, offset, pageSize, filters, sortBy, groupBy, showSums):
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy
        self.groupBy = groupBy
        self.showSums = showSums

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?,{self.offset},{self.pageSize},{self.filters},{self.sortBy},{self.groupBy},{self.showSums}")
            for work_package in json_obj._embedded.elements:
                yield WorkPackage(work_package)
        except RequestError as re:
            raise BusinessError(f"Error finding all work packages") from re
