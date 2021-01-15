from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.schema import Schema


class FindSchema(RelationCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schema")
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding schema ") from re
