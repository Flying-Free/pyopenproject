import unittest

from business.membership_service import MembershipService


class MembershipServiceTestCase(unittest.TestCase):
    membershipSer = MembershipService()

    def membership_request(self):
        self.assertNotNull(self.membershipSer.request(1))
