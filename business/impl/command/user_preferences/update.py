import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.user_preferences.user_preferences_command import UserPreferencesCommand
from model.user_preferences import UserPreferences


class Update(UserPreferencesCommand):

    def __init__(self, userPreferences):
        self.userPreferences = userPreferences

    def execute(self):
        try:
            json_obj = Connection().patch(f"{self.CONTEXT}", json.dumps(self.userPreferences.__dict__))
            return UserPreferences(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user by id: {self.user.id}") from re
