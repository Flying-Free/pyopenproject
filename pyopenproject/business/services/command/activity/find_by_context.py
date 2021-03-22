from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.activity.activity_command import ActivityCommand
from pyopenproject.model import activity as act


class FindByContext(ActivityCommand):

    def __init__(self, connection, context):
        """Constructor for class FindByContext, from ActivityCommand

        :param connection: The connection data
        :param context: The context of the URL we need to search for
        """
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, self.context).execute()
            if json_obj["_type"] == "Activity::Comment":
                return act.Activity(json_obj)
            elif json_obj["_type"] == "Error":
                raise BusinessError(f"Error finding activity by context {self.context}: \n"
                                    f"\tError Identifier: {json_obj['errorIdentifier']}\n"
                                    f"\tMessage: {json_obj['message']}")
        except RequestError as re:
            raise BusinessError(f"Error finding activity by context: {self.context}") from re
