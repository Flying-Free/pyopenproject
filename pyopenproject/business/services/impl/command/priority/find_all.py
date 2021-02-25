from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import PriorityCommand
from pyopenproject.business.util import Filters
from pyopenproject.business.util import URL
from pyopenproject.business.util import URLParameter
from pyopenproject.model import Priority


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
