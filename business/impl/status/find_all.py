from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.status.status_command import StatusCommand
from src.extract.business.impl.work_package.work_package_command import WorkPackageCommand
from src.extract.model.status import Status
from src.extract.model.work_package import WorkPackage


class FindAll(StatusCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding all statuses") from re
