from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership


class Find(MembershipCommand):

    def __init__(self, connection, membership):
        super(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.membership.id}").execute()
            return Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding membership by id: {self.membership.id}") from re
