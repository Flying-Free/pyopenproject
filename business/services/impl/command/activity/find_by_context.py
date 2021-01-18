from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.activity.activity_command import ActivityCommand
from model.activity import Activity


class FindByContext(ActivityCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            if json_obj["_type"] == "Activity::Comment":
                return Activity(json_obj)
            elif json_obj["_type"] == "Error":
                raise BusinessError(f"Error finding activity by context {self.context}: \n"
                                    f"\tError Identifier: {json_obj['errorIdentifier']}\n"
                                    f"\tMessage: {json_obj['message']}")
        except RequestError as re:
            raise BusinessError(f"Error finding activity by context: {self.context}") from re

