from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.relation import Relation


class FindRelations(WorkPackageCommand):
    def __init__(self, work_package):
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.work_package.id}/relations")
            for relation in json_obj._embedded.elements:
                yield Relation(relation)
        except RequestError as re:
            raise BusinessError(f"Error finding relations for work package {self.work_package.id}") from re