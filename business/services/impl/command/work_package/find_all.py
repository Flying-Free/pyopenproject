import model.work_package as wp
from business.services.impl.command.abstract_find_all import AbstractFindAll
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindAll(AbstractFindAll):
    def __init__(self, connection, offset, page_size, filters, sort_by, group_by, show_sums):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by
        self.group_by = group_by
        self.show_sums = show_sums

    def cast(self, endpoint):
        return wp.WorkPackage(endpoint)

    def request_url(self):
        return str(URL(f"{self.CONTEXT}", [
            URLParameter("offset", self.offset),
            URLParameter("pageSize", self.page_size),
            Filters("filters", self.filters),
            URLParameter("sortBy", self.sort_by),
            URLParameter("groupBy", self.group_by),
            URLParameter("showSums", self.show_sums)
        ]))
