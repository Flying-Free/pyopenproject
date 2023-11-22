from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.notification.notification_command import NotificationCommand
from pyopenproject.model.notification import Notification
import json


class Read(NotificationCommand):

    def __init__(self, connection, notification_id):
        super().__init__(connection)
        self.notification_id = notification_id

    def execute(self):
        try:
            response = PostRequest(connection=self.connection,
                                   headers={
                                       "Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.notification_id}/read_ian").execute()
            return response
        except RequestError as re:
            raise BusinessError(
                f"Error reading notification: {re.args}")
