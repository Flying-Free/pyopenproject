from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.priority.priority_command import PriorityCommand
from model.priority import Priority


class FindAll(PriorityCommand):

    def __init__(self, connection, filters):
        super(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for priority in json_obj._embedded.elements:
                yield Priority(priority)
        except RequestError as re:
            raise BusinessError(f"Error finding all priorities") from re
