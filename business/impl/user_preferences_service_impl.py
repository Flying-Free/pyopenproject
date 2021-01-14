from business.impl.command.user_preferences.find import Find
from business.impl.command.user_preferences.update import Update
from business.user_preferences_service import UserPreferencesService


class UserPreferencesServiceImpl(UserPreferencesService):

    def find(self):
        return Find().execute()

    def update(self, user_preferences):
        return Update(user_preferences).execute()