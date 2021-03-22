from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from openproject.business.util.filters import Filters
from openproject.business.util.url import URL
from openproject.model.schema import Schema


class FindAllSchemas(WorkPackageCommand):
    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}/schemas",
                                                           [
                                                               Filters(
                                                                   self.filters)
                                                           ])))
            return FindListCommand(self.connection, request, Schema).execute()
            # for schema in json_obj["_embedded"]["elements"]:
            #     yield Schema(schema)
        except RequestError as re:
            raise BusinessError(f"Error finding all schemas by filters: {self.filters}") from re
