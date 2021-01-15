from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand
from model.activity import Activity


class Find(ActivityCommand):

    def __init__(self, activity):
        self.activity = activity

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.activity.id}")
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by id: {self.activity.id}") from re
