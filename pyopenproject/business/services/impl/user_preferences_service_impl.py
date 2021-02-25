from pyopenproject.business import UserPreferencesService
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import Update


class UserPreferencesServiceImpl(UserPreferencesService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self):
        return Find(self.connection).execute()

    def update(self, user_preferences):
        return Update(self.connection, user_preferences).execute()
