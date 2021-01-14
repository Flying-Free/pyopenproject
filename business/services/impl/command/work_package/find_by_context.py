from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.work_package import WorkPackage


class FindByContext(WorkPackageCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding work package by context: {self.context}") from re
