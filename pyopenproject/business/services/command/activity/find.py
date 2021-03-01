from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.activity.activity_command import ActivityCommand
from pyopenproject.model import activity as act


class Find(ActivityCommand):

    def __init__(self, connection, activity):
        """Constructor for class Find, from ActivityCommand

        :param connection: The connection data
        :param activity: The activity to find
        """
        super().__init__(connection)
        self.activity = activity

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.activity.id}").execute()
            return act.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by id: {self.activity.id}")from re
