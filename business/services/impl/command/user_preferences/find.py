from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user_preferences.user_preferences_command import UserPreferencesCommand
from model.user_preferences import UserPreferences


class Find(UserPreferencesCommand):

    def __init__(self, connection):
        super(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return UserPreferences(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding user preferences") from re
