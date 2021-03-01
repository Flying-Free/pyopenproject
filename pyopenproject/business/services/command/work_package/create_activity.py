from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import activity as activity


class CreateActivity(WorkPackageCommand):

    def __init__(self, connection, work_package, comment, notify):
        super().__init__(connection)
        self.work_package = work_package
        self.comment = {
            "comment": {
                "raw": f"{comment}"
            }
        }
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=str(URL(f"{self.CONTEXT}{self.work_package.id}/activities",
                                                   [
                                                       URLParameter
                                                       ("notify", self.notify)
                                                   ])),
                                   json=self.comment).execute()
            return activity.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating activity for the work package {self.work_package.id}") from re
