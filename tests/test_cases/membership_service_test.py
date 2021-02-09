import json
import os

from model.membership import Membership
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class MembershipServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/membership.json')
        TO_CREATE = os.path.join(self.TEST_CASES, '../data/membership-to-create.json')
        FORM = os.path.join(self.TEST_CASES, '../data/membership-form.json')
        AVAILABLE_PROJECTS = os.path.join(self.TEST_CASES, '../data/memberships-available-projects.json')
        self.membershipSer = self.factory.get_membership_service()
        with open(DATA) as f:
            self.membership = Membership(json.load(f))
        with open(TO_CREATE) as f:
            self.membership_to_create = Membership(json.load(f))
        with open(FORM) as f:
            self.membership_form = Membership(json.load(f))
        with open(AVAILABLE_PROJECTS) as f:
            self.membership_available_projects = json.load(f)

    def test_find_all(self):
        memberships = self.membershipSer.find_all()
        self.assertEqual(2, len(memberships))

    def test_find(self):
        membership = self.membershipSer.find(self.membership)
        self.assertEqual(
            self.membership.__dict__["_links"]["self"]["title"],
            membership.__dict__["_links"]["self"]["title"])

    # TODO
    # def test_update(self):
    #     self.assertIsNotNone(self.membershipSer.update(self.membership))

    # TODO
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
    #  "message":"An internal error has occured. undefined method `fetch' for #<String:0x000055a4180c0758>"
    #  }
    # def test_delete(self):
    #     membership = self.membershipSer.create(self.membership_to_create)
    #     membership = self.membershipSer.find(membership)
    #     self.assertIsNotNone(membership)
    #     self.assertIsNotNone(self.membershipSer.delete(membership))
    #     membership = self.membershipSer.find(membership)
    #     self.assertIsNone(membership)

    # FIXME
    # def test_create(self):
    #     m = self.membershipSer.create(self.membership_to_create)
    #     print(m)

    # FIXME
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:BadRequest",
    #  "message":"Bad request: id is invalid"
    #  }
    # def test_membership_schema(self):
    #     schema = self.membershipSer.membership_schema()
    #     print(schema)

    def test_available_projects(self):
        available_projects = self.membershipSer.available_projects()
        self.assertEqual(2, len(available_projects))
        m = filter(lambda x: x.identifier == available_projects[0].identifier, self.membership_available_projects)
        self.assertEqual(1, len(m))

    # FIXME
    #  {
    #  "_type": "Error",
    #  "errorIdentifier": "urn:openproject-org:api:v3:errors:InternalServerError",
    #  "message": "An internal error has occured. undefined method `fetch' for #<String:0x000055a4175e7ef8>"
    #  }
    # def test_create_form(self):
    #     form = self.membershipSer.create_form(self.membership_form)
    #     print(form)

    # TODO: First, we need to solve the creation form request
    # def test_update_form(self):
    #     self.assertIsNotNone(self.membershipSer.update_form(self.membership))
