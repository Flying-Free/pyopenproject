import json
import unittest

from business.services.user_preferences_service import UserPreferencesService


class UserPreferencesServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.userPrefSer = UserPreferencesService()
        self.user_preferences = json.loads('/data/user_preferences.json')

    def find(self):
        self.assertNotNull(self.userPrefSer.find())

    def update(self):
        self.assertNotNull(self.userPrefSer.update(self.user_preferences))
