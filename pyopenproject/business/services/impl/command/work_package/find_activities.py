from pyopenproject import model as act
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand


class FindActivities(WorkPackageCommand):

    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}{self.work_package.id}/activities").execute()
            for activity in json_obj["_embedded"]["elements"]:
                yield act.Activity(activity)
        except RequestError as re:
            raise BusinessError(f"Error finding activities for work package {self.work_package.id}") from re
