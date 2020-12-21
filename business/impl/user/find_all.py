import json

from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.user.user_command import UserCommand
from src.extract.model.user import User


class FindAll(UserCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for tEntry in json_obj._embedded.elements:
                yield User(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all users by context: {self.CONTEXT}") from re
