from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.work_package.work_package_command import WorkPackageCommand
from model.schema import Schema


class FindSchema(WorkPackageCommand):

    def __init__(self, schema):
        self.schema = schema

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schemas/{self.schema.id}")
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding the work package schema") from re