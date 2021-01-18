import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class Update(RelationCommand):

    def __init__(self, connection, relation):
        super(connection)
        self.relation = relation

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.relation.id}",
                                    json=json.dumps(self.relation.__dict__)).execute()
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating relation by id: {self.relation.id}") from re
