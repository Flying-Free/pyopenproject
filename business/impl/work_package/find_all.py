from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.work_package.work_package_command import WorkPackageCommand
from src.extract.model.work_package import WorkPackage


class FindAll(WorkPackageCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for work_package in json_obj._embedded.elements:
                yield WorkPackage(work_package)
        except RequestError as re:
            raise BusinessError(f"Error finding all work packages") from re
