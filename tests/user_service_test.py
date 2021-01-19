import json
import unittest

from business.services.user_service import UserService
from model.user import User


class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.usrSer = UserService()
        with open('./data/user.json') as f:
            self.user = User(json.load(f))

    def find_all(self):
        self.assertNotNull(self.usrSer.find_all(25, 25, ' [{ "status": { "operator": "=", "values": ["invited"] } }, '
                                                        '{ "group": { "operator": "=", "values": ["1"] } }, '
                                                        '{ "name": { "operator": "=", "values": '
                                                        '["h.wurst@openproject.com"] } }]', '[["status", "asc"]]'))

    def find(self):
        self.assertNotNull(self.usrSer.find(self.user))

    def lock_user(self):
        self.assertNotNull(self.usrSer.lock_user(self.user))

    def unlock_user(self):
        self.assertNotNull(self.usrSer.unlock_user(self.user))

    def update_user(self):
        self.assertNotNull(self.usrSer.update_user(self.user))

    def delete_user(self):
        self.assertNotNull(self.usrSer.delete_user(self.user))

    def create_user(self):
        self.assertNotNull(self.usrSer.create_user(self.user))
