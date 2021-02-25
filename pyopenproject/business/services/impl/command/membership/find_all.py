from pyopenproject import model as mem
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import MembershipCommand
from pyopenproject.business.util import Filters
from pyopenproject.business.util import URL


class FindAll(MembershipCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               Filters("filters", self.filters)
                                                           ]))).execute()
            for membership in json_obj['_embedded']['elements']:
                yield mem.Membership(membership)
        except RequestError as re:
            raise BusinessError("Error finding all memberships") from re
