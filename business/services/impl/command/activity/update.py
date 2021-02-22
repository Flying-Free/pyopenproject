import json

import model.activity as act
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand


class Update(ActivityCommand):

    def __init__(self, connection, activity):
        """
        Constructor for class Update, from ActivityCommand

        :param connection: The connection data
        :param activity: The activity we want to update
        """
        super().__init__(connection)
        self.activity = activity

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.activity.id}",
                                    json=json.dumps(self.activity.__dict__)).execute()
            return act.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating activity: {self.activity.id}") from re
