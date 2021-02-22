import model.relation as rel
from business.services.impl.command.abstract_find_all import AbstractFindAll
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class FindAll(AbstractFindAll):

    def __init__(self, connection, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def cast(self, endpoint):
        return rel.Relation(endpoint)

    def request_url(self):
        return str(URL(f"{self.CONTEXT}", [
            Filters("filters", self.filters),
            URLParameter("sortBy", self.sort_by)
        ]))
