from pyopenproject.business.services.impl.command import Create
from pyopenproject.business.services.impl.command import CreateForm
from pyopenproject.business.services.impl.command import Delete
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindAvailable
from pyopenproject.business.services.impl.command import FindSchema
from pyopenproject.business.services.impl.command import Update
from pyopenproject.business.services.impl.command import UpdateForm
from pyopenproject.business.services.membership_service import MembershipService


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
