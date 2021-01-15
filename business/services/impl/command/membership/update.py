import json
from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership

class Update(MembershipCommand):

    def __init__(self, membership):
        self.membership = membership

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.membership.id}", json.dumps(self.membership.__dict__))
            return Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating membership by id: {self.membership.id}") from re
