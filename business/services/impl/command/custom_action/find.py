from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.custom_action.custom_action_command import CustomActionCommand
from model.custom_action import CustomAction


class Find(CustomActionCommand):

    def __init__(self, custom_action):
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.custom_action.id}")
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding custom_action by id: {self.custom_action.id}") from re
