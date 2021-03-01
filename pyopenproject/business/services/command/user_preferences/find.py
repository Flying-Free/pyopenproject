from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.user_preferences.user_preferences_command import UserPreferencesCommand
from pyopenproject.model.user_preferences import UserPreferences


class Find(UserPreferencesCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return UserPreferences(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding user preferences") from re
