import json
import os

from model.membership import Membership
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class MembershipServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/membership.json')
        TO_CREATE = os.path.join(self.TEST_CASES, '../data/inputs/membership.json')
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
    def test_update(self):
        self.assertIsNotNone(self.membershipSer.update(self.membership))

    # FIXME: 'Form' object has no attribute 'id'
    def test_operations(self):
        form=self.membershipSer.create_form(self.membership_form)
        self.assertIsNotNone(form)
        form._embedded['payload']['_links']['principal'] =  {'href': '/api/v3/users/1'}
        self.assertIsNotNone(self.membershipSer.update_form(form))
        membership = self.membershipSer.create(self.membership_to_create)
        membership = self.membershipSer.find(membership)
        self.assertIsNotNone(membership)
        self.assertIsNotNone(self.membershipSer.delete(membership))
        membership = self.membershipSer.find(membership)
        self.assertIsNone(membership)

    # FIXME
    #  {
    #  "_type":"Error",
    #  "errorIdentifier":"urn:openproject-org:api:v3:errors:BadRequest",
    #  "message":"Bad request: id is invalid"
    #  }
    def test_membership_schema(self):
        schema = self.membershipSer.membership_schema()
        print(schema)

    def test_available_projects(self):
        available_projects = self.membershipSer.available_projects()
        self.assertEqual(2, len(available_projects))
        m = list(filter(lambda x: x["identifier"] in list(map(lambda y: y.identifier, available_projects)),
                        self.membership_available_projects))
        self.assertEqual(1, len(m))


