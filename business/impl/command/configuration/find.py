from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.configuration.configuration_command import ConfigurationCommand
from model.configuration import Configuration


class Find(ConfigurationCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            return Configuration(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error listing configuration") from re
