from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.custom_action.custom_action_command import CustomActionCommand
from model.custom_action import CustomAction


class Find(CustomActionCommand):

    def __init__(self, custom_action):
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = Connection().get(self.custom_action._links["self"]["href"])
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding custom_action: {self.custom_action._links['self']['href']}") from re
