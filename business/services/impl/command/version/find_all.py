import model.version as v
from business.services.impl.command.abstract_find_all import AbstractFindAll
from util.Filters import Filters
from util.URL import URL


class FindAll(AbstractFindAll):
    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def cast(self, endpoint):
        return v.Version(endpoint)

    def request_url(self):
        return str(URL(f"{self.CONTEXT}", [
            Filters("filters", self.filters)
        ]))
