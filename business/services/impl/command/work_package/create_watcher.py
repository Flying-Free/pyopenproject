import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.user import User


class CreateWatcher(WorkPackageCommand):

    def __init__(self, work_package, watcher):
        self.work_package = work_package
        self.watcher = watcher

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.work_package.id}/watchers", json.dumps(self.watcher.__dict__))
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating watcher for the work package {self.work_package.id}") from re