from abc import ABCMeta, abstractmethod


class UserService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def lock_user(self, context): raise NotImplementedError

    @abstractmethod
    def unlock_user(self, context): raise NotImplementedError

    # TODO: Review what params we need to create a new user
    @abstractmethod
    def new_user(self): raise NotImplementedError
