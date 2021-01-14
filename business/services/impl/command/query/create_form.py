import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class CreateForm(QueryCommand):

    def __init__(self, form):
        self.form = form

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/form", json.dumps(self.form.__dict__))
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating form: {self.form.name}") from re
