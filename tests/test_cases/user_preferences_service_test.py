import json

from business.services.user_preferences_service import UserPreferencesService
from model.user_preferences import UserPreferences


class UserPreferencesServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.userPrefSer = UserPreferencesService()
        with open('../data/user_preferences.json') as f:
            self.user_preferences = UserPreferences(json.load(f))

    def find(self):
        self.assertIsNotNone(self.userPrefSer.find())

    def update(self):
        self.assertIsNotNone(self.userPrefSer.update(self.user_preferences))
