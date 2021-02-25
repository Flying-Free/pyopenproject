from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import DeleteRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import MembershipCommand


class Delete(MembershipCommand):

    def __init__(self, connection, membership):
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.membership.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting membership by id: {self.membership.id}") from re
