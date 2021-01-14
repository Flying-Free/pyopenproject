from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.principal.principal_command import PrincipalCommand
from model.principal import Principal


class FindAll(PrincipalCommand):

    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.filters}")
            for principal in json_obj._embedded.elements:
                yield Principal(principal)
        except RequestError as re:
            raise BusinessError(f"Error finding all principals") from re
