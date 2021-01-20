import model.user as usr
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand


class DeleteWatcher(WorkPackageCommand):

    def __init__(self, connection, work_package, watcher):
        super().__init__(connection)
        self.work_package = work_package
        self.watcher = watcher

    def execute(self):
        try:
            json_obj = DeleteRequest(self.connection,
                                     f"{self.CONTEXT}/{self.work_package.id}/watchers/{self.watcher.id}").execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting watcher {self.watcher.id} "
                                f"for the work package {self.work_package.id}") from re
