from pyopenproject import model as v
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import VersionCommand
from pyopenproject.business.util import Filters
from pyopenproject.business.util import URL


class FindAll(VersionCommand):
    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters("filters", self.filters)
                                                           ]))).execute()

            for version in json_obj["_embedded"]["elements"]:
                yield v.Version(version)
        except RequestError as re:
            raise BusinessError(f"Error finding all versions by filters: {self.filters}") from re
