from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.relation.relation_command import RelationCommand
from openproject.model import relation as rel


class Find(RelationCommand):

    def __init__(self, connection, relation):
        super().__init__(connection)
        self.relation = relation

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.relation.id}").execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding relation by id: {self.relation.id}") from re
