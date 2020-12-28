from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership


class Find(MembershipCommand):

    def __init__(self, help_text):
        self.help_text = help_text

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.membership.id}")
            return Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding membership by id: {self.membership.id}") from re