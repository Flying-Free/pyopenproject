from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.user.user_command import UserCommand
from model.user import User


class FindByContext(UserCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding user by context: {self.context}") from re
