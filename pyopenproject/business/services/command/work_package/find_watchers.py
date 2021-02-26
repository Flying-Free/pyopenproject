from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.model import user  as usr


class FindWatchers(WorkPackageCommand):
    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}{self.work_package.id}/watchers").execute()
            for watcher in json_obj["_embedded"]["elements"]:
                yield usr.User(watcher)
        except RequestError as re:
            raise BusinessError(f"Error finding watchers for work package {self.work_package.id}") from re
