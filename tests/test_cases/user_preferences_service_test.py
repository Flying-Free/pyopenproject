import json
import os

from pyopenproject.model.user_preferences import UserPreferences
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserPreferencesServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/user_preferences.json')
        self.userPrefSer = self.op.get_user_preferences_service()
        with open(DATA) as f:
            self.user_preferences = UserPreferences(json.load(f))

    def test_find(self):
        user_preferences = self.userPrefSer.find()
        self.assertEqual(self.user_preferences.__dict__, user_preferences.__dict__)

    # FIXME: We need an application user to update its preferences
    #  Actual user => {'href': '/api/v3/users/3', 'title': 'System'}
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:Unauthenticated",
    #  "message":"You need to be authenticated to access this resource."
    #  }
    def test_update(self):
        user_preferences = self.userPrefSer.find()
        user_preferences.timeZone = "Europe/London"
        user_preferences.hideMail = False
        # updated_user_preferences = self.userPrefSer.update(user_preferences)
        # self.assertEqual(user_preferences.timeZone, updated_user_preferences.timeZone)
        # self.assertEqual(user_preferences.hideMail, updated_user_preferences.hideMail)
        # updated_user_preferences = self.userPrefSer.update(self.user_preferences)
        # self.assertNotEqual(user_preferences.timeZone, updated_user_preferences.timeZone)
        # self.assertNotEqual(user_preferences.hideMail, updated_user_preferences.hideMail)
