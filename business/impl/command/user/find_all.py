from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.user.user_command import UserCommand
from model.user import User


class FindAll(UserCommand):

    def __init__(self, offset, pageSize, filters, sortBy):
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}")
            for tEntry in json_obj._embedded.elements:
                yield User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all users by context: {self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}") from re
