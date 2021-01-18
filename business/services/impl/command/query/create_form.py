import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class CreateForm(QueryCommand):

    def __init__(self, connection, form):
        super().__init__(connection)
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/form",
                                   json=json.dumps(self.form.__dict__)).execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating form: {self.form.name}") from re
