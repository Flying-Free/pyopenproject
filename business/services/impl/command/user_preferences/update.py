from contextlib import suppress

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user_preferences.user_preferences_command import UserPreferencesCommand
from model.user_preferences import UserPreferences


class Update(UserPreferencesCommand):

    def __init__(self, connection, user_preferences):
        super().__init__(connection)
        self.userPreferences = user_preferences

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}",
                                    json=self.userPreferences.__dict__).execute()
            return UserPreferences(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user preferences") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.userPreferences.__dict__["_links"]
        with suppress(KeyError): del self.userPreferences.__dict__["_type"]
