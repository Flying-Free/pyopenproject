from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.delete_request import DeleteRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.relation.relation_command import RelationCommand


class Delete(RelationCommand):

    def __init__(self, connection, relation):
        super().__init__(connection)
        self.relation = relation

    def execute(self):
        try:
            return DeleteRequest(self.connection, f"{self.CONTEXT}/{self.relation.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error updating relation by id: {self.relation.id}") from re
