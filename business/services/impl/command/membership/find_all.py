from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership


class FindAll(MembershipCommand):

    def __init__(self, filters):
        self.filters = filters

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.filters}")
            for membership in json_obj._embedded.elements:
                yield Membership(membership)
        except RequestError as re:
            raise BusinessError(f"Error finding all memberships") from re