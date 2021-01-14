from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand
from model.activity import Activity


class FindByContext(ActivityCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by context: {self.context}") from re

