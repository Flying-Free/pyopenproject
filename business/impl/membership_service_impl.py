from business.impl.command.membership.find_all import FindAll
from business.impl.command.membership.find import Find

from business.membership_service import MembershipService


class MembershipServiceImpl(MembershipService):

    def find_all(self, filters):
        return FindAll(filters).execute()

    def find(self):
        return Find(self).execute()

    def update_membership(self, membership): raise NotImplementedError


    def delete_membership(self, membership): raise NotImplementedError


    def new_membership(self, membership): raise NotImplementedError


    def membership_schema(self): raise NotImplementedError


    def available_memberships(self): raise NotImplementedError
