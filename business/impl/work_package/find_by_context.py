from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.work_package.work_package_command import WorkPackageCommand
from src.extract.model.work_package import WorkPackage


class FindByContext(WorkPackageCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by context: {self.context}") from re
