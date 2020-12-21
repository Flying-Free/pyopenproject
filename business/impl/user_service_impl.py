from src.extract.business.impl.user.find_all import FindAll
from src.extract.business.impl.user.find_by_context import FindByContext
from src.extract.business.impl.user.find_by_id import FindById
from src.extract.business.impl.user.lock import Lock
from src.extract.business.impl.user.unlock import Unlock
from src.extract.business.user_service import UserService


class UserServiceImpl(UserService):

    def lock_user(self, context):
        return Lock().execute()

    def unlock_user(self, context):
        return Unlock().execute()

    def find_all(self):
        find_all = FindAll()
        return find_all.execute()

    def find_by_id(self, identifier):
        find_by_id = FindById(identifier)
        return find_by_id.execute()

    def find_by_context(self, context):
        find_by_context = FindByContext(context)
        return find_by_context.execute()

    # TODO: Review what params we need to create a new user
    def new_user(self): raise NotImplementedError
