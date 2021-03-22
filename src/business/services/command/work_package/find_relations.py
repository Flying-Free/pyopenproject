from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.find_list_command import FindListCommand
from src.business.services.command.work_package.work_package_command import WorkPackageCommand
from src.model.relation import Relation


class FindRelations(WorkPackageCommand):
    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}{self.work_package.id}/relations")
            return FindListCommand(self.connection, request, Relation).execute()
            # for relation in json_obj["_embedded"]["elements"]:
            #     yield rel.Relation(relation)
        except RequestError as re:
            raise BusinessError(f"Error finding relations for work package {self.work_package.id}") from re
