from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.user import User


class FindWatchers(WorkPackageCommand):
    def __init__(self, work_package):
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.work_package.id}/watchers")
            for watcher in json_obj._embedded.elements:
                yield User(watcher)
        except RequestError as re:
            raise BusinessError(f"Error finding watchers for work package {self.work_package.id}") from re