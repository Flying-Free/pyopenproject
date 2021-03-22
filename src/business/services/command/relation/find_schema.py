from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.relation.relation_command import RelationCommand
from src.model.schema import Schema


class FindSchema(RelationCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schema").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding schema ") from re
