import json

import model.work_package as wp
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from util.URL import URL
from util.URLParameter import URLParameter


class Update(WorkPackageCommand):

    def __init__(self, connection, work_package, notify):
        super().__init__(connection)
        self.work_package = work_package
        self.notify = notify

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=  str(URL(f"{self.CONTEXT}/{self.work_package.id}",
                                          [
                                              URLParameter("notify", self.notify)
                                          ])),
                                    json=json.dumps(self.work_package.__dict__)).execute()
            return wp.WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating work package: {self.work_package.id}") from re
