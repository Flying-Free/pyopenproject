from abc import ABCMeta, abstractmethod


class UserService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self, offset, pageSize, filters, sortBy): raise NotImplementedError

    @abstractmethod
    def find(self, user): raise NotImplementedError

    @abstractmethod
    def lock_user(self, user): raise NotImplementedError

    @abstractmethod
    def unlock_user(self, user): raise NotImplementedError

    @abstractmethod
    def update_user(self, user): raise NotImplementedError

    @abstractmethod
    def delete_user(self, user): raise NotImplementedError

    @abstractmethod
    def create_user(self, user): raise NotImplementedError
