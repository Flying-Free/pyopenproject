from pyopenproject import model as wp
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PatchRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand
from pyopenproject.business.util import URL
from pyopenproject.business.util import URLParameter


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
