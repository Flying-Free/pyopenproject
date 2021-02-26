import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.util.filter import Filter
from pyopenproject.model.user import User
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        USER = os.path.join(self.TEST_CASES, '../data/user.json')
        USER_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/user.json')
        self.usrSer = self.op.get_user_service()
        with open(USER) as f:
            self.user = User(json.load(f))
        with open(USER_INPUT) as f:
            self.new_user = User(json.load(f))

    def test_find_all(self):
        # Order by status doesnt work
        users = self.usrSer.find_all(1, 25,
                                     [
                                         Filter("status", "=", ["invited"]),
                                         Filter("name", "=", ["OpenProject Admin"])
                                     ],
                                     '[["id", "asc"]]')
        self.assertEqual(0, len(users))
        users = self.usrSer.find_all(1, 25,
                                     [
                                         Filter("status", "=", ["active"]),
                                         Filter("name", "=", ["OpenProject Admin"])],
                                     '[["id", "asc"]]')
        self.assertEqual(1, len(users))
        for user in users:
            self.assertEqual("active", user.status)
            self.assertEqual("OpenProject Admin", user.name)
        users = self.usrSer.find_all()
        self.assertEqual(2, len(users))

    def test_find(self):
        expected = self.usrSer.find(self.user)
        self.assertEqual(self.user.name, expected.name)

    def test_not_found(self):
        user = User({"id": 50})
        # Result is 404
        with self.assertRaises(BusinessError):
            self.usrSer.find(user)

    def test_invite_user(self):
        user = self.usrSer.invite(
            email="example@openproject.com",
            first_name="Example"
        )
        self.assertEqual("example@openproject.com", user.email)
        self.assertEqual("Example", user.firstName)
        new_usr = self.usrSer.find(user)
        self.assertEqual(new_usr.email, user.email)
        self.assertEqual(new_usr.firstName, user.firstName)
        self.assertEqual('invited', new_usr.status)
        self.assertEqual(user.status, new_usr.status)
        # FIXME: Delete User
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
        #  "message":"You are not authorized to access this resource."
        #  }
        # self.usrSer.delete(new_usr)

    def test_operations_user(self):
        # Create
        user = self.usrSer.create(
            login="h.wurst",
            email="h.wurst@openproject.com",
            first_name="Hans",
            last_name="Wurst",
            admin=False,
            language="de",
            status="active",
            # Password minimum is 10 characters)
            password="h.wurst1234567890"
        )
        self.assertIsNotNone(user)
        self.assertEqual("h.wurst", user.login)
        # Update
        self.usrSer.unlock(user)
        user = self.usrSer.find(user)
        user.email = "h.wut@openproject.com"
        user_update = self.usrSer.update(user)
        user_update = self.usrSer.find(user_update)
        self.assertEqual(user.email, user_update.email)
        # Lock
        self.usrSer.lock(user_update)
        user_update = self.usrSer.find(user_update)
        self.assertEqual('locked', user_update.status)
        # Unlock
        self.usrSer.unlock(user_update)
        user = self.usrSer.find(user_update)
        self.assertNotEqual(user.status, user_update.status)
        # FIXME: Delete User
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
        #  "message":"You are not authorized to access this resource."
        #  }
        # self.usrSer.delete(user)
