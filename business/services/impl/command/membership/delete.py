from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand

class Delete(MembershipCommand):

    def __init__(self, membership):
        self.membership = membership

    def execute(self):
        try:
            Connection().delete(f"{self.CONTEXT}/{self.membership.id}")
        except RequestError as re:
            raise BusinessError(f"Error deleting membership by id: {self.membership.id}") from re
