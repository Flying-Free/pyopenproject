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

    def lock(self, user):
        return Lock(self.connection, user).execute()

    def unlock(self, user):
        return Unlock(self.connection, user).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())

    def find(self, user):
        return Find(self.connection, user).execute()

    def update(self, user_id, user):
        return Update(self.connection, user_id, user).execute()

    def delete(self, user):
        Delete(self.connection, user).execute()

    def create(self, user):
        return Create(self.connection, user).execute()
