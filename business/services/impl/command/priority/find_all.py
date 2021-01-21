from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.priority.priority_command import PriorityCommand
from model.priority import Priority


class FindAll(PriorityCommand):

    def __init__(self, connection, offset, page_size, filters, sort_by):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}?{self.offset},{self.page_size},"
                                  f"{self.filters},{self.sort_by}").execute()
            for priority in json_obj["_embedded"]["elements"]:
                yield Priority(priority)
        except RequestError as re:
            raise BusinessError(f"Error finding all priorities") from re
