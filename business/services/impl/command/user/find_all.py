import model.user as usr
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class FindAll(UserCommand):

    def __init__(self, connection, offset, page_size, filters, sort_by):
        super().__init__(connection)
        self.offset = offset
        self.extended_context = ""
        if page_size:
            self.extended_context += f"&pageSize={page_size}"
        if filters:
            self.extended_context += f"&filters={filters}"
        if sort_by:
            self.extended_context += f"&sort_by={sort_by}"

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}?offset={self.offset}"
                                  f"{self.extended_context}").execute()
            for user in json_obj["_embedded"]["elements"]:
                yield usr.User(user)
        except RequestError as re:
            raise BusinessError(f"Error finding all users: {self.CONTEXT}?offset={self.offset}"
                                f"{self.extended_context}") from re
