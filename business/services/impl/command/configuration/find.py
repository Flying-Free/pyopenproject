from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.configuration.configuration_command import ConfigurationCommand
from model.configuration import Configuration


class Find(ConfigurationCommand):

    def __init__(self, connection):
                super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Configuration(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error listing configuration") from re
