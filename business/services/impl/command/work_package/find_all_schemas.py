import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.schema import Schema


class FindAllSchemas(WorkPackageCommand):
    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schemas?{self.filters}").execute()
            for tEntry in json.loads(json_obj):
                yield Schema(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all schemas by filters: {self.filters}") from re
