from business.impl.command.work_package.find_all import FindAll
from business.impl.command.work_package.find_by_context import FindByContext
from business.impl.command.work_package.find_by_id import FindById
from business.membership_service import MembershipService


class MembershipServiceImpl(MembershipService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new membership
    def new_membership(self): raise NotImplementedError
