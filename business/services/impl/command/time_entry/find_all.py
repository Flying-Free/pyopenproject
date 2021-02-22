import model.time_entry as te
from business.services.impl.command.abstract_find_all import AbstractFindAll
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindAll(AbstractFindAll):

    def __init__(self, connection, offset, page_size, filters, sort_by):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by

    def cast(self, endpoint):
        return te.TimeEntry(endpoint)

    def request_url(self):
        return str(URL(f"{self.CONTEXT}", [
            URLParameter("offset", self.offset),
            URLParameter("pageSize", self.page_size),
            Filters("filters", self.filters),
            URLParameter("sortBy", self.sort_by)
        ]))
