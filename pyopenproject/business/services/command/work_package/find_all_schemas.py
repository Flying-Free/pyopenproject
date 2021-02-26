from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.model.schema import Schema


class FindAllSchemas(WorkPackageCommand):
    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}/schemas",
                                                           [
                                                               Filters(
                                                                   self.filters)
                                                           ]))).execute()

            for schema in json_obj["_embedded"]["elements"]:
                yield Schema(schema)
        except RequestError as re:
            raise BusinessError(f"Error finding all schemas by filters: {self.filters}") from re
