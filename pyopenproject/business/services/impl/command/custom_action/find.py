from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import CustomActionCommand
from pyopenproject.model.custom_action import CustomAction


class Find(CustomActionCommand):

    def __init__(self, connection, custom_action):
        """Constructor for class Find, from CustomActionCommand.

        :param connection: The connection data
        :param custom_action: The custom action to find
        """
        super().__init__(connection)
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, self.custom_action.__dict__['_links']["self"]["href"]).execute()
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding custom_action: "
                                f"{self.custom_action.__dict__['_links']['self']['href']}") from re
