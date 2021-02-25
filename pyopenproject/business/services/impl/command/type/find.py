from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TypeCommand
from pyopenproject.model import Type


class Find(TypeCommand):

    def __init__(self, connection, project_type):
        super().__init__(connection)
        self.project_type = project_type

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project_type.id}").execute()
            return Type(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding type by ID: {self.project_type.id}") from re
