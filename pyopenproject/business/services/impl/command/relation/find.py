from pyopenproject import model as rel
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import RelationCommand


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
