from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.query.query_command import QueryCommand
from pyopenproject.model.query import Query


class FindByContext(QueryCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            if json_obj["_type"] == "query::Comment":
                return Query(json_obj)
            elif json_obj["_type"] == "Error":
                raise BusinessError(f"Error finding query by context {self.context}: \n"
                                    f"\tError Identifier: {json_obj['errorIdentifier']}\n"
                                    f"\tMessage: {json_obj['message']}")
        except RequestError as re:
            raise BusinessError(f"Error finding query by context: {self.context}") from re

