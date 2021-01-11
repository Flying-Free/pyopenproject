import unittest

from business.user_service import UserService


class UserServiceTestCase(unittest.TestCase):
    usrSer = UserService()

    def find_all(self):
        self.assertNotNull(self.usrSer.find_all(offset, pageSize, filters, sortBy))

    def find(self):
        self.assertNotNull(self.usrSer.find(user))

    def lock_user(self):
        self.assertNotNull(self.usrSer.lock_user(user))

    def unlock_user(self):
        self.assertNotNull(self.usrSer.unlock_user(user))

    def update_user(self, user):
        self.assertNotNull(self.usrSer.update_user(user))

    def delete_user(self, user):
        self.assertNotNull(self.usrSer.delete_user(user))

    def create_user(self, user):
        self.assertNotNull(self.usrSer.create_user(user))
