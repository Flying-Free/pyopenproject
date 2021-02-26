from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.custom_action.custom_action_command import CustomActionCommand
from pyopenproject.model.custom_action import CustomAction


class Execute(CustomActionCommand):

    def __init__(self, connection, custom_action):
        """Constructor for class Execute, from CustomActionCommand.

        :param connection: The connection data
        :param custom_action: The custom action to execute
        """
        super().__init__(connection)
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.custom_action.__dict__['_links']['self']['href']}/execute",
                                   json=self.custom_action.__dict__).execute()
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error executing custom_action:"
                                f" {self.custom_action.__dict__['_links']['self']['href']}/execute") from re
