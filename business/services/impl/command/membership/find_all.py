import model.membership as mem
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand


class FindAll(MembershipCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.filters}").execute()
            for membership in json_obj['_embedded']['elements']:
                yield mem.Membership(membership)
        except RequestError as re:
            raise BusinessError(f"Error finding all memberships") from re
