import json

from model.user import User
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class UserServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.usrSer = self.factory.get_user_service()
        with open('../data/user.json') as f:
            self.user = User(json.load(f))
        with open('../data/inputs/user.json') as f:
            self.new_user = User(json.load(f))

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

    def test_operations_user(self):
        # Create FIXME: ERROR  {"_type":"Error","errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError","message":"An internal error has occured. undefined method `fetch' for #<String:0x0000556bedbebb68>"}
        nwusr=self.usrSer.create_user(self.new_user)
        self.assertIsNotNone(nwusr)
        self.assertEqual(self.new_user.login, nwusr.login)
        # Update
        nwusr.email="h.wut@openproject.com"
        self.assertEqual(nwusr, self.usrSer.update_user(nwusr))
        # Lock
        self.assertEqual(nwusr, self.usrSer.lock_user(nwusr))
        # Unlock
        self.assertEqual(nwusr, self.usrSer.unlock_user(nwusr))
        # Delete
        self.assertIsNone(self.usrSer.delete_user(nwusr))




