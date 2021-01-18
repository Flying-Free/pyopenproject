from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class Find(RelationCommand):

    def __init__(self, connection, relation):
        super(connection)
        self.relation = relation

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.relation.id}").execute()
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding relation by id: {self.relation.id}") from re
