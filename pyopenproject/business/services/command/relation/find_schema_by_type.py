from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.relation.relation_command import RelationCommand
from pyopenproject.model.schema import Schema


class FindSchemaByType(RelationCommand):

    def __init__(self, connection, relation_type):
        """Constructor for class FindSchemaByType, from RelationCommand
        :param connection:
        :param relation_type:
        """
        super().__init__(connection)
        self.relation_type = relation_type

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/schema/{self.relation_type}").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding relation schema") from re
