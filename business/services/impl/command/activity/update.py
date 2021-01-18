import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand
from model.activity import Activity


class Update(ActivityCommand):

    def __init__(self, connection, activity):
        super(connection)
        self.activity = activity

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.activity.id}",
                                    json=json.dumps(self.activity.__dict__)).execute()
            return Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating activity: {self.activity.id}") from re
