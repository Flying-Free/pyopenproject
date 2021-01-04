import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.work_package.work_package_command import WorkPackageCommand
from model.schema import Schema


class FindAllSchemas(WorkPackageCommand):
    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schemas?{self.filters}")
            for tEntry in json.loads(json_obj):
                yield Schema(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all schemas by filters: {self.filters}") from re