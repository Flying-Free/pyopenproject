from business.services.impl.command.user.create import Create
from business.services.impl.command.user.delete import Delete
from business.services.impl.command.user.find import Find
from business.services.impl.command.user.find_all import FindAll
from business.services.impl.command.user.lock import Lock
from business.services.impl.command.user.unlock import Unlock
from business.services.impl.command.user.update import Update
from business.services.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self, connection):
        super().__init__(connection)

    def lock_user(self, user):
        return Lock(self.connection, user).execute()

    def unlock_user(self, user):
        return Unlock(self.connection, user).execute()

    def find_all(self, offset=1, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())

    def find(self, user):
        return Find(self.connection, user).execute()

    def update_user(self, user):
        return Update(self.connection, user).execute()

    def delete_user(self, user):
        Delete(self.connection, user).execute()

    def create_user(self, user):
        return Create(self.connection, user).execute()
