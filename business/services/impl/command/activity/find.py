from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand
from model.activity import Activity


class Find(ActivityCommand):

    def __init__(self, connection, activity):
        super().__init__(connection)
        self.activity = activity

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.activity.id}").execute()
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by id: {self.activity.id}") from re
