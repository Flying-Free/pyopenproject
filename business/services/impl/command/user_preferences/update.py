import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user_preferences.user_preferences_command import UserPreferencesCommand
from model.user_preferences import UserPreferences


class Update(UserPreferencesCommand):

    def __init__(self, connection, userPreferences):
super().__init__(connection)        self.userPreferences = userPreferences

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}",
                                    json=json.dumps(self.userPreferences.__dict__)).execute()
            return UserPreferences(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user preferences") from re
