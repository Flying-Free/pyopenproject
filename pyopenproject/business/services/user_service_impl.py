from pyopenproject.business.services.command.user.create import Create
from pyopenproject.business.services.command.user.delete import Delete
from pyopenproject.business.services.command.user.find import Find
from pyopenproject.business.services.command.user.find_all import FindAll
from pyopenproject.business.services.command.user.find_by_context import FindByContext
from pyopenproject.business.services.command.user.invite import Invite
from pyopenproject.business.services.command.user.lock import Lock
from pyopenproject.business.services.command.user.unlock import Unlock
from pyopenproject.business.services.command.user.update import Update
from pyopenproject.business.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self, connection):
        super().__init__(connection)

    def lock(self, user):
        return Lock(self.connection, user).execute()

    def unlock(self, user):
        return Unlock(self.connection, user).execute()

    def find_all(self, filters=None, sort_by=None):
        return list(FindAll(self.connection, filters, sort_by).execute())

    def find(self, user):
        return Find(self.connection, user).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def update(self, user):
        return Update(self.connection, user).execute()

    def delete(self, user):
        Delete(self.connection, user).execute()

    def create(self, login, email, first_name, last_name, admin, language, status, password):
        return Create(self.connection, login, email, first_name, last_name, admin, language, status, password).execute()

    def invite(self, first_name, email):
        return Invite(self.connection, first_name, email).execute()
