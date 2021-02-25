from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import PriorityCommand
from pyopenproject.model import Priority


class Find(PriorityCommand):

    def __init__(self, connection, priority):
        super().__init__(connection)
        self.priority = priority

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.priority.id}").execute()
            return Priority(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding priority by id: {self.priority.id}") from re
