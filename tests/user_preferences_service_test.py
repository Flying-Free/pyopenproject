import unittest

from business.user_preferences_service import UserPreferencesService


class UserPreferencesServiceTestCase(unittest.TestCase):
    userPrefSer = UserPreferencesService()

    def find(self):
        self.assertNotNull(self.userPrefSer.find())

    def update(self):
        self.assertNotNull(self.userPrefSer.update(user_preferences))
