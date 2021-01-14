from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.user import User


class DeleteWatcher(WorkPackageCommand):

    def __init__(self, work_package, watcher):
        self.work_package = work_package
        self.watcher = watcher

    def execute(self):
        try:
            json_obj = Connection().delete(f"{self.CONTEXT}/{self.work_package.id}/watchers/{self.watcher.id}")
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error deleting watcher {self.watcher.id} for the work package {self.work_package.id}") from re