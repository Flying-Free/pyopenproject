import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.relation import Relation


class CreateRelation(WorkPackageCommand):

    def __init__(self, work_package, relation):
        self.work_package = work_package
        self.relation = relation

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.work_package.id}/relations", json.dumps(self.relation.__dict__))
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating relation for the work package {self.work_package.id}") from re