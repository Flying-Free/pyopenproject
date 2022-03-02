import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.membership import Membership
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class MembershipServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/membership.json')
        TO_CREATE = os.path.join(self.TEST_CASES, '../data/inputs/membership.json')
        FORM = os.path.join(self.TEST_CASES, '../data/membership-form.json')
        AVAILABLE_PROJECTS = os.path.join(self.TEST_CASES, '../data/memberships-available-projects.json')
        self.membershipSer = self.op.get_membership_service()
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
        user = self.op.get_user_service().create(login="member",
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
        membership_aux = Membership(membership.__dict__.copy())
        updated_form = self.membershipSer.update_form(membership_aux)
        self.assertEqual({'_links': {'roles': [{'href': '/api/v3/roles/5', 'title': 'Reader'}]}},
                         updated_form._embedded['payload'])
        membership = self.membershipSer.find(membership)
        self.assertIsNotNone(membership)
        membership.__dict__['_links']['project'] = {"href": projects[0].__dict__["_links"]["self"]["href"]}
        membership.__dict__['_links']['roles'] = [{"href": '/api/v3/roles/4'}]
        updated_membership = self.membershipSer.update(membership)
        self.assertEqual(
            membership.__dict__['_embedded']['project'],
            updated_membership.__dict__['_embedded']['project'])
        self.assertEqual(
            membership.__dict__['_embedded']['roles'],
            updated_membership.__dict__['_embedded']['roles'])
        self.membershipSer.delete(updated_membership)
        with self.assertRaises(BusinessError):
            self.membershipSer.find(updated_membership)

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
