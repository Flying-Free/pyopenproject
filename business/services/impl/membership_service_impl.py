from business.services.impl.command.membership.create import Create
from business.services.impl.command.membership.create_form import CreateForm
from business.services.impl.command.membership.delete import Delete
from business.services.impl.command.membership.find import Find
from business.services.impl.command.membership.find_all import FindAll
from business.services.impl.command.membership.find_available import FindAvailable
from business.services.impl.command.membership.find_schema import FindSchema
from business.services.impl.command.membership.update import Update
from business.services.impl.command.membership.update_form import UpdateForm
from business.services.membership_service import MembershipService


class MembershipServiceImpl(MembershipService):

    def find_all(self, filters):
        return FindAll(filters).execute()

    def find(self):
        return Find(self).execute()

    def update(self, membership):
        return Update(self, membership).execute()

    def delete(self, membership):
        Delete(self, membership)

    def create(self, membership):
        return Create(self, membership).execute()

    def membership_schema(self):
        return FindSchema(self).execute()

    def available_memberships(self):
        return FindAvailable(self).execute

    def create_form(self, membership):
        return CreateForm(self, membership).execute()

    def update_form(self, membership):
        return UpdateForm(self, membership).execute()