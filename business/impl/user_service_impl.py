from business.impl.command.user.find_all import FindAll
from business.impl.command.user.find import Find
from business.impl.command.user.lock import Lock
from business.impl.command.user.unlock import Unlock
from business.impl.command.user.update import Update
from business.impl.command.user.delete import Delete
from business.impl.command.user.create import Create
from business.user_service import UserService


class UserServiceImpl(UserService):

    def lock_user(self, user):
        lock = Lock(user)
        return lock.execute()

    def unlock_user(self, user):
        unlock = Unlock(user)
        return unlock.execute()

    def find_all(self, offset, pageSize,filters, sortBy):
        find_all = FindAll(offset, pageSize,filters, sortBy)
        return find_all.execute()

    def find(self, user):
        find= Find(user)
        return find.execute()

    def update_user(self, user):
        update = Update(user)
        return update.execute()

    def delete_user(self, user):
        delete = Delete(user)
        return delete.execute()

    def new_user(self, user):
        new = Create(user)
        return new.execute()
