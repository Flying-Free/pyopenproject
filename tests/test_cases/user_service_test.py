import json
import os

from business.exception.business_error import BusinessError
from model.user import User
from tests.test_cases.openproject_test_case import OpenProjectTestCase
from util.Filter import Filter


class UserServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        USER = os.path.join(self.TEST_CASES, '../data/user.json')
        USER_INPUT = os.path.join(self.TEST_CASES, '../data/inputs/user.json')
        self.usrSer = self.factory.get_user_service()
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
        self.assertEqual(1, len(users))

    def test_find(self):
        expected = self.usrSer.find(self.user)
        self.assertEqual(self.user.name, expected.name)

    def test_not_found(self):
        user = User({"id": 50})
        # Result is 404
        with self.assertRaises(BusinessError):
            e = self.usrSer.find(user)

    def test_invite_user(self):
        user = self.usrSer.invite(
            email="h.wurst@openproject.com",
            first_name="Hanz"
        )
        self.assertEqual("h.wurst@openproject.com", user.email)
        self.assertEqual("Hanz", user.firstName)
        #  FIXME:
        #   {
        #   "_type":"Error",
        #   "errorIdentifier":"urn:openproject-org:api:v3:errors:MissingPermission",
        #   "message":"You are not authorized to access this resource."
        #   }
        self.usrSer.delete(user)

    # FIXME:
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
    #  "message":"An internal error has occured.
    #  undefined method `identity_url=' for #<API::V3::Users::UserRepresenter:0x00005642a7e34190>"
    #  }
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
        user.email = "h.wut@openproject.com"
        user_update = self.usrSer.update(user)
        self.assertEqual(user_update.email, "h.wut@openproject.com")
        self.assertEqual(user, self.usrSer.lock(user))
        # Unlock
        self.assertEqual(user, self.usrSer.unlock(user))
        # Delete
        self.usrSer.delete(user)
