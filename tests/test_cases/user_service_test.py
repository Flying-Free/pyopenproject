import json

from model.user import User
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.usrSer = self.factory.get_user_service()
        with open('../data/user.json') as f:
            self.user = User(json.load(f))

    def test_find_all(self):
        # Order by status doesnt work
        usservs = self.usrSer.find_all(1, 25, ' [{ "status": { "operator": "=", "values": ["invited"] } }, '
                                               '{ "name": { "operator": "=", "values": '
                                               '["OpenProject Admin"] } }]', '[["id", "asc"]]')
        self.assertEqual(0, len(usservs))
        usservs = self.usrSer.find_all(1, 25, ' [{ "status": { "operator": "=", "values": ["active"] } }, '
                                              '{ "name": { "operator": "=", "values": '
                                              '["OpenProject Admin"] } }]', '[["id", "asc"]]')
        self.assertEqual(1, len(usservs))

    def test_find(self):
        self.assertIsNotNone(self.usrSer.find(self.user))

    def test_lock_user(self):
        self.assertIsNotNone(self.usrSer.lock_user(self.user))

    def test_unlock_user(self):
        self.assertIsNotNone(self.usrSer.unlock_user(self.user))

    def test_update_user(self):
        self.assertIsNotNone(self.usrSer.update_user(self.user))

    def test_delete_user(self):
        self.assertIsNotNone(self.usrSer.delete_user(self.user))

    def test_create_user(self):
        self.assertIsNotNone(self.usrSer.create_user(self.user))
