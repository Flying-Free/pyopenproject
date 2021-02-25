from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.priority.priority_command import PriorityCommand
from model.priority import Priority
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


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
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               URLParameter("offset", self.offset),
                                                               URLParameter("pageSize", self.page_size),
                                                               Filters("filters", self.filters),
                                                               URLParameter("sortBy", self.sort_by)
                                                           ]))).execute()

            for priority in json_obj["_embedded"]["elements"]:
                yield Priority(priority)
        except RequestError as re:
            raise BusinessError("Error finding all priorities") from re
