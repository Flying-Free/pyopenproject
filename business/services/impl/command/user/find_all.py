from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand
from model.user import User


class FindAll(UserCommand):

    def __init__(self, connection, offset, pageSize, filters, sortBy):
        super(connection)
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}")\
                .execute()
            for tEntry in json_obj._embedded.elements:
                yield User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all users by context: {self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}") from re
