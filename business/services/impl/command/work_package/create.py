import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.work_package import WorkPackage


class Create(WorkPackageCommand):

    def __init__(self, connection, work_package, notify):
        super().__init__(connection)
        self.work_package = work_package
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}?{self.notify}",
                                   json=json.dumps(self.work_package.__dict__)).execute()
            return WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating work package") from re
