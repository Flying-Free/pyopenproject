from openproject.business.services.command.user_preferences.find import Find
from openproject.business.services.command.user_preferences.update import Update
from openproject.business.user_preferences_service import UserPreferencesService


class UserPreferencesServiceImpl(UserPreferencesService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self):
        return Find(self.connection).execute()

    def update(self, user_preferences):
        return Update(self.connection, user_preferences).execute()
