import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.custom_action.custom_action_command import CustomActionCommand
from model.custom_action import CustomAction


class Execute(CustomActionCommand):

    def __init__(self, custom_action):
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/{self.custom_action.id}/execute", json.dumps(self.custom_action.__dict__))
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error executing custom_action: {self.custom_action.id}") from re
