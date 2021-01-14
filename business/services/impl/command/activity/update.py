import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand
from model.activity import Activity


class Update(ActivityCommand):

    def __init__(self, activity):
        self.activity = activity

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}/{self.activity.id}", json.dumps(self.activity.__dict__))
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating activity: {self.activity.id}") from re
