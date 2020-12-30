from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.membership.membership_command import MembershipCommand
from model.schema import Schema


class FindSchema(MembershipCommand):

    def __init__(self, help_text):
        self.help_text = help_text

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schemas")
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding the membership schema") from re