from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.work_package.work_package_command import WorkPackageCommand
from model.work_package import WorkPackage


class FindAll(WorkPackageCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for work_package in json_obj._embedded.elements:
                yield WorkPackage(work_package)
        except RequestError as re:
            raise BusinessError(f"Error finding all work packages") from re
