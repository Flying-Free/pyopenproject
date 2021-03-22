from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.priority.priority_command import PriorityCommand
from openproject.model.priority import Priority


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
