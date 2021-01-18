from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.custom_action.custom_action_command import CustomActionCommand
from model.custom_action import CustomAction


class Find(CustomActionCommand):

    def __init__(self, connection, custom_action):
        super().__init__(connection)
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, self.custom_action._links["self"]["href"]).execute()
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding custom_action: {self.custom_action._links['self']['href']}") from re
