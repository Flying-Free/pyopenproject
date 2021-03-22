from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.delete_request import DeleteRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand


class DeleteWatcher(WorkPackageCommand):

    def __init__(self, connection, work_package, watcher):
        super().__init__(connection)
        self.work_package = work_package
        self.watcher = watcher

    def execute(self):
        try:
            DeleteRequest(self.connection,
                          f"{self.CONTEXT}/{self.work_package.id}/watchers/{self.watcher.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting watcher {self.watcher.id} "
                                f"for the work package {self.work_package.id}") from re
