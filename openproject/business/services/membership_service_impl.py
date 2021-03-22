from openproject.business.membership_service import MembershipService
from openproject.business.services.command.membership.create import Create
from openproject.business.services.command.membership.create_form import CreateForm
from openproject.business.services.command.membership.delete import Delete
from openproject.business.services.command.membership.find import Find
from openproject.business.services.command.membership.find_all import FindAll
from openproject.business.services.command.membership.find_available import FindAvailable
from openproject.business.services.command.membership.find_schema import FindSchema
from openproject.business.services.command.membership.update import Update
from openproject.business.services.command.membership.update_form import UpdateForm


class MembershipServiceImpl(MembershipService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())

    def find(self, membership):
        return Find(self.connection, membership).execute()

    def update(self, membership):
        return Update(self.connection, membership).execute()

    def delete(self, membership):
        Delete(self.connection, membership).execute()

    def create(self, membership):
        return Create(self.connection, membership).execute()

    def membership_schema(self):
        return FindSchema(self.connection).execute()

    def available_projects(self):
        return list(FindAvailable(self.connection).execute())

    def create_form(self, membership):
        return CreateForm(self.connection, membership).execute()

    def update_form(self, membership):
        return UpdateForm(self.connection, membership).execute()
