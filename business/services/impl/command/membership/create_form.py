import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.form import Form


class CreateForm(MembershipCommand):

    def __init__(self, membership):
        self.membership = membership

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/form", json.dumps(self.membership.__dict__))
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating membership") from re