from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import DeleteRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand


class Delete(WorkPackageCommand):

    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            return DeleteRequest(self.connection, f"{self.CONTEXT}{self.work_package.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting work package: {self.work_package.id}") from re
