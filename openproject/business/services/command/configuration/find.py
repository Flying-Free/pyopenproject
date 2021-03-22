from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.configuration.configuration_command import ConfigurationCommand
from openproject.model.configuration import Configuration


class Find(ConfigurationCommand):

    def __init__(self, connection):
        """Constructor for class Find, from ConfigurationCommand.

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Configuration(json_obj)
        except RequestError as re:
            raise BusinessError("Error listing configuration") from re
