from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.patch_request import PatchRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import work_package as wp


class Update(WorkPackageCommand):

    def __init__(self, connection, work_package, notify):
        super().__init__(connection)
        self.work_package = work_package
        self.notify = notify

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=str(URL(f"{self.CONTEXT}{self.work_package.id}",
                                                    [
                                                        URLParameter("notify", self.notify)
                                                    ])),
                                    json=self.work_package.__dict__).execute()
            return wp.WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating work package: {self.work_package.id}") from re
