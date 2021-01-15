from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.relation import Relation


class FindRelationCandidatesByWorkPackage(WorkPackageCommand):
    def __init__(self, work_package, filters, query, type, pageSize):
        self.work_package = work_package
        self.filters = filters
        self.query = query
        self.type = type
        self.pageSize = pageSize

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.work_package.id}/available_relation_candidates?{self.filters},{self.query},{self.type},.{self.pageSize}")
            for relation in json_obj._embedded.elements:
                yield Relation(relation)
        except RequestError as re:
            raise BusinessError(f"Error finding relation candidates for work package {self.work_package.id}") from re