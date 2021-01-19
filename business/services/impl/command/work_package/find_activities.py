from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.activity import Activity


class FindActivities(WorkPackageCommand):

    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}/{self.work_package.id}/activities").execute()
            for activity in json_obj._embedded.elements:
                yield Activity(activity)
        except RequestError as re:
            raise BusinessError(f"Error finding activities for work package {self.work_package.id}") from re