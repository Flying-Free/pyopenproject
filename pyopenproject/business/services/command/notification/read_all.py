from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.notification.notification_command import NotificationCommand
from pyopenproject.model.notification import Notification
import json


class ReadAll(NotificationCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = json.dumps([{'filters':filters}])

    def execute(self):
        try:
            response = PostRequest(connection=self.connection,
                                   headers={
                                       "Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/read_ian",
                                   json=self.filters).execute()
            return response
        except RequestError as re:
            raise BusinessError(
                f"Error creating project form: {self.form.name}") from re
