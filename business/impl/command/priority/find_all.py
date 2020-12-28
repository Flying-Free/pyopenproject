from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.priority.priority_command import PriorityCommand
from model.priority import Priority


class FindAll(PriorityCommand):

    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for priority in json_obj._embedded.elements:
                yield Priority(priority)
        except RequestError as re:
            raise BusinessError(f"Error finding all priorities") from re
