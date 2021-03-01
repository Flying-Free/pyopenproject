from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.membership.membership_command import MembershipCommand
from pyopenproject.model import membership as mem


class Find(MembershipCommand):

    def __init__(self, connection, membership):
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.membership.id}").execute()
            return mem.Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding membership by id: {self.membership.id}") from re
