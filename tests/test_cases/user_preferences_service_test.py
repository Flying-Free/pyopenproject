import json

from model.user_preferences import UserPreferences
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserPreferencesServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.userPrefSer = self.factory.get_user_preferences_service()
        with open('../data/user_preferences.json') as f:
            self.user_preferences = UserPreferences(json.load(f))

    def find(self):
        self.assertIsNotNone(self.userPrefSer.find())

    def update(self):
        self.assertIsNotNone(self.userPrefSer.update(self.user_preferences))
