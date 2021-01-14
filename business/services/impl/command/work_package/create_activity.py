import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
import model.activity as activity


class CreateActivity(WorkPackageCommand):

    def __init__(self, work_package, activity, notify):
        self.work_package = work_package
        self.activity = activity
        self.notify = notify

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.work_package.id}/activities?{self.notify}", json.dumps(self.activity.__dict__))
            return activity.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating activity for the work package {self.work_package.id}") from re