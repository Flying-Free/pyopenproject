from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class FindByContext(RelationCommand):

    def __init__(self, connection, context):
        super(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding project by context: {self.context}") from re
