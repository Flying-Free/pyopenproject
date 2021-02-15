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

    def test_operations(self):
        # Create form
        form = self.membershipSer.create_form(self.membership_form)
        self.assertIsNotNone(form)
        membership_to_create = Membership(form._embedded['payload'])
        user = self.factory.get_user_service().create(login="member",
                                                      email="member@openproject.com",
                                                      first_name="Member",
                                                      last_name="Member",
                                                      admin=False,
                                                      language="es",
                                                      status="active",
                                                      password="SomePasswordForAMember1234567890")
        projects = self.membershipSer.available_projects()
        membership_to_create.__dict__['_links']['project'] = {"href": projects[-1].__dict__["_links"]["self"]["href"]}
        membership_to_create.__dict__['_links']['principal'] = {'href': user.__dict__["_links"]["self"]["href"]}
        membership_to_create.__dict__['_links']['roles'] = [{"href": '/api/v3/roles/5'}]
        membership = self.membershipSer.create(membership_to_create)
        self.assertEqual(
            membership.__dict__['_links']['principal']["href"],
            membership_to_create.__dict__['_links']['principal']["href"])
        # FIXME
        #  {
        #  "_type":"Error",
        #  "errorIdentifier":"urn:openproject-org:api:v3:errors:InternalServerError",
        #  "message":"An internal error has occured. 405 Not Allowed"
        #  }
        updated_form = self.membershipSer.update_form(membership)
        membership = self.membershipSer.find(membership)
        updated_membership = self.membershipSer.update(membership)
        self.assertIsNotNone(membership)
        self.assertIsNotNone(self.membershipSer.delete(membership))
        membership = self.membershipSer.find(membership)
        self.assertIsNone(membership)

    def test_membership_schema(self):
        schema = self.membershipSer.membership_schema()
        self.assertIsNotNone(schema)
        self.assertEqual(schema.id['name'], 'ID')

    def test_available_projects(self):
        available_projects = self.membershipSer.available_projects()
        self.assertEqual(2, len(available_projects))
        m = list(filter(lambda x: x["identifier"] in list(map(lambda y: y.identifier, available_projects)),
                        self.membership_available_projects))
        self.assertEqual(1, len(m))
