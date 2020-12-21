import unittest

from business.user_service import UserService


class UserServiceTestCase(unittest.TestCase):
    usrSer = UserService()


def user_request(self):
    self.assertNotNull(self.usrSer.find_by_id(1))
