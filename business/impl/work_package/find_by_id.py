from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.work_package.work_package_command import WorkPackageCommand
from src.extract.model.work_package import WorkPackage


class FindById(WorkPackageCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.identifier}")
            return WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by id: {self.identifier}") from re
