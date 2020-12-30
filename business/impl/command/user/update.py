import json
from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.user.user_command import UserCommand
from model.user import User


class Update(UserCommand):

    def __init__(self, user):
        self.user = user

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.user.id}", json.dumps(self.user.__dict__))
            return User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user by id: {self.user.id}") from re
