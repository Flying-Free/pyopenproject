from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.activity.activity_command import ActivityCommand
from model.activity import Activity


class Update(ActivityCommand):

    def __init__(self, identifier, body):
        self.identifier = identifier
        self.body = body

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.identifier}", self.body)
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating activity: {self.identifier}") from re
