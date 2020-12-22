from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.activity.activity_command import ActivityCommand
from model.activity import Activity


class FindById(ActivityCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.identifier}")
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding project by id: {self.identifier}") from re
