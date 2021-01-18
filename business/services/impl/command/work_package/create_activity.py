import json

import model.activity as activity
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand


class CreateActivity(WorkPackageCommand):

    def __init__(self, connection, work_package, activity, notify):
        super().__init__(connection)
        self.work_package = work_package
        self.activity = activity
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.work_package.id}/activities?{self.notify}",
                                   json=json.dumps(self.activity.__dict__)).execute()
            return activity.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating activity for the work package {self.work_package.id}") from re
