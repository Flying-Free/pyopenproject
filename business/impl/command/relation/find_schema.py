from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation

class FindSchema(RelationCommand):

    def __init__(self, relation):
        self.relation = relation

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schema")
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding schema from relation: {self.relation.id}") from re
