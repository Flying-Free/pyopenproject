import unittest

from business.membership_service import MembershipService


class MembershipServiceTestCase(unittest.TestCase):
    membershipSer = MembershipService()

    def test_find_all(self):
        self.assertNotNull(self.membershipSer.find_all())
    
    def test_find(self):
        self.assertNotNull(self.membershipSer.find(membership))

    def test_update(self):
        self.assertNotNull(self.membershipSer.update(membership))
    
    def test_delete(self):
        self.assertNotNull(self.membershipSer.delete(membership))
    
    def test_create(self):
        self.assertNotNull(self.membershipSer.create(membership))
    
    def test_membership_schema(self):
        self.assertNotNull(self.membershipSer.membership_schema(membership))

    def test_available_memberships(self):
        self.assertNotNull(self.membershipSer.available_memberships())

    def test_create_form(self):
        self.assertNotNull(self.membershipSer.create_form(membership))

    def test_update_form(self):
        self.assertNotNull(self.membershipSer.update_form(membership))
