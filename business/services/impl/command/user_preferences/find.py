from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.user_preferences.user_preferences_command import UserPreferencesCommand
from model.user_preferences import UserPreferences


class Find(UserPreferencesCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            return UserPreferences(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding user preferences") from re
