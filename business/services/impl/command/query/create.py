import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Create(QueryCommand):

    def __init__(self, connection, query):
        super(connection)
        self.query = query

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}",
                                   json=json.dumps(self.query.__dict__)).execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating query: {self.query}") from re
