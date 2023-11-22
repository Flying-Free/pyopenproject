from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.notification.notification_command import NotificationCommand
from pyopenproject.model.notification import Notification


class Find(NotificationCommand):

    def __init__(self, connection, notification_id):
        super().__init__(connection)
        self.notification_id = notification_id

    def execute(self):
        try:
            json_obj = GetRequest(
                self.connection, f"{self.CONTEXT}/{self.notification_id}",).execute()
            return Notification(json_obj)

        except RequestError as re:
            raise BusinessError(
                f"Error finding notifications:{re.args}")
