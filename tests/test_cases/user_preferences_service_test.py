import json
import os

from model.user_preferences import UserPreferences
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserPreferencesServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/user_preferences.json')
        self.userPrefSer = self.factory.get_user_preferences_service()
        with open(DATA) as f:
            self.user_preferences = UserPreferences(json.load(f))

    def find(self):
        self.assertIsNotNone(self.userPrefSer.find())

    def update(self):
        self.assertIsNotNone(self.userPrefSer.update(self.user_preferences))
