import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class UpdateForm(RelationCommand):

    def __init__(self, connection, relation, form):
        super().__init__(connection)
        self.relation = relation
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.relation.id}/form",
                                   json=json.dumps(self.form.__dict__)).execute()
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form: {self.form.name} for relation {self.relation.name}") from re