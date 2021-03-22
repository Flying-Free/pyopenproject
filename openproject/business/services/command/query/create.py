from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.post_request import PostRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.query.query_command import QueryCommand
from openproject.model.query import Query


class Create(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.query.__dict__).execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating query: {self.query}") from re
