from pyopenproject import model as wp
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand
from pyopenproject.business.util import Filters
from pyopenproject.business.util import URL
from pyopenproject.business.util import URLParameter


class FindAll(WorkPackageCommand):
    def __init__(self, connection, offset, page_size, filters, sort_by, group_by, show_sums):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by
        self.group_by = group_by
        self.show_sums = show_sums

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               URLParameter("offset", self.offset),
                                                               URLParameter("pageSize", self.page_size),
                                                               Filters("filters", self.filters),
                                                               URLParameter("sortBy", self.sort_by),
                                                               URLParameter("groupBy", self.group_by),
                                                               URLParameter("showSums", self.show_sums)
                                                           ]))).execute()

            for work_package in json_obj["_embedded"]["elements"]:
                yield wp.WorkPackage(work_package)
        except RequestError as re:
            raise BusinessError("Error finding all work packages") from re
