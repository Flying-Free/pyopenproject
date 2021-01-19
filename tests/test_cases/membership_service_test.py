import json
import unittest

from business.services.membership_service import MembershipService
from model.membership import Membership


class MembershipServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.membershipSer = MembershipService()
        with open('../data/membership.json') as f:
            self.membership = Membership(json.load(f))

    def test_find_all(self):
        self.assertNotNull(self.membershipSer.find_all())
    
    def test_find(self):
        self.assertNotNull(self.membershipSer.find(self.membership))

    def test_update(self):
        self.assertNotNull(self.membershipSer.update(self.membership))
    
    def test_delete(self):
        self.assertNotNull(self.membershipSer.delete(self.membership))
    
    def test_create(self):
        self.assertNotNull(self.membershipSer.create(self.membership))
    
    def test_membership_schema(self):
        self.assertNotNull(self.membershipSer.membership_schema(self.membership))

    def test_available_memberships(self):
        self.assertNotNull(self.membershipSer.available_memberships())

    def test_create_form(self):
        self.assertNotNull(self.membershipSer.create_form(self.membership))

    def test_update_form(self):
        self.assertNotNull(self.membershipSer.update_form(self.membership))
