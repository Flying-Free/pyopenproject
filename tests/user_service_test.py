import json
import unittest

from business.user_service import UserService


class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.usrSer = UserService()
        self.user = json.loads('/data/user.json')

    def find_all(self):
        self.assertNotNull(self.usrSer.find_all(offset, pageSize, filters, sortBy))

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
