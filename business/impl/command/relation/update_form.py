import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.relation.relation_command import RelationCommand
from model.relation import Relation


class UpdateForm(RelationCommand):

    def __init__(self, relation, form):
        self.relation = relation
        self.form = form

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.relation.id}/form", json.dumps(self.form.__dict__))
            return Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form: {self.form.name} for relation {self.relation.name}") from re
