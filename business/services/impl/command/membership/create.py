import json
from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership

class Create(MembershipCommand):

    def __init__(self, membership):
        self.membership = membership

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}", json.dumps(self.membership.__dict__))
            return Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating membership") from re
