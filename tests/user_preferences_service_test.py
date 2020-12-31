import unittest

from business.user_preferences_service import UserPreferencesService


class UserPreferencesServiceTestCase(unittest.TestCase):
    userPrefSer = UserPreferencesService()

    def type_request(self):
        self.assertNotNull(self.userPrefSer.request(1))
