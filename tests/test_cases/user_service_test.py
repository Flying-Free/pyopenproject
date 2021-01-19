import json

from model.user import User
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.usrSer = self.factory.get_user_service()
        with open('../data/user.json') as f:
            self.user = User(json.load(f))

    def find_all(self):
        self.assertIsNotNone(self.usrSer.find_all(25, 25, ' [{ "status": { "operator": "=", "values": ["invited"] } }, '
                                                          '{ "group": { "operator": "=", "values": ["1"] } }, '
                                                          '{ "name": { "operator": "=", "values": '
                                                          '["h.wurst@openproject.com"] } }]', '[["status", "asc"]]'))

    def find(self):
        self.assertIsNotNone(self.usrSer.find(self.user))

    def lock_user(self):
        self.assertIsNotNone(self.usrSer.lock_user(self.user))

    def unlock_user(self):
        self.assertIsNotNone(self.usrSer.unlock_user(self.user))

    def update_user(self):
        self.assertIsNotNone(self.usrSer.update_user(self.user))

    def delete_user(self):
        self.assertIsNotNone(self.usrSer.delete_user(self.user))

    def create_user(self):
        self.assertIsNotNone(self.usrSer.create_user(self.user))
