import json
import unittest

from business.services.user_preferences_service import UserPreferencesService
from model.user_preferences import UserPreferences


class UserPreferencesServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.userPrefSer = UserPreferencesService()
        with open('../data/user_preferences.json') as f:
            self.user_preferences = UserPreferences(json.load(f))

    def find(self):
        self.assertNotNull(self.userPrefSer.find())

    def update(self):
        self.assertNotNull(self.userPrefSer.update(self.user_preferences))
