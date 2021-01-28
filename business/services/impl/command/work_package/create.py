import json

import model.work_package as wp
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand


class Create(WorkPackageCommand):

    def __init__(self, connection, work_package, notify=None):
        super().__init__(connection)
        self.work_package = work_package
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}?notify={self.notify}",
                                   json=json.dumps(self.work_package.__dict__)).execute()
            return wp.WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating work package") from re
